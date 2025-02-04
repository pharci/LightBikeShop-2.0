from db.models.user import User, UserActivity, Wishlist, Notification
from db.models.product import Product, ProductVariant, CategoryAttribute, AttributeValue, Category, Brand, Review
from db.models.store import Store, Inventory
from db.db import AsyncSessionLocal

from uuid import UUID
import bcrypt
from fastadmin import SqlAlchemyModelAdmin, SqlAlchemyInlineModelAdmin, register, WidgetType, action
from sqlalchemy import select

def setup_admin():

    class UserActivityAdminInline(SqlAlchemyInlineModelAdmin):
        model = UserActivity
        db_session_maker=AsyncSessionLocal
        list_display = ("user", "activity_type")
        list_display_links = ("user", "activity_type")
        list_filter = ("user", "activity_type")
        search_fields = ("user", "activity_type")

    @register(User, sqlalchemy_sessionmaker=AsyncSessionLocal)
    class UserAdmin(SqlAlchemyModelAdmin):
        exclude = ("hash_password",)
        list_display = ("id", "username", "is_superuser", "is_active")
        list_display_links = ("id", "username")
        list_filter = ("id", "username", "is_superuser", "is_active")
        search_fields = ("username",)
        inlines = (UserActivityAdminInline,)

        async def authenticate(self, username, password):
            sessionmaker = self.get_sessionmaker()
            async with sessionmaker() as session:
                query = select(User).filter_by(username=username, is_superuser=True)

                result = await session.scalars(query)
                user = result.first()
                if not user:
                    return None
                if not user.verify_password(password):
                    return None
                return user.id
            
        async def change_password(self, id: UUID | int, password: str) -> None:
            user = await self.model_cls.filter(id=id).first()
            if not user:
                return
            user.hash_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
            await user.save(update_fields=("hash_password",))

        @action(description="Set as active")
        async def activate(self, ids: list[int]) -> None:
            await self.model_cls.filter(id__in=ids).update(is_active=True)

        @action(description="Deactivate")
        async def deactivate(self, ids: list[int]) -> None:
            await self.model_cls.filter(id__in=ids).update(is_active=False)
            
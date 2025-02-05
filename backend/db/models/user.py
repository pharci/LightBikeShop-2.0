from sqlalchemy import Integer, String, Boolean, BigInteger, ForeignKey, Text
from db.mixin import BaseModel
import bcrypt
from sqlalchemy.orm import Mapped, mapped_column, relationship
from starlette.requests import Request

class User(BaseModel):
    __tablename__ = "users"
    
    username: Mapped[str] = mapped_column(String(20), unique=True, nullable=False)
    password_hash: Mapped[str] = mapped_column(String(255), nullable=False)
    telegram_id: Mapped[int] = mapped_column(BigInteger, unique=True, nullable=True)
    telegram_username: Mapped[str | None] = mapped_column(String(255), nullable=True, default=None)
    email: Mapped[str | None] = mapped_column(String(255), unique=True, nullable=True, default=None)
    first_name: Mapped[str | None] = mapped_column(String(255), nullable=True, default=None)
    description: Mapped[str | None] = mapped_column(String(255), nullable=True, default=None)
    phone: Mapped[str | None] = mapped_column(String(20), nullable=True, default=None)
    avatar: Mapped[str | None] = mapped_column(String(255), nullable=True, default=None)
    
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    is_staff: Mapped[bool] = mapped_column(Boolean, default=False)
    is_superuser: Mapped[bool] = mapped_column(Boolean, default=False)
    is_marketing_subscribed: Mapped[bool] = mapped_column(Boolean, default=False)

    activities: Mapped[list["UserActivity"]] = relationship("UserActivity", back_populates="user", cascade="all, delete-orphan")
    wishlist: Mapped[list["Wishlist"]] = relationship("Wishlist", back_populates="user", cascade="all, delete-orphan")
    notifications: Mapped[list["Notification"]] = relationship("Notification", back_populates="user", cascade="all, delete-orphan")
    reviews: Mapped[list["Review"]] = relationship("Review", back_populates="user", cascade="all, delete-orphan")

    def __str__(self):
        return self.username
    
    def set_password(self, password: str):
        self.password_hash = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
    
    def verify_password(self, password: str) -> bool:
        return bcrypt.checkpw(password.encode('utf-8'), self.password_hash.encode('utf-8'))

class UserActivity(BaseModel):
    __tablename__ = "user_activities"
    
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    activity_type: Mapped[str] = mapped_column(String(255), nullable=False)
    device: Mapped[str | None] = mapped_column(String(255), nullable=True)
    ip_address: Mapped[str | None] = mapped_column(String(45), nullable=True)
    
    user: Mapped["User"] = relationship("User", back_populates="activities")
    
    def __str__(self):
        return self.activity_type

class Wishlist(BaseModel):
    __tablename__ = "wishlists"
    
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    
    user: Mapped["User"] = relationship("User", back_populates="wishlist")
    
    def __str__(self):
        return "Wishlist"


class Notification(BaseModel):
    __tablename__ = "notifications"
    
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    message: Mapped[str] = mapped_column(Text, nullable=False)
    read: Mapped[bool] = mapped_column(Boolean, default=False)
    
    user: Mapped["User"] = relationship("User", back_populates="notifications")
    
    def __str__(self):
        return self.message
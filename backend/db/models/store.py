from sqlalchemy import Integer, String, Boolean, Text, ForeignKey
from sqlalchemy.orm import relationship, Mapped, mapped_column
from db.mixin import BaseModel
from starlette.requests import Request
from html import escape

class Store(BaseModel):
    __tablename__ = "stores"

    address: Mapped[str] = mapped_column(String(255), nullable=False)
    city: Mapped[str] = mapped_column(String(255), nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    working_hours: Mapped[str | None] = mapped_column(Text, nullable=True)

    inventory: Mapped[list["Inventory"]] = relationship("Inventory", back_populates="store")

    async def __admin_repr__(self, request: Request) -> str:
        return f"{self.city}, {self.address}"

    async def __admin_select2_repr__(self, request: Request) -> str:
        return f'<div><span>{escape(self.city)}, {escape(self.address)}</span></div>'
    
class Inventory(BaseModel):
    __tablename__ = "inventory"

    store_id: Mapped[int] = mapped_column(Integer, ForeignKey("stores.id", ondelete="CASCADE"), nullable=False)
    product_variant_id: Mapped[int] = mapped_column(Integer, ForeignKey("product_variants.id", ondelete="CASCADE"), nullable=False)
    quantity: Mapped[int] = mapped_column(Integer, nullable=False)

    store: Mapped["Store"] = relationship("Store", back_populates="inventory")
    variant: Mapped["ProductVariant"] = relationship("ProductVariant", back_populates="inventory")

    async def __admin_repr__(self, request: Request) -> str:
        return f"Количество: {self.quantity}"

    async def __admin_select2_repr__(self, request: Request) -> str:
        return f'<div><span>Количество: {escape(str(self.quantity))}</span></div>'
from sqlalchemy import Integer, String, Boolean, Text, ForeignKey, DECIMAL
from sqlalchemy.orm import relationship, mapped_column, Mapped
from db.mixin import BaseModel
from sqlalchemy_file import ImageField
from starlette.requests import Request
from html import escape
from markupsafe import Markup

class Product(BaseModel):
    __tablename__ = "products"
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    slug: Mapped[str] = mapped_column(String(255), unique=True, nullable=False)
    category_id: Mapped[int] = mapped_column(Integer, ForeignKey("categories.id", ondelete="CASCADE"), nullable=False)
    brand_id: Mapped[int] = mapped_column(Integer, ForeignKey("brands.id", ondelete="CASCADE"), nullable=False)
    description: Mapped[str | None] = mapped_column(Text, nullable=True)

    category: Mapped["Category"] = relationship("Category", back_populates="products")
    brand: Mapped["Brand"] = relationship("Brand", back_populates="products")
    variants: Mapped[list["ProductVariant"]] = relationship("ProductVariant", back_populates="product", cascade="all, delete-orphan")
    reviews: Mapped["Review"] = relationship("Review", back_populates="product", cascade="all, delete-orphan")

    async def __admin_repr__(self, request: Request) -> str:
        return f"{self.name}"

    async def __admin_select2_repr__(self, request: Request) -> str:
        return f'<div><span>Количество: {escape(self.name)}</span></div>'

class ProductVariant(BaseModel):
    __tablename__ = "product_variants"
    product_id: Mapped[int] = mapped_column(Integer, ForeignKey("products.id", ondelete="CASCADE"), nullable=False)
    sku: Mapped[str] = mapped_column(String(255), unique=True, nullable=False)
    barcode: Mapped[str | None] = mapped_column(String(255), nullable=True)
    price: Mapped[float] = mapped_column(DECIMAL(10, 2), nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    images: Mapped[list] = mapped_column(ImageField(thumbnail_size=(128, 128), multiple=True))

    product: Mapped["Product"] = relationship("Product", back_populates="variants")
    attributes: Mapped[list["AttributeValue"]] = relationship("AttributeValue", back_populates="variant", cascade="all, delete-orphan")
    inventory: Mapped[list["Inventory"]] = relationship("Inventory", back_populates="variant", cascade="all, delete-orphan")
    
    async def __admin_repr__(self, request: Request) -> str:
        return f"{self.sku}"

    async def __admin_select2_repr__(self, request: Request) -> str:
        img = self.images[0]

        image_url = f"{request.base_url}admin/api/file/{img['upload_storage']}/{img["thumbnail"]["file_id"]}"

        return f'''
                    <div style="display: flex; align-items: center;">
                        <img style="width: 5em; height: 5em; object-fit: cover; border-radius: 0.5em; margin-right: 1em;" 
                            src="{escape(image_url)}" 
                            alt="{escape(img['filename'])}">
                        <span>{escape(self.sku)}</span>
                    </div>
                '''

class AttributeValue(BaseModel):
    __tablename__ = 'variant_attributes'
    variant_id: Mapped[int] = mapped_column(Integer, ForeignKey('product_variants.id'), nullable=False)
    attribute_id: Mapped[int] = mapped_column(Integer, ForeignKey('category_attributes.id'), nullable=False)
    value: Mapped[str] = mapped_column(String, nullable=False)  # Значение атрибута (например, 'Красный' или 'M')

    variant: Mapped["ProductVariant"] = relationship("ProductVariant", back_populates="attributes")
    category_attribute: Mapped["CategoryAttribute"] = relationship("CategoryAttribute", back_populates="values")

    def __admin_repr__(self, request: Request):
        return f"{self.value}"


class Category(BaseModel):
    __tablename__ = "categories"
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    slug: Mapped[str] = mapped_column(String(255), unique=True, nullable=False)
    parent_id: Mapped[int | None] = mapped_column(Integer, ForeignKey("categories.id", ondelete="CASCADE"), nullable=True)
    description: Mapped[str | None] = mapped_column(Text, nullable=True)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    image: Mapped[list] = mapped_column(ImageField(thumbnail_size=(128, 128)))

    products: Mapped["Product"] = relationship("Product", back_populates="category")
    category_attributes: Mapped[list["CategoryAttribute"]] = relationship("CategoryAttribute", back_populates="category")

    def __admin_repr__(self, request: Request):
        return f"{self.name}"
    
class CategoryAttribute(BaseModel):
    __tablename__ = "category_attributes"
    category_id: Mapped[int] = mapped_column(Integer, ForeignKey("categories.id", ondelete="CASCADE"), nullable=False)
    name: Mapped[str] = mapped_column(String(255), nullable=False)  # Название атрибута
    type: Mapped[str] = mapped_column(String(255), nullable=False)  # Тип атрибута, например, 'string', 'integer', 'boolean'
    
    category: Mapped["Category"] = relationship("Category", back_populates="category_attributes")
    values: Mapped[list["AttributeValue"]] = relationship("AttributeValue", back_populates="category_attribute")

    def __admin_repr__(self, request: Request):
        return f"{self.name} ({self.type})"



class Brand(BaseModel):
    __tablename__ = "brands"
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    slug: Mapped[str] = mapped_column(String(255), unique=True, nullable=False)
    description: Mapped[str | None] = mapped_column(Text, nullable=True)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    image: Mapped[list] = mapped_column(ImageField(thumbnail_size=(128, 128)))

    products: Mapped["Product"] = relationship("Product", back_populates="brand")

    def __admin_repr__(self, request: Request):
        return f"{self.name}"

class Review(BaseModel):
    __tablename__ = "reviews"
    product_id: Mapped[int] = mapped_column(Integer, ForeignKey("products.id", ondelete="CASCADE"), nullable=False)
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    rating: Mapped[int] = mapped_column(Integer, nullable=False)
    text: Mapped[str | None] = mapped_column(Text, nullable=True)
    images: Mapped[list] = mapped_column(ImageField(thumbnail_size=(128, 128), multiple=True))

    product: Mapped["Product"] = relationship("Product", back_populates="reviews")
    user: Mapped["User"] = relationship("User", back_populates="reviews")

    def __admin_repr__(self, request: Request):
        return f"{self.user} - {self.product}"

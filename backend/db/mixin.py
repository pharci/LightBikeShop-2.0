from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy.sql import func
from sqlalchemy.types import DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship
from db.db import Base

class BaseModel(Base):
    __abstract__ = True
    id: Mapped[int] = mapped_column(primary_key=True, index=True)

    @declared_attr
    def created_at(cls) -> Mapped[DateTime]:
        return mapped_column(DateTime(timezone=True), server_default=func.now())

    @declared_attr
    def updated_at(cls) -> Mapped[DateTime]:
        return mapped_column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())
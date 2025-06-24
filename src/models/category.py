from sqlalchemy.orm import Mapped, mapped_column
from src.models.base import BaseModel
from src.core.db import db

class Category(BaseModel):
    __tablename__ = 'categories'

    name: Mapped[str] = mapped_column(
        db.String(100),
        nullable=False,
    )
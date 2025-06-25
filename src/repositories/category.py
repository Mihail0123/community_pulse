from src.models.category import Category
from src.core.db import db


class CategoryRepository:
    def get_all(self) -> list[Category]:
        return db.session.query(Category).all()

    def get_by_id(self, category_id: int) -> Category | None:
        return db.session.query(Category).get(category_id)

    def create(self, category: Category) -> Category:
        db.session.add(category)
        db.session.commit()
        db.session.refresh(category)
        return category

    def update(self, category: Category) -> Category:
        db.session.add(category)
        db.session.commit()
        return category

    def delete(self, category: Category) -> None:
        db.session.delete(category)
        db.session.commit()

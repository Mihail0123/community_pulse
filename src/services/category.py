from src.repositories.category import CategoryRepository
from src.models.category import Category


class CategoryService:
    def __init__(self):
        self.repo = CategoryRepository()

    def get_all(self) -> list[Category]:
        return self.repo.get_all()

    def get_by_id(self, category_id: int) -> Category | None:
        return self.repo.get_by_id(category_id)

    def create(self, name: str) -> Category:
        category = Category(name=name)
        return self.repo.create(category)

    def update(self, category_id: int, name: str) -> Category | None:
        category = self.repo.get_by_id(category_id)
        if not category:
            return None
        category.name = name
        return self.repo.update(category)

    def delete(self, category_id: int) -> bool:
        category = self.repo.get_by_id(category_id)
        if not category:
            return False
        self.repo.delete(category)
        return True

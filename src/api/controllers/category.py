from http import HTTPStatus
from flask import request, jsonify
from src.services.category import CategoryService
from src.dto.category import CategoryCreate, CategoryResponse, CategoryUpdate


class CategoryController:
    service = CategoryService()

    @staticmethod
    def get_all():
        categories = CategoryController.service.get_all()
        data = [CategoryResponse.from_orm(c).dict() for c in categories]
        return jsonify(data), HTTPStatus.OK

    @staticmethod
    def get_by_id(category_id: int):
        category = CategoryController.service.get_by_id(category_id)
        if not category:
            return jsonify({"detail": "Category not found"}), HTTPStatus.NOT_FOUND
        return jsonify(CategoryResponse.from_orm(category).dict()), HTTPStatus.OK

    @staticmethod
    def create():
        payload = request.get_json()
        data = CategoryCreate(**payload)
        category = CategoryController.service.create(data.name)
        return jsonify(CategoryResponse.from_orm(category).dict()), HTTPStatus.CREATED

    @staticmethod
    def update(category_id: int):
        payload = request.get_json()
        data = CategoryUpdate(**payload)
        category = CategoryController.service.update(category_id, data.name)
        if not category:
            return jsonify({"detail": "Category not found"}), HTTPStatus.NOT_FOUND
        return jsonify(CategoryResponse.from_orm(category).dict()), HTTPStatus.OK

    @staticmethod
    def delete(category_id: int):
        success = CategoryController.service.delete(category_id)
        if not success:
            return jsonify({"detail": "Category not found"}), HTTPStatus.NOT_FOUND
        return jsonify({"message": "Category deleted"}), HTTPStatus.OK

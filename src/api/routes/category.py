from flask import Blueprint
from src.api.controllers.category import CategoryController
from src.core.config import settings

category_bp = Blueprint(
    "categories",
    __name__,
    url_prefix=f"{settings.API_PREFIX}/{settings.API_VERSION}/categories"
)

category_bp.add_url_rule("", view_func=CategoryController.get_all, methods=["GET"])
category_bp.add_url_rule("", view_func=CategoryController.create, methods=["POST"])
category_bp.add_url_rule("<int:category_id>", view_func=CategoryController.get_by_id, methods=["GET"])
category_bp.add_url_rule("<int:category_id>", view_func=CategoryController.update, methods=["PUT"])
category_bp.add_url_rule("<int:category_id>", view_func=CategoryController.delete, methods=["DELETE"])

from flask import Flask
from src.api.routes.poll import polls_blueprint
from src.api.routes.category import category_bp

def register_blueprints(app: Flask) -> None:
    app.register_blueprint(polls_blueprint)
    app.register_blueprint(category_bp)

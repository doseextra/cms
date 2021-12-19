from app.http.controllers import FileController
from flask import Blueprint

file = Blueprint("file", __name__, url_prefix="/files")


@file.route("/", methods=["GET"])
def index():
    # file routes
    # Utilize para separar as rotas da lógica de sua aplicação

    return FileController.index()


def init_app(app):
    app.register_blueprint(file)

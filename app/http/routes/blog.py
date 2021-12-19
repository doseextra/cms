from app.http.controllers import BlogController
from flask import Blueprint

blog = Blueprint("blog", __name__, url_prefix="/blog")


@blog.route("/", methods=["GET"])
def index():
    return BlogController.index()

@blog.route("/<string:slug>", methods=["GET"])
def single(slug):
    return BlogController.single(slug)

def init_app(app):
    app.register_blueprint(blog)

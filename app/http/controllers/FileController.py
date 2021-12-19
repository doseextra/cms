from flask import jsonify
from app.utils.files import get_all_files, save_files


def index():
    return jsonify(get_all_files())

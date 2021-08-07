from flask import Blueprint, request, jsonify, render_template, url_for, session

from app.db import get_db, execute_query_read, execute_query_write

bp = Blueprint(
    "statistics",
    __name__,
    url_prefix="/statistics",
    template_folder="templates",
    static_folder="static",
)

# VIEWS


@bp.route("/")
def statistics():
    return render_template("statistics.html")

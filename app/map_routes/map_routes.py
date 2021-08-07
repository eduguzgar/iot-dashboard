from flask import Blueprint, request, jsonify, render_template, url_for, session

from app.db import get_db, execute_query_read, execute_query_write

bp = Blueprint(
    "map-routes",
    __name__,
    url_prefix="/map-routes",
    template_folder="templates",
    static_folder="static",
)

# VIEWS


@bp.route("/")
def map_routes():
    return render_template("map-routes.html")

import datetime

from flask import (
    Blueprint,
    request,
    jsonify,
    render_template,
    redirect,
    url_for,
    session,
)

from app.db import get_db, execute_query_read

bp = Blueprint(
    "dashboard",
    __name__,
    url_prefix="/dashboard",
    template_folder="templates",
    static_folder="static",
)


# DATA FUNCTIONS
from . import models


def get_last_date():
    """Get the last date for charts and map"""
    query = models.last_date
    rows = execute_query_read(query)

    last_date = rows[0]["last_date"]

    return last_date


def get_speed(date):
    """Get the speed data for chart"""
    query = models.speed
    rows = execute_query_read(query, date)

    # convert to list of dicts
    speed = [dict(row) for row in rows]
    # sort dicts by timestamp_utc
    speed.sort(key=lambda x: x["timestamp_utc_ms"])

    return speed


def get_map_data(date):
    """Get the map data for chart"""
    query = models.map_data
    rows = execute_query_read(query, date)

    # convert to list of dicts
    data = [dict(row) for row in rows]

    return data


def get_truck_turnaround_time():
    """Get the truck turnaround time data for chart"""
    query = models.truck_turnaround_time
    rows = execute_query_read(query)

    # convert to list of dicts
    ttt = [dict(row) for row in rows]
    # sort dicts by hour
    ttt.sort(key=lambda x: x["hour"])
    # separate ttt by both current ttt and improved ttt
    curr_ttt = [{"t": str(x["hour"]), "y": x["curr_ttt"]} for x in ttt]
    impr_ttt = [{"t": str(x["hour"]), "y": x["impr_ttt"]} for x in ttt]

    return curr_ttt, impr_ttt


# VIEW FUNCTIONS


@bp.route("/index", methods=["GET", "POST"])
def index():
    date = request.args.get("date")  # date form input

    get_db()  # connect to database and open cursor

    # if the user request 'index' without any date use last day with data
    if not date:
        date = get_last_date()
        return redirect(url_for("dashboard.index", date=date))

    speed = get_speed(date)
    curr_ttt, impr_ttt = get_truck_turnaround_time()
    map_data = get_map_data(date)

    return render_template(
        "dashboard.html",
        date=date,
        speed=speed,
        curr_ttt=curr_ttt,
        impr_ttt=impr_ttt,
        map_data=map_data,
    )

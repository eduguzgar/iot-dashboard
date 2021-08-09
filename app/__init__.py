import os
from flask import Flask, request, make_response

from functools import wraps, update_wrapper
from datetime import datetime


def create_app():
    """Create and configure the app"""

    app = Flask(__name__)

    # load the instance config, if it exists, when not testing
    app.config.from_object(os.environ["APP_SETTINGS"])

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    """ Blueprints """

    with app.app_context():

        from .dashboard import dashboard
        app.register_blueprint(dashboard.bp)

        from .statistics import statistics
        app.register_blueprint(statistics.bp)

        from .map_routes import map_routes
        app.register_blueprint(map_routes.bp)

        app.add_url_rule("/", endpoint="dashboard.index")
        app.add_url_rule("/dashboard", endpoint="dashboard.index")
        app.add_url_rule("/dashboard/", endpoint="dashboard.index")

    """ This routes """

    return app


def nocache(view):
    """Decorator for view functions to not use cache"""

    @wraps(view)
    def no_cache(*args, **kwargs):
        response = make_response(view(*args, **kwargs))
        response.headers["Last-Modified"] = datetime.now()
        response.headers[
            "Cache-Control"
        ] = "no-store, no-cache, must-revalidate, post-check=0, pre-check=0, max-age=0"
        response.headers["Pragma"] = "no-cache"
        response.headers["Expires"] = "-1"
        return response

    return update_wrapper(no_cache, view)

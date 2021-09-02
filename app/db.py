from flask import current_app, g
from flask.cli import with_appcontext

import psycopg2
from psycopg2 import pool
import psycopg2.extras


# database pool
current_app.config['DB_POOL'] = psycopg2.pool.ThreadedConnectionPool(
                                                    current_app.config["DB_POOL_MINCONN"],
                                                    current_app.config["DB_POOL_MINCONN"],
                                                    **current_app.config["DB_CONN"]
                                                    )

def check_params(params):
    """If params single object, convert to tuple"""
    if type(params) is not tuple:
        try:
            params = (params,)
        except:
            e = ("params passed cannot be "
                    +"converted to tuple")
            raise Exception(e)

    return params


def execute_query_read(query, params=None):
    """Query for read operations"""
    if params is not None:
        params = check_params(params)

    try:
        g.db_cur.execute(query, params)
        rows = g.db_cur.fetchall()
    except Exception as e:
        g.db_conn.rollback()
        rows = []
        print(e)
    else:   
        g.db_conn.commit()

    return rows


def execute_query_write(query, record):
    """Query for write operations"""
    try:
        g.db_cur.execute(query, record)
        rowid = g.db_cur.fetchone()[0]
    except Exception as e:
        g.db_conn.rollback()
        rowid = None
        print(e)
    else:
        g.db_conn.commit()

    return rowid


def get_db():
    if "db_conn" not in g:
        g.db_conn = current_app.config['DB_POOL'].getconn()
    if "db_cur" not in g:
        g.db_cur = g.db_conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)


@current_app.teardown_appcontext
def close_db(exception):
    db_conn = g.pop("db_conn", None)
    db_cur = g.pop("db_cur", None)

    if db_cur is not None:
        db_cur.close()
    if db_conn is not None:
        current_app.config['DB_POOL'].putconn(db_conn)
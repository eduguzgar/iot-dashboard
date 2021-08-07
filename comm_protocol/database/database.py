import psycopg2
from psycopg2 import pool

class DatabaseConnectionPool:
    def __init__(self, host, port, database, user, password, minconn=1, maxconn=50):
        self.host = host
        self.port = port
        self.database = database
        self.user = user
        self.password = password
        self.minconn = minconn
        self.maxconn = maxconn
        self.pool = None

    def init(self):
        self.pool = psycopg2.pool.ThreadedConnectionPool(
                                                self.minconn,
                                                self.maxconn,
                                                host = self.host,
                                                port = self.port,
                                                database = self.database,
                                                user = self.user,
                                                password = self.password
                                            )
    def get_conn(self):
        return self.pool.getconn()

    def close_conn(self, conn):
        self.pool.putconn(conn)

    def close_all_connections(self):
        self.pool.closeall()


class Database:
    def __init__(self, conn_pool):
        self.conn_pool = conn_pool
        self.cur = None
        self.conn = None

    def __del__(self):
        self.cur.close()
        self.conn_pool.close_conn(self.conn)

    def close(self):
        self.cur.close()
        self.conn_pool.close_conn(self.conn)

    def open(self):
        self.conn = self.conn_pool.get_conn()
        self.cur = self.conn.cursor()
        return self.cur

    def check_params(self, params):
        """If params is a single object, convert to tuple"""
        if type(params) is not tuple:
            try:
                params = (params,)
            except:
                e = ("params passed cannot be "
                    +"converted to tuple")
                raise Exception(e)

        return params

    def execute_query_read(self, query, params=None):
        """Query for read operations"""
        if params is not None:
            params = self.check_params(params)

        try:
            self.cur.execute(query, params)
            rows = self.cur.fetchall()
        except Exception as e:
            self.conn.rollback()
            rows = []
            print(e)
        else:   
            self.conn.commit()

        return rows

    def execute_query_write(self, query, record):
        """Query for write operations"""
        try:
            self.cur.execute(query, record)
            rowid = self.cur.fetchone()[0]
        except Exception as e:
            self.conn.rollback()
            rowid = None
            print(e)
        else:
            self.conn.commit()

        return rowid
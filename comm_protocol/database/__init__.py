import os

# database
DB_HOST = os.environ["DB_HOST"]
DB_PORT = os.environ["DB_PORT"]
DB_USER = os.environ["DB_USER"]
DB_PASS = os.environ["DB_PASS"]
DB_NAME = os.environ["DB_NAME"]

# database connection pool
DB_POOL_MINCONN = os.environ["DB_POOL_MINCONN"]
DB_POOL_MAXCONN = os.environ["DB_POOL_MAXCONN"]



import psycopg2
from psycopg2.pool import SimpleConnectionPool
from fastapi import FastAPI,Depends

DB_URL = {
    "host": "localhost",
    "database": "mydb",
    "user": "postgres",
    "password": "postgres"
}

pool: SimpleConnectionPool = None


def init_db():
    global pool
    pool = SimpleConnectionPool(
        minconn=1,
        maxconn=10,
        **DB_URL
    )
    if not pool:
        raise Exception("Failed to create connection pool")


def get_conn():
    conn = pool.getconn()
    try:
        yield conn
    finally:
        pool.putconn(conn)


def get_cursor(conn=Depends(get_conn)):
    cur = conn.cursor()
    try:
        yield cur
        conn.commit()
    except Exception:
        conn.rollback()
        raise
    finally:
        cur.close()

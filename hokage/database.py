#!/usr/bin/env python

from sqlalchemy import create_engine
from sqlalchemy import text

def connect(db=None, user=None, host=None, port=None, passwd=None, uri=None, pool_size = 50):
    try:
        print("Connecting to PostgreSQL database!")
        if uri:
            return _get_engine_from_uri(uri, pool_size = pool_size)
        return get_engine(db, user, host, port, passwd, pool_size)
    except IOError:
        print("Failed to get database connection!")
        return None, 'fail'

def get_engine(db, user, host, port, passwd, pool_size):
    uri = 'postgresql://{user}:{passwd}@{host}:{port}/{db}'.format(user=user, passwd=passwd, host=host, port=port, db=db)
    return _get_engine_from_uri(uri, pool_size=pool_size)

def _get_engine_from_uri(uri, pool_size):
    return create_engine(uri, pool_size=pool_size)

def execute(conn, sql_command):
    result = conn.execute(text(sql_command))
    try:
        return [dict(row) for row in result]
    except Exception:
        return result
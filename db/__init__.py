from flask import Flask
from flask_mysqldb import MySQL

from db.exceptions import DatabaseError

_mysql = None


def init_mysql(app: Flask):
    global _mysql
    if _mysql is None:
        _mysql = MySQL(app)


def get_connection() -> MySQL:
    if _mysql is None:
        raise DatabaseError("MySQL connection not initialized")

    return _mysql

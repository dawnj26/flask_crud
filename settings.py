from os import environ

SECRET_KEY = environ.get("SECRET_KEY")
MYSQL_USER = environ.get("MYSQL_USER")
MYSQL_PASSWORD = environ.get("MYSQL_PASSWORD")
MYSQL_DB = environ.get("MYSQL_DATABASE")
MYSQL_CURSORCLASS = "DictCursor"

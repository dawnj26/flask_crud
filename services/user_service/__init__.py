from flask import session

from db import get_connection
from models.user import User
from services.user_service.exceptions import UserFetchError

_TABLE_NAME = "users"


def get_user_by_id(user_id: int) -> User:
    conn = get_connection()
    cur = conn.connection.cursor()

    cur.execute(f"SELECT * FROM {_TABLE_NAME} WHERE id = %s", (user_id,))

    res = cur.fetchone()

    if res is None:
        raise UserFetchError(f"User id: {user_id} not found")

    user = User.from_dict(res)
    return user


def is_user_logged_in() -> bool:
    return "user_id" in session

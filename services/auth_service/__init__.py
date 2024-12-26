from flask import session
from werkzeug.security import check_password_hash

from db import get_connection
from services.auth_service.exceptions import AuthError


def signin_with_email_and_password(email: str, password: str):
    conn = get_connection()
    cur = conn.connection.cursor()

    cur.execute("SELECT id, pwd FROM users WHERE email_address = %s", (email,))
    user = cur.fetchone()

    if user is None:
        raise AuthError("User not found")

    if not check_password_hash(user["pwd"], password):
        raise AuthError("Incorrect password")

    session["user_id"] = user["id"]

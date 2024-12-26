from flask import Blueprint, render_template, request, flash, redirect, url_for, session

from services.auth_service import signin_with_email_and_password, AuthError
from services.user_service import is_user_logged_in

bp = Blueprint(
    "auth",
    __name__,
)


@bp.route("/login", methods=("GET", "POST"))
def login():
    if is_user_logged_in():
        return redirect(url_for("root.index"))

    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        if not email or not password:
            flash("Please enter your email and password.", "warning")
        else:
            try:
                signin_with_email_and_password(email, password)
            except AuthError:
                flash("Invalid email or password", "danger")
            else:
                return redirect(url_for("root.index"))

    return render_template("login.html")


@bp.route("/logout")
def logout():
    session.clear()

    return redirect(url_for("auth.login"))

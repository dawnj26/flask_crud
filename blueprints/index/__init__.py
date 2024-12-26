from flask import (
    Blueprint,
    redirect,
    url_for,
    render_template,
    session,
    flash,
    current_app,
)

from services.product_service import get_all_products
from services.user_service import is_user_logged_in, get_user_by_id, UserFetchError

bp = Blueprint(
    "root",
    __name__,
)


@bp.route("/")
def index():
    if not is_user_logged_in():
        return redirect(url_for("auth.login"))
    try:
        user = get_user_by_id(session["user_id"])
    except UserFetchError as e:
        session.pop("user_id", None)
        flash(e.message, "danger")
        return redirect(url_for("auth.login"))

    return render_template("index.html", user=user)


@bp.route("/management")
def management():
    if not is_user_logged_in():
        return redirect(url_for("auth.login"))

    user = get_user_by_id(session["user_id"])
    products = get_all_products()

    return render_template("management.html", user=user, products=products)


@bp.route("/about")
def about():
    if not is_user_logged_in():
        return redirect(url_for("auth.login"))

    user = get_user_by_id(session["user_id"])
    return render_template("about.html", user=user)

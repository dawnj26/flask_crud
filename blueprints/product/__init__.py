from flask import (
    Blueprint,
    redirect,
    url_for,
    flash,
    current_app,
    render_template,
    request,
)

from models.product import Product
from services.product_service import (
    delete_product_by_id,
    ProductDeleteError,
    add_product,
    get_product,
    ProductFetchError,
    update_product,
)
from services.user_service import is_user_logged_in

bp = Blueprint(
    "product",
    __name__,
    url_prefix="/product/",
)


@bp.route("/<int:product_id>/delete")
def delete(product_id):
    if not is_user_logged_in():
        return redirect(url_for("auth.login"))

    current_app.logger.info("Deleting product with id {}".format(product_id))

    try:
        delete_product_by_id(product_id)
    except ProductDeleteError as e:
        flash(e.message, "danger")
    else:
        flash("Product deleted successfully.", "success")

    return redirect(url_for("root.management"))


@bp.route("/add", methods=["GET", "POST"])
def add():
    if not is_user_logged_in():
        return redirect(url_for("auth.login"))

    if request.method == "POST":
        name = request.form.get("name")
        description = request.form.get("description")
        price = request.form.get("price")
        stock = request.form.get("stock")
        category = request.form.get("category")
        status = request.form.get("status")

        if (
            not name
            or not description
            or not price
            or not stock
            or not category
            or not status
        ):
            flash("Please fill all fields", "danger")
        else:
            product = Product(
                -1,
                name,
                description,
                float(price),
                int(stock),
                category,
                status,
            )
            add_product(product)
            flash("Product added successfully.", "success")

    return render_template("add_product.html")


@bp.route("/<int:product_id>/edit", methods=["GET", "POST"])
def edit(product_id):
    if not is_user_logged_in():
        return redirect(url_for("auth.login"))

    if request.method == "POST":
        name = request.form.get("name")
        description = request.form.get("description")
        price = request.form.get("price")
        stock = request.form.get("stock")
        category = request.form.get("category")
        status = request.form.get("status")

        if (
            not name
            or not description
            or not price
            or not stock
            or not category
            or not status
        ):
            flash("Please fill all fields", "danger")
        else:
            product = Product(
                product_id,
                name,
                description,
                float(price),
                int(stock),
                category,
                status,
            )
            update_product(product)
            flash("Product updated successfully.", "success")
            return redirect(url_for("root.management"))

    try:
        product = get_product(product_id)
    except ProductFetchError as e:
        flash(e.message, "danger")
        return redirect(url_for("root.management"))
    else:
        return render_template("edit_product.html", product=product)

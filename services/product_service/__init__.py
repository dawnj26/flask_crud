from db import get_connection
from models.product import Product
from services.product_service.exceptions import ProductDeleteError, ProductFetchError


def get_all_products() -> list[Product]:
    conn = get_connection()
    cur = conn.connection.cursor()
    cur.execute("SELECT * FROM products")

    products_data = cur.fetchall()
    products = [Product.from_dict(product) for product in products_data]

    return products


def delete_product_by_id(product_id: int) -> None:
    conn = get_connection()
    cur = conn.connection.cursor()
    cur.execute("DELETE FROM products WHERE id = %s", (product_id,))

    conn.connection.commit()
    if cur.rowcount == 0:
        raise ProductDeleteError("Product not found")


def add_product(product: Product) -> None:
    conn = get_connection()
    cur = conn.connection.cursor()
    cur.execute(
        "INSERT INTO products VALUES (NULL, %s, %s, %s, %s,%s,%s)",
        (
            product.name,
            product.description,
            product.price,
            product.stock,
            product.category,
            product.status,
        ),
    )
    conn.connection.commit()


def get_product(product_id: int) -> Product:
    conn = get_connection()
    cur = conn.connection.cursor()
    cur.execute("SELECT * FROM products WHERE id = %s", (product_id,))
    products_data = cur.fetchone()

    if products_data is None:
        raise ProductFetchError("Product not found")

    return Product.from_dict(products_data)


def update_product(product: Product) -> None:
    conn = get_connection()
    cur = conn.connection.cursor()
    cur.execute(
        """
        UPDATE `products`
        SET `name`=%s,`description`=%s,`price`=%s,`stock`=%s,`category`=%s,`status`=%s 
        WHERE `id`=%s
        """,
        (
            product.name,
            product.description,
            product.price,
            product.stock,
            product.category,
            product.status,
            product.id,
        ),
    )
    conn.connection.commit()

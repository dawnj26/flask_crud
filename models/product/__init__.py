class Product:
    def __init__(
        self,
        product_id: int,
        name: str,
        description: str,
        price: float,
        stock: int,
        category: str,
        status: str,
    ):
        self.id = product_id
        self.name = name
        self.description = description
        self.price = price
        self.stock = stock
        self.category = category
        self.status = status

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            product_id=data.get("id"),
            name=data.get("name"),
            description=data.get("description"),
            price=data.get("price"),
            stock=data.get("stock"),
            category=data.get("category"),
            status=data.get("status"),
        )

    def __repr__(self):
        return f"Product(id: {self.id}, name: {self.name}, description: {self.description}, price: {self.price}, stock: {self.stock}, category: {self.category}, status: {self.status})"

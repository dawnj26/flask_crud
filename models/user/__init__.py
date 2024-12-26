class User:
    def __init__(
        self,
        user_id: int,
        first_name: str,
        last_name: str,
        email: str,
        phone_number: str,
        address: str,
    ):
        self.id = user_id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone_number = phone_number
        self.address = address

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            user_id=data.get("id"),
            first_name=data.get("first_name"),
            last_name=data.get("last_name"),
            email=data.get("email_address"),
            phone_number=data.get("phone_number"),
            address=data.get("address"),
        )

    def __str__(self):
        return f"User(id={self.id}, first_name={self.first_name}, last_name={self.last_name}, email={self.email}, address={self.address})"

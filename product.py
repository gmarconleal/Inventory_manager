from exceptions import InsufficientStockError


class Product:
    def __init__(
        self,
        name,
        sku,
        price,
        quantity,
        category,
        min_stock
    ):
        if price < 0:
            raise ValueError(
                            "The price must be equal or greater than zero."
                        )
        if min_stock < 0:
            raise ValueError(
                "The minimum stock must be greater than zero"
            )

        if quantity < 0:
            raise ValueError(
                "The quantity must be greater or equal than zero"
            )
            
        self.name = name
        self.sku = sku
        self.price = price
        self.quantity = quantity
        self.category = category
        self.min_stock = min_stock

    def add_stock(self, amount):
        if amount <= 0:
            raise ValueError(
                "The added quantity must be greater than zero."
            )

        self.quantity += amount

    def remove_stock(self, amount):
        if amount <= 0:
            raise ValueError(
                "The amount removed must be greater than zero."
            )

        if amount > self.quantity:
            raise InsufficientStockError(
                self.quantity,
                amount
            )

        self.quantity -= amount

    def __str__(self):
        return (
            f"Product: {self.name}\n"
            f"SKU: {self.sku}\n"
            f"Price: R$ {self.price:.2f}\n"
            f"stock: {self.quantity}\n"
            f"Category: {self.category}\n\n"
        )
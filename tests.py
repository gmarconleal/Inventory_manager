import json
from product import Product
from supplier import Supplier

def product_to_dict(product):
    return {
        "name": product.name,
        "sku": product.sku,
        "price": product.price,
        "quantity": product.quantity,
        "category": product.category,
        "min_stock": product.min_stock
    }

def dict_to_product(product):
    return Product(
        product["name"],
        product["sku"],
        product["price"],
        product["quantity"],
        product["category"],
        product["min_stock"]
    )

def function_test():

    products = {
        "TEC001": Product(
            "Teclado",
            "TEC001",
            250,
            10,
            "Periféricos",
            3
        ),

        "MOU001": Product(
            "Mouse",
            "MOU001",
            150,
            20,
            "Periféricos",
            5
        )
    }

    data = []

    for product in products.values():
        product = product_to_dict(product)
        data.append(product)

    print(data)

function_test()



import json

from product import Product
from supplier import Supplier


# ==========================================
# PRODUCT
# ==========================================

def product_to_dict(product):
    return {
        "name": product.name,
        "sku": product.sku,
        "price": product.price,
        "quantity": product.quantity,
        "category": product.category,
        "min_stock": product.min_stock
    }


def dict_to_product(data):
    return Product(
        data["name"],
        data["sku"],
        data["price"],
        data["quantity"],
        data["category"],
        data["min_stock"]
    )


def save_products(products):
    data = []

    for product in products.values():
        data.append(product_to_dict(product))

    with open("data/products.json", "w") as file:
        json.dump(data, file, indent=4)

    print("Products saved!")


def load_products():
    with open("data/products.json", "r") as file:
        data = json.load(file)

    products = {}

    for product_data in data:
        product = dict_to_product(product_data)
        products[product.sku] = product

    return products


# ==========================================
# SUPPLIER
# ==========================================

def supplier_to_dict(supplier):
    return {
        "name": supplier.name,
        "cnpj": supplier.cnpj,
        "phone": supplier.phone,
        "email": supplier.email
    }


def dict_to_supplier(data):
    return Supplier(
        data["name"],
        data["cnpj"],
        data["phone"],
        data["email"]
    )


def save_suppliers(suppliers):
    data = []

    for supplier in suppliers:
        data.append(supplier_to_dict(supplier))

    with open("data/suppliers.json", "w") as file:
        json.dump(data, file, indent=4)

    print("Suppliers saved!")


def load_suppliers():
    with open("data/suppliers.json", "r") as file:
        data = json.load(file)

    suppliers = []

    for supplier_data in data:
        supplier = dict_to_supplier(supplier_data)
        suppliers.append(supplier)

    return suppliers
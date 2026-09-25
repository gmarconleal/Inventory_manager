import json
import os

from product import Product
from supplier import Supplier


# Cria a pasta data caso ela não exista
os.makedirs("data", exist_ok=True)


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

    with open("data/products.json", "w", encoding="utf-8") as file:
        json.dump(
            data,
            file,
            indent=4,
            ensure_ascii=False
        )



def load_products():
    with open("data/products.json", "r", encoding="utf-8") as file:
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
        "email": supplier.email,


        "products": [
            product.sku
            for product in supplier.products
        ]
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

    for supplier in suppliers.values():
        data.append(
            supplier_to_dict(supplier)
        )

    with open("data/suppliers.json", "w", encoding="utf-8") as file:
        json.dump(
            data,
            file,
            indent=4,
            ensure_ascii=False
        )

    return "Suppliers saved!"


def load_suppliers(products):
    with open("data/suppliers.json", "r", encoding="utf-8") as file:
        data = json.load(file)
        suppliers = {}
    
        for suppliers_data in data:
            supplier = dict_to_supplier(suppliers_data)
            suppliers[supplier.cnpj] = supplier
            for sku in suppliers_data.get("products", []):
                if sku in products:
                    supplier.add_product(products[sku])
        return suppliers

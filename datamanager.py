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

def supplier_to_dict(supplier):
    return {
       "name": supplier.name,
        "cnpj": supplier.cnpj,
        "phone": supplier.phone,
        "email": supplier.email
    }

def dict_to_supplier(supplier):
    return Supplier(
        supplier["name"],
        supplier["cnpj"],
        supplier["phone"],
        supplier["email"]
    )


def save_product(prod):
    product = product_to_dict(prod)
    with open("data/product.json", "w") as file:
        json.dump(product, file, indent=4)
    print('Save!')

def load_products():
    with open("data/product.json", "r") as file:
        product = json.load(file)
    return dict_to_product(product)

def save_suppliers(supplier):
    supplier = supplier_to_dict(supplier)
    with open("data/supplier.json", "w") as file:
        json.dump(supplier,file, indent=4)
    print('Saved!')

def load_suppliers():
    with open("data/supplier.json", "r") as file:
        supplier = json.load(file)
    return dict_to_supplier(supplier)

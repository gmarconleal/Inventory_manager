from product import Product
from inventory import Inventory
from supplier import Supplier

from datamanager import (
    save_products,
    load_products,
    save_suppliers,
    load_suppliers
)


# ==========================================
# INVENTORY
# ==========================================

inventory = Inventory()


# ==========================================
# PRODUCTS
# ==========================================

product1 = Product(
    "Teclado Mecânico",
    "TEC001",
    250,
    10,
    "Periféricos",
    3
)

product2 = Product(
    "Mouse Gamer",
    "MOU001",
    150,
    20,
    "Periféricos",
    5
)

product3 = Product(
    "Monitor 24",
    "MON001",
    800,
    5,
    "Monitores",
    2
)


# ==========================================
# ADD PRODUCTS TO INVENTORY
# ==========================================

inventory.add_product(product1)
inventory.add_product(product2)
inventory.add_product(product3)

print("\n========== INVENTORY ==========\n")
print(inventory)


# ==========================================
# FIND PRODUCT
# ==========================================

print("\n========== FIND PRODUCT ==========\n")

inventory.find_product(product1)


# ==========================================
# STOCK
# ==========================================

print("\n========== STOCK ==========\n")

product1.add_stock(5)

print(
    f"{product1.name}: "
    f"{product1.quantity} units"
)

product2.remove_stock(3)

print(
    f"{product2.name}: "
    f"{product2.quantity} units"
)


# ==========================================
# TOTAL VALUE
# ==========================================

print("\n========== TOTAL VALUE ==========\n")

total = inventory.total_value()

print(f"\nTotal: R$ {total:.2f}")


# ==========================================
# LOW STOCK
# ==========================================

print("\n========== LOW STOCK ==========\n")

inventory.low_stock_report()


# ==========================================
# SUPPLIER
# ==========================================

print("\n========== SUPPLIER ==========\n")

supplier = Supplier(
    "Tech Distribuidora",
    "12.345.678/0001-90",
    "11999999999",
    "contato@tech.com"
)

print(supplier)


# ==========================================
# SUPPLIER PRODUCTS
# ==========================================

supplier.add_product(product1)
supplier.add_product(product2)

print("\n========== SUPPLIER PRODUCTS ==========\n")

for product in supplier.list_products():
    print(product)


# ==========================================
# UPDATE SUPPLIER
# ==========================================

print("\n========== UPDATE SUPPLIER ==========\n")

supplier.update_contact(
    phone="11988888888"
)

print(supplier)


# ==========================================
# SAVE DATA
# ==========================================

print("\n========== SAVE DATA ==========\n")

save_products(inventory.get_products())

save_suppliers([supplier])


# ==========================================
# LOAD DATA
# ==========================================

print("\n========== LOAD DATA ==========\n")

loaded_products = load_products()
loaded_suppliers = load_suppliers()


# ==========================================
# NEW INVENTORY
# ==========================================

new_inventory = Inventory()

new_inventory.set_products(loaded_products)

print("\n========== LOADED INVENTORY ==========\n")

print(new_inventory)


# ==========================================
# LOADED SUPPLIERS
# ==========================================

print("\n========== LOADED SUPPLIERS ==========\n")

for supplier in loaded_suppliers:
    print(supplier)
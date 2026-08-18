from product import Product
from inventory import Inventory
from supplier import Supplier

from exceptions import (
    InsufficientStockError,
    DuplicateSKUError,
    ProductNotFoundError
)


def main():


    # ==========================================
    # CREATING PRODUCTS
    # ==========================================

    print("\n========== CREATING PRODUCTS ==========\n")

    mouse = Product(
        name="Mouse",
        sku="M001",
        price=100.00,
        quantity=10,
        category="Peripherals",
        min_stock=3
    )

    keyboard = Product(
        name="Keyboard",
        sku="T001",
        price=250.00,
        quantity=2,
        category="Peripherals",
        min_stock=5
    )

    monitor = Product(
        name="Monitor",
        sku="MON001",
        price=1200.00,
        quantity=8,
        category="Monitors",
        min_stock=2
    )

    print(mouse)
    print()
    print(keyboard)
    print()
    print(monitor)

    # ==========================================
    # TESTING PRODUCT.add_stock()
    # ==========================================

    print("\n========== ADDING STOCK ==========\n")

    try:
        mouse.add_stock(5)

        print("Stock added successfully.")
        print(f"New mouse stock: {mouse.quantity}")

    except ValueError as error:
        print(f"Error: {error}")

    # ==========================================
    # TESTING add_stock() WITH ZERO
    # ==========================================

    print("\n========== TESTING add_stock(0) ==========\n")

    try:
        mouse.add_stock(0)

    except ValueError as error:
        print(f"Error caught correctly: {error}")

    # ==========================================
    # TESTING add_stock() WITH NEGATIVE VALUE
    # ==========================================

    print("\n========== TESTING add_stock(-5) ==========\n")

    try:
        mouse.add_stock(-5)

    except ValueError as error:
        print(f"Error caught correctly: {error}")

    # ==========================================
    # TESTING Product.remove_stock()
    # ==========================================

    print("\n========== REMOVING STOCK ==========\n")

    try:
        mouse.remove_stock(3)

        print("Stock removed successfully.")
        print(f"New mouse stock: {mouse.quantity}")

    except ValueError as error:
        print(f"Error: {error}")

    except InsufficientStockError as error:
        print(f"Error: {error}")

    # ==========================================
    # TESTING remove_stock() WITH ZERO
    # ==========================================

    print("\n========== TESTING remove_stock(0) ==========\n")

    try:
        mouse.remove_stock(0)

    except ValueError as error:
        print(f"Error caught correctly: {error}")

    # ==========================================
    # TESTING remove_stock() WITH NEGATIVE VALUE
    # ==========================================

    print("\n========== TESTING remove_stock(-5) ==========\n")

    try:
        mouse.remove_stock(-5)

    except ValueError as error:
        print(f"Error caught correctly: {error}")

    # ==========================================
    # TESTING INSUFFICIENT STOCK
    # ==========================================

    print("\n========== TESTING INSUFFICIENT STOCK ==========\n")

    try:
        mouse.remove_stock(1000)

    except InsufficientStockError as error:
        print(f"Error caught correctly: {error}")

    # ==========================================
    # CREATING INVENTORY
    # ==========================================

    print("\n========== CREATING INVENTORY ==========\n")

    inventory = Inventory()

    # ==========================================
    # TESTING add_product()
    # ==========================================

    print("\n========== ADDING PRODUCTS TO INVENTORY ==========\n")

    inventory.add_product(mouse)
    inventory.add_product(keyboard)
    inventory.add_product(monitor)

    # ==========================================
    # TESTING DUPLICATE PRODUCT
    # ==========================================

    print("\n========== TESTING DUPLICATE PRODUCT ==========\n")
    try:
        duplicate_mouse = Product(
            name="Another Mouse",
            sku="M001",
            price=80.00,
            quantity=5,
            category="Peripherals",
            min_stock=2
        )

        inventory.add_product(duplicate_mouse)
    except DuplicateSKUError as error:
            print(f"Error caught correctly: {error}")
    # ==========================================
    # TESTING find_product()
    # ==========================================

    print("\n========== SEARCHING FOR EXISTING PRODUCT ==========\n")

    inventory.find_product(mouse)

    # ==========================================
    # TESTING find_product()
    # WITH NONEXISTENT PRODUCT
    # ==========================================

    print("\n========== SEARCHING FOR NONEXISTENT PRODUCT ==========\n")
    try:
        nonexistent_product = Product(
            name="Headset",
            sku="H001",
            price=300.00,
            quantity=4,
            category="Audio",
            min_stock=1
        )

        inventory.find_product(nonexistent_product)
    except ProductNotFoundError as error:
        print(f"Error caught correctly: {error}")


    # ==========================================
    # TESTING total_value()
    # ==========================================

    print("\n========== TOTAL INVENTORY VALUE ==========\n")

    total = inventory.total_value()

    print(f"\nTotal inventory value: R$ {total:.2f}")

    # ==========================================
    # TESTING low_stock_report()
    # ==========================================

    print("\n========== LOW STOCK REPORT ==========\n")

    inventory.low_stock_report(keyboard)

    # ==========================================
    # TESTING __str__() OF INVENTORY
    # ==========================================

    print("\n========== FULL INVENTORY ==========\n")

    print(inventory)

    # ==========================================
    # TESTING remove_product()
    # ==========================================

    print("\n========== REMOVING PRODUCT ==========\n")

    inventory.remove_product(mouse)

    # ==========================================
    # TRYING TO REMOVE AN ALREADY REMOVED PRODUCT
    # ==========================================

    print("\n========== REMOVING NONEXISTENT PRODUCT ==========\n")
    try:
        inventory.remove_product(mouse)
    except ProductNotFoundError as error:
        print(f"Error caught correctly: {error}")
    # ==========================================
    # FINAL STATE
    # ==========================================






    # Remover produto
    supplier.remove_product(product2)

    print("Produtos após remover o Mouse:")
    for product in supplier.list_products():
        print(product)

    print("\n========== FINAL INVENTORY ==========\n")

    print(inventory)


if __name__ == "__main__":
        main()
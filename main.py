from product import Product
from inventory import Inventory
from exceptions import DuplicateSKUError
from datamanager import save_products
option=0
inventory = Inventory()
while True:
    print("INVENTORY MANAGER \n 1 - Add Product \n 2 - Remove Product \n 3 - Exit")
    option = int(input("Option: "))

    if option == 1:
        print('Add product')
        name = input("Product name: ")
        sku = input("SKU: ")
        price = float(input("Price: "))
        quantity = int(input("Quantity: "))
        category = input("Category: ")
        min_stock = int(input("Minimum stock: "))

        product = Product(
            name,
            sku,
            price,
            quantity,
            category,
            min_stock
        )

        try:
            inventory.add_product(product)
            save_products(inventory.products)
            print("Product added successfully!")

        except DuplicateSKUError as error:
            print(error)
            

    if option == 3:
        print("saindo")
        quit()
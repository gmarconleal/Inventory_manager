from product import Product
from inventory import Inventory
from exceptions import DuplicateSKUError, ProductNotFoundError
from datamanager import save_products, load_products
option=0
inventory = Inventory()
while True:
    products = load_products()
    inventory.set_products(products)
    print("INVENTORY MANAGER \n 1 - Add Product \n 2 - Remove Product \n 3 - Find product \n 4 - All products \n 5 - Exit")
    option = int(input("Option: "))

    if option == 1:
        print('Add product')
        name = input("Product name: ")
        sku = input("SKU: ")
        price = float(input("Price: "))
        quantity = int(input("Quantity: "))
        category = input("Category: ")
        min_stock = int(input("Minimum stock: "))

        

        try:
            product = Product(
                        name,
                        sku,
                        price,
                        quantity,
                        category,
                        min_stock
                    )
            inventory.add_product(product)
            save_products(inventory.products)

        except DuplicateSKUError as error:
            print(error)
            
    elif option == 2:
        print('Remove product')
        sku = input("SKU: ")
        try:
            inventory.remove_product(sku)
            save_products(inventory.products)
        except ProductNotFoundError as error:
            print(error)
    elif option == 3:
        print("Find sku")
        sku = input('SKU: ')
        try:
            print(inventory.find_product(sku))
            
        except ProductNotFoundError as error:
            print(error)

    elif option == 4:
        for product in products.values():
            print(product)
        

    elif option == 5:
        print("leaving...")
        quit()
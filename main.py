from product import Product
from inventory import Inventory
from validators import validate_cnpj
from supplier import Supplier
from suppliermanager import Suppliermanager
from exceptions import DuplicateSKUError, ProductNotFoundError,DuplicateSupplierError,SupplierNotFoundError,InvalidCNPJError
from datamanager import save_products, load_products,save_suppliers,load_suppliers


def main():
    inventory = Inventory()
    inventory.set_products(load_products())
    suppliermanager = Suppliermanager()
    suppliermanager.set_suppliers(load_suppliers(inventory.get_products()))
    while True:
        print("INVENTORY MANAGER \n 1 - Add Product \n 2 - Remove Product \n 3 - Find product \n 4 - All products \n 5 - Add Supplier \n 6 - Add product to supplier \n 7 - List all suppliers\n 8 - Exit ")
        option = int(input("Option: "))

        if option == 1:
            print('Add product')
            try:
                name = input("Product name: ")
                sku = input("SKU: ")
                price = float(input("Price: "))
                quantity = int(input("Quantity: "))
                category = input("Category: ")
                min_stock = int(input("Minimum stock: "))
            except ValueError:
                print('Please enter the data correctly!')
                continue

            try:
                product = Product(name, sku, price, quantity, category, min_stock)
                inventory.add_product(product)
                save_products(inventory.get_products())
            except DuplicateSKUError as error:
                print(error)

        elif option == 2:
            print('Remove product')
            sku = input("SKU: ")
            try:
                inventory.remove_product(sku)
                save_products(inventory.get_products())
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
            for product in inventory.get_products().values():
                print(product)

        elif option == 5:
            print('Add Supplier')
            try:                
                name = input("Supplier name: ")
                cnpj = input("CNPJ: ")
                cnpj = validate_cnpj(cnpj)
                phone = input("Phone: ")
                email = input("Email: ") 
            except (ValueError, InvalidCNPJError) as error:
                print(error)
                continue
            
            try:
                 supplier = Supplier(name,cnpj,phone,email)
                 suppliermanager.add_supplier(supplier)
                 save_suppliers(suppliermanager.get_suppliers())
            except DuplicateSupplierError as error:
                            print(error)
    
        elif option == 6:
            try:
                sku = input('SKU: ')
                cnpj = input('cnpj: ')
                supplier = suppliermanager.find_supplier(cnpj)
                product = inventory.find_product(sku)
                supplier.add_product(product)
                save_suppliers(suppliermanager.get_suppliers())
            except (ProductNotFoundError,SupplierNotFoundError ) as e:
                print(f"{e}")
        
        elif option == 7:
               for supplier in suppliermanager.get_suppliers().values():
                    print(supplier)
                
        elif option == 8:
            print("Exit!")
            break


if __name__ == "__main__":
    main()
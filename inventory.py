from product import Product
from exceptions import DuplicateSKUError,ProductNotFoundError

class Inventory:
    def __init__(self):
        self.products = {}  # key: sku, value: Product object

    def add_product(self, product):
        if product.sku in self.products:
            raise DuplicateSKUError(product.sku)
        else:
            self.products[product.sku] = product
            print('Product add!')

    def remove_product(self, product):
        if product.sku not in self.products:
            raise ProductNotFoundError(product.sku)
        else:
            del self.products[product.sku]
            print('Product deleted!')
    
    def find_product(self, product):
        if product.sku in self.products:
            print(f'{product.sku} exist! ')
        else:
            raise ProductNotFoundError(product.sku)

    def total_value(self):
        total=0
        for product in self.products.values():
            value = product.price*product.quantity
            total+=value
            print(f'{product.name} - total value: R${value:.2f}')
        return total

    def low_stock_report(self, product):
        for product in self.products.values():
            if product.quantity <= product.min_stock:
                print(f'{product.name}: {product.quantity} remaining units')

    def __str__(self):
        resultado = ""
        for produto in self.products.values():
            resultado += str(produto) + "\n\n"
        return resultado
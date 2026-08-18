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

    def remove_product(self, sku):
        if sku not in self.products:
            raise ProductNotFoundError(sku)
        else:
            del self.products[sku]
            print('Product deleted!')
    
    def find_product(self, sku):
        if sku not in self.products:
            raise ProductNotFoundError(sku)

        return self.products[sku]

    def total_value(self):
        total=0
        for product in self.products.values():
            value = product.price*product.quantity
            total+=value
            print(f'{product.name} - total value: R${value:.2f}')
        return total

    def low_stock_report(self):
        for product in self.products.values():
            if product.quantity <= product.min_stock:
                print(
                    f'{product.name}: '
                    f'{product.quantity} remaining units'
                )

    def __str__(self):
        resultado = ""
        for produto in self.products.values():
            resultado += str(produto) + "\n\n"
        return resultado
class InsufficientStockError(Exception):

    def __init__(self, qty, amount):
        self.qty = qty
        self.amount = amount

        message = (
            f'Quantity: {qty}. '
            f'Attempted removal: {amount}.'
        )
  
        super().__init__(message)

class DuplicateSKUError(Exception):
    def __init__(self, sku):
        self.sku = sku
        message = (
                    f'The SKU "{sku}" already exists.'
                )

        super().__init__(message)

class DuplicateSupplierError(Exception):
    def __init__(self, cnpj):
        self.cnpj = cnpj
        message = (
                    f'The CNPJ "{cnpj}" already exists.'
                )

        super().__init__(message)

class ProductNotFoundError(Exception):
    def __init__(self,sku):
        self.sku = sku
        message = (
                f'Product {sku} not found!'
        )
        super().__init__(message)

class SupplierNotFoundError(Exception):
    def __init__(self,cnpj):
        self.cnpj = cnpj
        message = (
                f'Supplier {cnpj} not found!'
        )
        super().__init__(message)

class InvalidCNPJError(Exception):
     def __init__(self,cnpj):
            self.cnpj = cnpj
            message = (
                    f'The CNPJ {cnpj} must have 14 characters.'
            )
            super().__init__(message)
    


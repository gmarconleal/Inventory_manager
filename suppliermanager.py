from supplier import Supplier
from exceptions import DuplicateSupplierError,SupplierNotFoundError

class Suppliermanager:
    def __init__(self):
        self.suppliers = {}

    def add_supplier(self,supplier):
        if supplier.cnpj in self.suppliers:
                    raise DuplicateSupplierError(supplier.cnpj)
        self.suppliers[supplier.cnpj] = supplier
        print('Supllier add!')
    
    def find_supplier(self,cnpj):
        if cnpj not in self.suppliers:
                    raise SupplierNotFoundError(cnpj)
        return self.suppliers[cnpj]

        
    def get_suppliers(self):
        return self.suppliers
    
    def set_suppliers(self,suppliers):
        self.suppliers = suppliers
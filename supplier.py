class Supplier:
    def __init__(self, name, cnpj, phone, email):
        self.name = name
        self.cnpj = cnpj
        self.phone = phone
        self.email = email
        self.products = []
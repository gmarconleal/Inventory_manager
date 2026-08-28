class Supplier:

    def __init__(self, name, cnpj, phone, email):
        self.name = name
        self.cnpj = cnpj
        self.phone = phone
        self.email = email
        self.products = []

    def add_product(self, product):
        if product not in self.products:
            self.products.append(product)

    def remove_product(self, product):
        if product not in self.products:
            print("Your product doesn't exist")
        else:
            self.products.remove(product)
            print(f"{product} removed!")

    def list_products(self):
        return self.products

    def update_contact(self, phone=None, email=None):

        if phone is not None:
            self.phone = phone

        if email is not None:
            self.email = email

    def __str__(self):
        return (
            f"Supplier: {self.name}\n"
            f"CNPJ: {self.cnpj}\n"
            f"Phone: {self.phone}\n"
            f"Email: {self.email}"
        )
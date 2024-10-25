class Product:
    def __init__(self, name, price, description=None):
        self.name = name
        self.price = price
        self.description = description

    def __str__(self):
        return f"{self.name} - ${self.price}: {self.description or 'No description'}"

class ProductBuilder:
    def __init__(self):
        self.name = None
        self.price = None
        self.description = None

    def set_name(self, name):
        self.name = name
        return self

    def set_price(self, price):
        self.price = price
        return self

    def set_description(self, description):
        self.description = description
        return self

    def build(self):
        if not self.name or self.price is None:
            raise ValueError("Product must have a name and price.")
        return Product(self.name, self.price, self.description)

class Product:
    def __init__(self, name, price):
        self.name = name
        self._price = price

    @property
    def price(self):
        print("Getting price...")
        return self._price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Price cannot be negative.")
        print("Setting price...")
        self._price = value

    @price.deleter
    def price(self):
        print("Deleting price...")
        del self._price

product = Product("juicer Machine", 3000)
print(product.price)  # Getting price... 1000
product.price = 1500  # Setting price...
print(product.price)  # Getting price... 1500
del product.price  # Deleting price...
try:
    print(product.price)
except AttributeError:
    print("Price attribute has been deleted.")

# Attempting to set a negative price will raise an error
try:
    product.price = -50
except ValueError as e:
    print(e)  # Price cannot be negative.

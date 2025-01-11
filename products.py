class Product:
    """Represents a store product"""

    def __init__(self, name, price, quantity):
        """Initialize with name, price, and quantity"""
        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True

    def get_quantity(self) -> float:
        """returns the quantity of the corresponding product"""
        return float(self.quantity)

    def set_quantity(self, quantity):
        """Update product quantity"""
        if self.quantity + quantity < 0:
            raise Exception("not enough stock. Only {self.quantity} units available")
        self.quantity += quantity
        if self.quantity == 0:
            self.active = False
        return self.quantity

    def is_active(self) -> bool:
        """Returns whether the product is active or not"""
        return self.active

    def deactivate(self):
        """changes the state of the product"""
        self.deactivate = False

    def show(self) -> str:
        """Returns a string representation of the product"""
        return f"Product name: {self.name}, Price: {self.price}$, Stock: {self.quantity} items"

    def buy(self, quantity):
        if quantity > self.quantity:
            raise Exception(f"not enough stock. Only {self.quantity} units available")
        self.quantity -= quantity
        total_price = self.price * quantity
        return total_price
        # return f"The total price of {quantity} times {self.name} = {total_price}$"

bose = Product("Bose QuietComfort Earbuds", price=250, quantity=500)
print(bose.get_quantity())
print(bose.set_quantity(50))
print(bose.get_quantity())
print(bose.set_quantity(-150))
print(bose.get_quantity())
print(bose.show())
print(bose.buy(100))
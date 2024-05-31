class Product:
    def __init__(self, name, price, quantity):
        if not name or price < 0 or quantity < 0:
            raise ValueError("Invalid input: name cannot be empty, price and quantity must be non-negative.")
        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True

    def get_quantity(self):
        return self.quantity

    def set_quantity(self, quantity):
        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")
        self.quantity = quantity
        if self.quantity == 0:
            self.deactivate()

    def is_active(self):
        return self.active

    def activate(self):
        self.active = True

    def deactivate(self):
        self.active = False

    def show(self):
        return f"{self.name}, Price: {self.price}, Quantity: {self.quantity}"

    def buy(self, quantity):
        if not self.active:
            raise Exception("Product is not active.")
        if quantity <= 0:
            raise ValueError("Quantity to buy should be greater than zero.")
        if quantity > self.quantity:
            raise Exception("Not enough quantity in stock.")

        total_price = self.price * quantity
        self.quantity -= quantity
        if self.quantity == 0:
            self.deactivate()

        return total_price

class NonStockedProduct(Product):
    def __init__(self, name, price):
        super().__init__(name, price, quantity = 0)

    def set_quantity(self, quantity):
        raise Exception("Cannot set quantity for non-stocked product.")

    def show(self):
        return f"{self.name}, Price: {self.price}, Quantity: N/A"


class LimitedProduct(Product):
    def __init__(self, name, price, quantity, maximum):
        super().__init__(name, price, quantity)
        self.maximum = maximum

    def buy(self, quantity):
        if quantity > self.maximum:
            raise Exception(f"Cannot purchase more than {self.maximum} of this product in a single order.")
        return super().buy(quantity)

    def show(self):
        return f"{self.name}, Price: {self.price}, Quantity: {self.quantity}, Maximum per order: {self.maximum}"

# test_non_stocked = NonStockedProduct('Windows License', 125)
# print(test_non_stocked.show())
# test_limited = LimitedProduct('Shipping', 10, quantity=250, maximum=1)
# print(test_limited.show())



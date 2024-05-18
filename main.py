class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def display_info(self):
        print(f"Product Name: {self.name}")
        print(f"Price: ${self.price}")
        print(f"Quantity: {self.quantity}")


class Inventory:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)
        print(f"Added {product.name} to the inventory.")

    def update_quantity(self, product_name, quantity_change):
        for product in self.products:
            if product.name == product_name:
                product.quantity += quantity_change
                print(f"Updated {product.name}'s quantity to {product.quantity}.")
                return
        print(f"Product {product_name} not found in the inventory.")

    def total_inventory_value(self):
        total_value = sum(product.price * product.quantity for product in self.products)
        print(f"Total inventory value: ${total_value:.2f}")

    def display_all_products(self):
        for product in self.products:
            product.display_info()
            print('---')


inventory = Inventory()

inventory.add_product(Product("Laptop", 1000.00, 5))
inventory.add_product(Product("Smartphone", 500.00, 10))
inventory.add_product(Product("Headphones", 150.00, 15))

print("All products in inventory:")
inventory.display_all_products()

inventory.update_quantity("Laptop", -2)
inventory.update_quantity("Smartphone", 5)

inventory.total_inventory_value()

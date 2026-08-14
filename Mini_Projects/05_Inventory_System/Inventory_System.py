class Product:
    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity


class InventorySystem:
    def __init__(self):
        self.stock = []

    def add_product(self, product):
        for existing_product in self.stock:
            if existing_product.name == product.name:
                existing_product.quantity += product.quantity
                print(f'The product "{product.name}" was previously added to stock, the specified quantity was added to the total.')
                return

        self.stock.append(product)
        print(f'\nProduct "{product.name}" added successfully.', 40 * '~', sep = '\n')

    def remove_product(self, product_name, quantity):

        for product in self.stock:
            if product.name == product_name:

                if quantity > product.quantity:
                    print('\nThere is no such quantity of the specified product in stock.')
                    return

                if product.quantity > quantity:
                    product.quantity -= quantity
                    print(f'\n{quantity} "{product.name}" removed from stock.')
                    return

                if quantity == product.quantity:
                    self.stock.remove(product)
                    print(f'\n"{product.name}" removed from stock.')

                return

        print('\nProduct not found.')

    def check_stock(self):
        print('\n', 17 * '=', 'Products in stock', 17 * '=', sep = '\n')
        for product in self.stock:
            print(f'{product.name} - {product.quantity}')


inventory_system = InventorySystem()

inventory_system.add_product(Product('Banana', 2))
inventory_system.add_product(Product('Milk', 15))
inventory_system.add_product(Product('Banana', 10))
inventory_system.add_product(Product('Bread', 11))

inventory_system.check_stock()

inventory_system.remove_product('Banana', 10)

inventory_system.check_stock()

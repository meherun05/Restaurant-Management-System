from user import User
from restaurant import Restaurant
from menu import Menu
from order import Order

class Customer(User):
    def __init__(self, name, phone, email, address):
        super().__init__(name, phone, email, address)
        self.cart = Order()

    def showMenu(self,restaurant):
        restaurant.menu.showMenu()

    def addToCart(self, restaurant, itemName, quantity):
        item = restaurant.menu.findItems(itemName)
        if item:
            if quantity > item.quantity:
                print("Item quantity exceeded!")
            else:
                self.cart.addItem(item)
                print(f'{itemName} added to cart successfully!')
        else:
            print('Item not found!')

    def viewCart(self):
        print('*****View Cart*****')
        print("Name\tPrice\tQuantity")
        for item, quantity in self.cart.items.items():
            print(f'{item.name}\t{item.price}\t{quantity}')
        print(f'Total price: {self.cart.totalPrice}')

    def payBill(self):
        print(f'Total {self.cart.totalPrice} paid successfully!')
        self.cart.clear()

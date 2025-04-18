class Order:
    def __init__(self):
        self.items = {}

    def addItem(self,item):
        if item in self.items:
            self.items[item] += item.quantity # jodi item thake to quantity barai dibe
        else:
            self.items[item] = item.quantity

    def removeItem(self,item):
        if item in self.items:
            del self.items[item]
            
    @property
    def totalPrice(self):
        return sum(item.price * quantity for item,quantity in self.items.items())
    
    def clear(self):
        self.cart = {}
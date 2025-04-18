class Menu:
    def __init__(self):
        self.items = []

    def addMenuItem(self,item):
        self.items.append(item)
    
    def findItems(self, itemName):
        for item in self.items:
            if item.name.lower() == itemName.lower():
                return item
        return None
    
    def removeItem(self, itemName):
        item = self.findItems(itemName)
        if item:
            self.items.remove(item)
            print(f'{itemName} is removed from Menu')
        else:
            print(f'{itemName} not in menu')

    def showMenu(self):
        print('*****Menu*****')
        print("Name\tPrice\tQuantity")
        for item in self.items:
            print(f'{item.name}\t{item.price}\t{item.quantity}')

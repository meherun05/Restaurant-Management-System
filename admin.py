from user import User
from restaurant import Restaurant
from employee import Employee
from menu import Menu
class Admin(User):
    def __init__(self, name, phone, email, address):
        super().__init__(name, phone, email, address)
        
    def addEmployee(self,restaurant,employee):
        restaurant.addEmployee(employee)
    
    def viewAllEmployee(self,restaurant):
        restaurant.viewAllEmployee()
    
    def addMenuItem(self,restaurant,item):
        restaurant.menu.addMenuItem(item)
    
    def viewMenuItem(self,restaurant):
        restaurant.menu.showMenu()

    def removeMenuItem(self,restaurant,item):
        restaurant.menu.removeItem(item)

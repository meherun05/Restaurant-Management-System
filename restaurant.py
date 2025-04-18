from foodItem import FoodItem
from menu import Menu
class Restaurant:
    def __init__(self,name):
        self.name = name
        self.employees = []
        self.menu = Menu()

    def addEmployee(self,employee):
        self.employees.append(employee)
        print(f'{employee.name} has been added as employee!')

    def viewAllEmployee(self):
        if not self.employees:
            print("No employees found!")
            return
        print('Employee List!')
        for emp in self.employees:
            print(f"Name: {emp.name}, Phone: {emp.phone}, Email: {emp.email}, Address: {emp.address}, Age: {emp.age}, Designation: {emp.designation}, Salary: {emp.salary}")

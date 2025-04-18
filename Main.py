from user import User
from restaurant import Restaurant
from employee import Employee
from menu import Menu
from foodItem import FoodItem
from order import Order
from customer import Customer
from admin import Admin

mamaRestaurant = Restaurant("Mama Restaurant")
def customerList():
    name =  input('Enter your name : ')
    email =  input('Enter your email : ')
    phone =  input('Enter your phone : ')
    address =  input('Enter your address : ')

    customer = Customer(name,phone,email,address)

    while(True):
        print(f'Welcome {customer.name}')
        print("1. View Menu")
        print("2. Add item to cart")
        print("3. View cart")
        print("4. Pay Bill")
        print("5. Exit")


        choice = int(input("Enter your choice (1-5) : "))
        if choice == 1:
            customer.showMenu(mamaRestaurant)
        elif choice == 2 :
            itemName = input("Enter item name : ")
            itemQuantity = int(input("Enter item quantity : "))
            customer.addToCart(mamaRestaurant,itemName,itemQuantity)
        elif choice == 3:
            customer.viewCart()
        elif choice == 4 :
            customer.payBill()
        elif choice == 5 :
            print('Program Exit!')
            break
        else : 
            print('invalid input')

def adminList():
    name =  input('Enter your name : ')
    email =  input('Enter your email : ')
    phone =  input('Enter your phone : ')
    address =  input('Enter your address : ')

    admin = Admin(name,phone,email,address)

    while(True):
        print('Welcome Admin')
        print("1. Add new item")
        print("2. Add new employee")
        print("3. View employee")
        print("4. View Item")
        print("5. Delete Item")
        print("6. Exit")


        choice = int(input("Enter your choice (1-6) : "))
        if choice == 1:
            itemName = input("Enter item name : ")
            itemPrice = int(input("Enter item price : "))
            itemQuantity = int(input("Enter item quantity : "))
            item = FoodItem(itemName,itemPrice,itemQuantity)
            admin.addMenuItem(mamaRestaurant,item)
        elif choice == 2 :
            employeeName =  input('Enter Employee name : ')
            employeeEmail =  input('Enter Employee email : ')
            employeePhone =  input('Enter Employee phone : ')
            employeeAddress =  input('Enter Employee address : ')
            employeeAge =  input('Enter Employee age : ')
            employeeDesignation =  input('Enter Employee designation : ')
            employeeSalary =  input('Enter Employee salary : ')
            employee = Employee(employeeName,employeePhone,employeeEmail,employeeAddress,employeeAge,employeeDesignation,employeeSalary)
            admin.addEmployee(mamaRestaurant,employee)
        elif choice == 3:
            admin.viewAllEmployee(mamaRestaurant)
        elif choice == 4 :
            admin.viewMenuItem(mamaRestaurant)
        elif choice == 5 :
            itemName = input("Enter item name : ")
            admin.removeMenuItem(mamaRestaurant,itemName)
        elif choice == 6:
             print('Program Exit!')
             break
        else : 
            print('invalid input')

while True:
    print("Welcome!!")
    print("1. Customer")
    print("2. Admin")
    print("3. Exit")

    choice = int(input("Enter your choice (1-3) : "))
    if choice == 1:
        customerList()
    elif choice == 2 :
        adminList()
    elif choice == 3:
        print('Program Exit!')
        break
    else :
        print("Invalid choice!")

# ad = Admin('Shahin Mia',3424,'shahin@gmail.com','Mirpur')
# # emp = Employee('Shahin Mia',3424,'shahin@gmail.com','Mirpur',18,'Manager',1230000)
# res = Restaurant('Meherun Kitchen')
# # ad.addEmployee(res,emp)
# # ad.viewAllEmployee(res)

# item = FoodItem('Burger',20,10)
# item2 = FoodItem('Pizza',30,4)
# menu = Menu()
# ad.addMenuItem(res,item)
# ad.addMenuItem(res,item2)
# # menu.showMenu()

# cus = Customer('Mehrima',2663,'mehrima@gmail.com','some')
# cus.showMenu(res)
# # cus.addToCart(res,'Burgur',3)
# # cus.viewCart()

# itemName = input("Enter item name : ")
# itemQuantity = int(input("Enter item quantity : "))

# cus.addToCart(res,itemName,itemQuantity)
# cus.viewCart()
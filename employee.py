from user import User
class Employee(User):
    def __init__(self, name, phone, email, address,age,designation,salary):
        super().__init__(name, phone, email, address) # for use the parent attribute
        self.age = age
        self.designation = designation
        self.salary = salary

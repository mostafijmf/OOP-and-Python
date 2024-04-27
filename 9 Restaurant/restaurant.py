from menu import Menu

class Restaurant:
    def __init__(self, name):
        self.name = name
        self.employees = []
        self.menu = Menu()

    def add_employee(self, employee):
        self.employees.append(employee)

    def view_employee(self):
        print("Employee List:")
        for emp in self.employees:
            print(f"Name: {emp.name}, Phone: {emp.phone}, Email {emp.email}, Address: {emp.address}, Age: {emp.age}, Destination: {emp.destination}, Salary: {emp.salary}")

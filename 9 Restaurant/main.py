from users import Customer, Employee, Admin
from restaurant import Restaurant
from menu import Menu
from food_item import FoodItem
from orders import Order


res = Restaurant("Ajaira Restaurant")


def customer_menu():
    name = input("Enter your name: ")
    email = input("Enter your email: ")
    phone = input("Enter your phone: ")
    address = input("Enter your address: ")
    customer = Customer(name=name, email=email, phone=phone, address=address)

    while True:
        print(f"Welcome {customer.name}")
        print("1. View Menu")
        print("2. Add Item to Cart")
        print("3. View Cart")
        print("4. PayBill")
        print("5. Exit")

        choice = int(input(f"Enter your choice: "))
        if choice == 1:
            customer.view_menu(res)
        elif choice == 2:
            item_name = input("Enter item name: ")
            item_quantity = int(input("Enter item quantity: "))
            customer.add_to_cart(res, item_name, item_quantity)

        elif choice == 3:
            customer.view_cart()
        elif choice == 4:
            customer.pay_bill()
        elif choice == 5:
            break
        else:
            print("Invalid input")


def admin_menu():
    name = input("Enter your name: ")
    email = input("Enter your email: ")
    phone = input("Enter your phone: ")
    address = input("Enter your address: ")
    admin = Admin(name=name, email=email, phone=phone, address=address)

    while True:
        print(f"Welcome {admin.name}")
        print("1. Add New Item")
        print("2. Add New Employee")
        print("3. View Employee")
        print("4. View Items")
        print("5. Delete Item")
        print("6. Exit")

        choice = int(input(f"Enter your choice: "))
        if choice == 1:
            item_name = input("Enter Item Name: ")
            item_price = int(input("Enter Item Price: "))
            item_quantity = int(input("Enter Item Quantity: "))
            item = FoodItem(item_name, item_price, item_quantity)
            admin.add_new_item(res, item)

        elif choice == 2:
            name = input("Enter employee name: ")
            phone = input("Enter employee phone: ")
            email = input("Enter employee email: ")
            address = input("Enter employee address: ")
            age = input("Enter employee age: ")
            destination = input("Enter employee destination: ")
            salary = input("Enter employee salary: ")
            employee = Employee(name, phone, email, address, age, destination, salary)
            admin.add_employee(res, employee)

        elif choice == 3:
            admin.view_employee(res)
        elif choice == 4:
            admin.view_menu(res)
        elif choice == 5:
            item_name = input("Enter Item Name: ")
            admin.remove_item(res, item_name)
        elif choice == 6:
            break
        else:
            print("Invalid input")

while True:
    print("**************** Welcome! ****************")
    print("1. Customer")
    print("2. Admin")
    print("3. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        customer_menu()
    elif choice == 2:
        admin_menu()
    elif choice == 3:
        break
    else:
        print("Invalid input")
from fooditem import FoodItem
from menu import Menu
from user import Customer,Admin,Employee
from restaurent import Restaurent
from orders import Order

mamar_restaurent = Restaurent("Mamar Restaurent")
def customer_menu():
    name = input("Enter your name: ")
    email = input("Enter your email: ")
    phone = input("Enter your Phone: ")
    address = input("Enter your Address: ")
    customer = Customer(name=name,email=email,phone=phone,address=address)
    
    while True:
        print(f'Welcome {customer.name}')
        print(f'1. View Menu')
        print(f'2. Add item to cart')
        print('3. View Cart')
        print("4. PayBill")
        print('5. Exit')
        
        choice = int(input('Enter your choice: '))
        if choice == 1:
            customer.view_menu(mamar_restaurent)
        elif choice == 2:
            item_name = input("Enter item name: ")
            item_quantity = input("Enter item quantity: ")
            customer.add_to_cart(mamar_restaurent,item_name,item_quantity)
        elif choice == 3:
            customer.view_cart()
        elif choice == 4:
            customer.pay_bill()
        elif choice == 5:
            break
        else:
            print("invalid choice")
def admin_menu():
    name = input("Enter your name: ")
    email = input("Enter your email: ")
    phone = input("Enter your Phone: ")
    address = input("Enter your Address: ")
    admin = Admin(name=name,email=email,phone=phone,address=address)
    
    while True:
        print(f'Welcome {admin.name}')
        print(f'1. Add New Item')
        print(f'2. Add New Employee')
        print('3. View Employee')
        print("4. View Items")
        print('5. Delete Item')
        print("6. Exit")
        choice = int(input('Enter your choice: '))
        if choice == 1:
            item_name = input("Enter item name: ")
            item_price = int(input("Enter Item price: "))
            item_quantity = int(input("Enter Item quantity: "))
            item = FoodItem(item_name,item_price,item_quantity)
            admin.add_new_item(mamar_restaurent,item)
            
        elif choice == 2:
            name = input("Enter Emplyee name: ")
            phoney = input("Enter Employee Phone: ")
            email = input("Enter Employee email: ")
            designation = input("Enter Employee designation: ")
            age = input("Enter Employee age: ")
            salary = input("Enter Employee salary: ")
            address = input("Enter Employee address: ")
            employee = Employee(name, phone, email, address,age,designation,salary)
            admin.add_employee(mamar_restaurent,employee)
            
        elif choice == 3:
            admin.view_employee(mamar_restaurent)
        elif choice == 4:
            admin.view_menu(mamar_restaurent)
        elif choice == 5:
            item_name = input("Enter Item name: ")
            admin.remove_item(mamar_restaurent,item_name)
        elif choice == 6:
            break
        else:
            print("invalid choice")

while True:
    print("Welcome!!")
    print("1. Customer")
    print("2. Admin")
    print("3. Exit")
    choice = int(input("Enter your chocie: "))
    if choice == 1:
        customer_menu()
    elif choice == 2:
        admin_menu()
    elif choice == 3:
        break
    else:
        print("Invalid Input")
        
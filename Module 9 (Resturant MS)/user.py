# customer
# Employee
# Admin

from abc import ABC
from orders import Order
class User(ABC):
    def __init__(self,name,phone,email,address):
        self.name = name
        self.email = email
        self.phone = phone 
        self.address = address


class Customer(User):
    def __init__(self, name, phone, email, address):
        super().__init__(name, phone, email, address)
        self.cart = Order()
        
    def view_menu(self,restaurent):
        restaurent.menu.show_menu()
    
    def add_to_cart(self,restaurent,item_name,quantity):
        item = restaurent.menu.find_item(item_name)
        # print(item.quantity)
        if item:
            if int(quantity) > int(item.quantity):
                print('Item Quantity exceeded')
            else:
                item.quantity = quantity
                self.cart.add_items(item)
                print('Item Added')
        else:
            print('Item not found')
            
    def view_cart(self):
        print('-------view Cart--------')
        print('Name\tPrice\tQuantity') 
        for item, quantity in self.cart.items.items():   # changes from self.cart.items() to now 
            print(f"{item.name}\t{item.price}\t{quantity}")
        print(f'Total price : {self.cart.total_price}')
    def pay_bill(self):
        print(f'Total {self.cart.total_price} paid successfully')
        self.cart.clear()   
        
class Employee(User):
    def __init__(self, name, phone, email, address,age,designation,salary):
        super().__init__(name, phone, email, address)
        self.age = age
        self.designation = designation
        self.salary = salary
        
# emp = Employee('kamrul',213,'kamrul@gmail.com','ctg',23,'chef',12000)
# print(emp.name)

class Admin(User):
    def __init__(self, name, phone, email, address):
        super().__init__(name, phone, email, address)
       
        
    def add_employee(self,restaurent,employee):
        if employee not in restaurent.employees:  
            restaurent.add_employee(employee)
        else:
            print(f"Employee {employee.name} already exists")
        
        
    def view_employee(self, restaurent):
        print("Admin is viewing employees:")
        restaurent.view_employee()
        
    def add_new_item(self,restaurent,item):
        restaurent.menu.add_menu_item(item)
    
    def remove_item(self,restaurent,item):
        restaurent.menu.remove_item(item)

    def view_menu(self,restaurest):
        restaurest.menu.show_menu()
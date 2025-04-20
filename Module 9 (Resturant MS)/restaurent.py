from menu import Menu
from user import Employee

class Restaurent:
    def __init__(self,name):
        self.name = name
        self.employees = [] # eta hoccea amader database
        self.menu = Menu()
   
    def add_employee(self,employee):
        #employee class er ekta object create hobe 
        # employee = Employee(employee)
        self.employees.append(employee)

    def view_employee(self):
        print('Employee List')
        
        # print('Name\tEmail\tPhone\tAddress')
        # for emp in self.employees:
        #     print(f'{emp.name}\t{emp.email}\t{emp.phone}\t{emp.address}')
        
        print(f'{"Name":<15}{"Email":<25}{"Phone":<15}{"Address":<20}')
        print('-' * 75)
        for emp in self.employees:
            print(f'{emp.name:<15}{emp.email:<25}{emp.phone:<15}{emp.address:<20}')

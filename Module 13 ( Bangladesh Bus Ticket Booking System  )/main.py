from bus_system import BusSystem,Admin
from user import Bus,Passenger

def admin_menu():
    print("Welcome Admin")
    print('1. Add Bus')
    print('2. View All Buses')
    print('3. Logout')
    
def user_menu():
    print('Welcome User')
    print("1. Admin Login")
    print("2. Book Ticket")
    print('3. View all buses')
    print('4. Exit')

def main():
    bus_system = BusSystem()
    admin = Admin()
    while True:
        user_menu()
        choice = int(input("Enter your choice: "))
        if choice == 1:
            username = input("Enter username: ")
            password = input("Enter password: ")
            if admin.login(username,password):
                while True:
                    admin_menu()
                    choice = int(input("Enter your choice: "))
                    if choice == 1:
                        number = input("Enter bus number: ")
                        route = input("Enter bus Route: ")
                        seats = int(input("Enter total seats: "))
                        admin.add_bus(number,route,seats)
                    elif choice == 2:
                        bus_system.view_bus()
                    elif choice == 3:
                        print("Logout Successfully")
                        break
                    else:
                        print("Invalid choice")
        elif choice == 2:    
            name = input("Enter your name: ")
            phone = input("Enter your phone number: ")
            bus_number = input("Enter bus number: ")
            seats = int(input("Enter the number of seats you want to book: "))
            bus_system.book_ticket(bus_number,name,phone,seats)
        elif choice == 3:
            bus_system.view_bus()
        elif choice == 4:
            print("Thank you for using our service")
            break
        else:
            print("Invalid choice")


main() 
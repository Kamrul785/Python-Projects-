from user import Bus,Passenger
class BusSystem:
    buses = []
    passengers = []
    def add_passenger(self,passenger):
        self.passengers.append(passenger)
        print(f'Passenger {passenger.name} added successfully')
        
    def find_bus(self,bus_number):
        for bus in self.buses:
            if bus.number == bus_number:
                return bus
        print(f'Bus {bus_number} not found')
        return None
    
    def book_ticket(self,bus_number,name,phone,seats):
        bus = self.find_bus(bus_number)
        if bus:
            if bus.available_seats() >= seats:
                bus.book_seat(seats)
                passenger = Passenger(name,phone,bus)
                self.add_passenger(passenger)
                fare = seats * 500
                
                print(f'{seats} ticket booked successfully')
                print(f'Total Fare is: {fare} taka, please pay for confirm the ticket')
            else:
                print(f'{seats} seats not available at that moment ')
    
    def view_bus(self):
        print(f'{'Bus Numer':<15} {'Route': <15} {"Available Seats":<15}')
        for bus in self.buses:
            print(f'{bus.number:<15} {bus.route:<15} {bus.available_seats():<15}')
     
class Admin(BusSystem):
    def __init__(self):
        super().__init__()
        self.username = 'admin'
        self.password = '1234'
    
    def login(self,username,password):
        if username == self.username and password == self.password:
            print("Login as a admin successfull")
            return True
        else:
            print('login failed, Try again')
            return False
            
    def add_bus(self, number, route, seats):
        for bus in self.buses:
            if bus.number == number:
                print(f"Bus with number {number} already exists.")
                return
        bus = Bus(number, route, seats)
        self.buses.append(bus)
        print(f'Bus {number} added successfully')
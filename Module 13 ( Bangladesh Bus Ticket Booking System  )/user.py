from abc import ABC

class Bus(ABC):
    def __init__(self,number,route, total_seats):
        self.number = number
        self.route = route
        self.total_seats = total_seats
        self.booked_seats = 0
    
    def available_seats(self):
        return self.total_seats - self.booked_seats
    
    def book_seat(self, seats):
        if self.available_seats() >= seats:
            self.booked_seats += seats
            self.total_seats -= seats
            
        else:
            print(f'{seats} seats not available at that moment')
    
class Passenger:
    def __init__(self,name, phone,bus):
        self.name = name
        self.phone = phone
        self.bus = bus
        

    
    
     
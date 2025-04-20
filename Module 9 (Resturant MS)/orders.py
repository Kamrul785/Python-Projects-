class Order:
    def __init__(self):
        self.items = {} # changes here [] to {}
        
    def add_items(self,item):
        if item in self.items:
            self.items[item.name] += int(item.quantity) # jodi item ta cart a already thake
        else:
            self.items[item.name] = int(item.quantity) # cart a item jodi na thake
    
    def remove(self,item):
        if item in self.items:
            del self.items[item]
    
    @property
    def total_price(self):
        return sum(int(item.price) *int(quantity) for item,quantity in self.items.items())
    
    def clear(self):
        self.items = {}
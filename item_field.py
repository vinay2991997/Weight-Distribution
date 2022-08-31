class Item_field:
    def __init__(self,name,quantity,weight):
        self.name = name
        self.quantity = quantity
        self.weight = weight
        self.total_weight = round(self.quantity * self.weight)
    
    def __repr__(self) -> str:
        return f'{self.quantity} {self.name} [{str(self.total_weight)}]'
    
    def update_quantity(self, quantity):
        if quantity >= 0:
            self.quantity = quantity
        self.calculate_total_weight()
            
    def update_name(self, name, weight):
        self.name = name
        self.weight = weight
        self.calculate_total_weight()
        
    def calculate_total_weight(self):
        self.total_weight = round(self.quantity * self.weight)
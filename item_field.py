class item_field:
    def __init__(self,name,quantity,weight):
        self.name = name
        self.quantity = quantity
        self.weight = weight
        self.total_weight = round(self.quantity * self.weight)
    
    def __repr__(self) -> str:
        # return 'item name : ' + self.name + '\nitem weight : ' + str(self.weight) + '\nitem quantity : ' + str(self.quantity) + '\nTotal Weight : ' + str(self.total_weight)
        return str(self.quantity) + ' ' + self.name + ' [' + str(self.total_weight) +']'
    pass

def sum_of_list_of_item_field(item_field_list):
    return sum([item.total_weight for item in item_field_list])
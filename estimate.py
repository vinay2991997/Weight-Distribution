from datetime import datetime
from item_field_list import Item_field_list


class Estimate:
    def __init__(self, estimate_no) -> None:
        self.estimate_no = f'E-{int(estimate_no)}'
        self.date_time = datetime.now()
        self.item_field_list = Item_field_list()
    
    def get_number_of_items(self):
        return len(self.item_field_list)
    
    def get_estimate_no(self):
        return self.estimate_no
    
    def add_item_field_list(self, item_field):
        try:
            iter(item_field)
        except:
            self.item_field_list.add_item(item_field)
        else:
            self.item_field_list.add_item_list(item_field)
            
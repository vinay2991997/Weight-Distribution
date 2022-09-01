from datetime import datetime
from item_field_list import Item_field_list
from packing_slip import Packing_slip
from weight_distribution import weight_distribution


class Estimate:
    def __init__(self, estimate_no) -> None:
        self.estimate_no = f'E-{int(estimate_no)}'
        self.date_time = datetime.now()
        self.item_field_list = Item_field_list([])
        self.packing_slip = Packing_slip(self.estimate_no,[])
    
    def make_packing_slip(self):
        self.packing_slip = Packing_slip(self.estimate_no,[])
        weight_distribution(self.item_field_list,self.packing_slip.bale_list)
    
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
            
    def __repr__(self) -> str:
        data_str = []
        data_str.append(f'\n{" "*8} ESTIMATE')
        data_str.append(f'  {self.estimate_no} {" "*10} {self.date_time.date()}')
        
        data_str.append(str(self.item_field_list))
        
        data_str.append(str(self.packing_slip))
        
        return '\n'.join(data_str)
        
        
            
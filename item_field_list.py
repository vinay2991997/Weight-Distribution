class Item_field_list:
    
    item_fields = []
    def __init__(self, item_fields) -> None:
        self.item_fields = item_fields
        pass
    
    def add_item(self, item_field):
        self.item_fields.append(item_field)
        
    def __iter__(self):
        return iter(self.item_fields)
    
    def add_item_list(self, item_field_list):
        for item in item_field_list:
            self.add_item(item)
    
    def sum_of_total_weights(self):
        return sum([item_field.total_weight for item_field in self.item_fields])
    
    def filter(self, item_name):
        filtered_list = Item_field_list([])
        for item_field in self.item_fields:
            if item_field.name.upper().find(item_name.upper()) != -1:
                filtered_list.item_fields.append(item_field)
    
        return filtered_list
    
    def filter_out_one(self, item_name_long):
        local_list = self
        item_name_long_segregated_list = item_name_long.split(' ')
        for item_to_be_searched in item_name_long_segregated_list:
            local_list = local_list.filter(item_to_be_searched)

        if local_list.get_length() == 1:
            return local_list.item_fields[0]
        else:
            return None
    
    def __repr__(self) -> str:
        data_str = []
        for item in self.item_fields:
            data_str.append(str(item))
            
        data_str.append(f'Total Sum : {self.sum_of_total_weights()}')
        return '\n'.join(data_str)
        
    def get_length(self):
        return len(self.item_fields)
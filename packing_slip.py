from datetime import datetime
import os


class Packing_slip:
    
    def __init__(self,estimate_no, bale_list) -> None:
        self.estimate_no = estimate_no
        self.bale_list = bale_list
        self.no_of_bales = len(bale_list)
        self.date_time = datetime.now()
      
    def generate_file(self):
        folder_name = "Estimate"
        try:
            os.makedirs(folder_name)
        except:
            pass
        file_name = self.estimate_no + '.txt'
        file_object = open(f'{folder_name}/{file_name}',"w")
        file_object.write(str(self))
        file_object.close()
      
    def __repr__(self) -> str:
        data_str = []
        data_str.append(f'\n{" "*8} PACKING SLIP')
        data_str.append(f'  {self.estimate_no} {" "*10} {self.date_time.date()} {self.date_time.time()}')
        for item_field_list in self.bale_list:
            data_str.append('-'*40)
            data_str.append(str(item_field_list))
        return '\n'.join(data_str)
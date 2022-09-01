

from estimate import Estimate
from item_field import Item_field
from item_field_list import Item_field_list
from miscellenious import read_csv_file

print('Enter Estimate no : ')
estimate_no = int(input())
estimate = Estimate(estimate_no)

mydict = read_csv_file()

csv_item_field_list = Item_field_list([])
for key,value in mydict.items():
    csv_item_field_list.add_item(Item_field(key,0,value))

while True:
    print('Enter item name : ')
    item_name = str(input())

    if item_name == '--':
        break

    actual_item = csv_item_field_list.filter_out_one(item_name)

    if actual_item is not None :
        print('Enter Quantity : ')
        quantity = int(input())

        item = Item_field(actual_item.name,quantity,mydict[actual_item.name])
        estimate.add_item_field_list(item)
    
    else:
        print('\nPLEASE re-enter item name correctly!!\n'.upper())
    

while True:
    estimate.make_packing_slip()
    print(estimate)
    
    print('Reshuffle Packing List (y/n) : ')
    reply = str(input())
    if (reply.upper() != 'Y'):
        break

# print(estimate.packing_slip)
## get list of items from file
# mydict = get_all_item_list()

## get estimate no.
# estimate_no = str(input())

## get items and quantity
# item_list = get_item_list()

## calculate
# result = []
# weight_distribute(item_list, result)

## dispay the result
# display(result)

## make a packing slip
# make a file with name estimate no which have packing slip

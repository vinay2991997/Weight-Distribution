import csv
from item_field import item_field, sum_of_list_of_item_field
from weight_distribution import weight_distribution

mydict = {}

with open('item_list.csv', mode='r') as infile:
    reader = csv.reader(infile)
    mydict = {rows[0]:float(rows[4]) for rows in reader}


def find_item(item_list,item_name):
    no_of_found = 0
    actual_item_name = ''
    for item in item_list:
        if item.find(item_name.upper()) != -1:
            no_of_found += 1
            actual_item_name = item
    # print('no of found items : ' + str(no_of_found))
    if no_of_found == 1:
        return actual_item_name
    else:
        return None


def filter_list(item_list, item_name):
    filtered_list = []
    for item in item_list:
        if item.find(item_name.upper()) != -1:
            filtered_list.append(item)
    
    return filtered_list


def filter_out_one(item_list, item_name_long):
    local_list = item_list
    item_name_long_segregated_list = item_name_long.split(' ')
    for item_to_be_searched in item_name_long_segregated_list:
        local_list = filter_list(local_list,item_to_be_searched)

    if len(local_list) == 1:
        return local_list[0]
    else:
        return None

item_list = []
item_name_list = list(mydict.keys())

print('Enter Estimate no : ')
estimate_no = str(input())
file_name = f'E-{estimate_no}.txt'
file_object = open(file_name,'w')
file_object.write(f'{" "*10}{file_name[:-4]}\n\n{"-"*40}\n\n')

while True:
    
    print('Enter item name : ')
    item_name = str(input())

    if item_name == '--':
        break

    actual_item_name = filter_out_one(item_name_list, item_name)

    if actual_item_name is not None :
        print('Enter Quantity : ')
        quantity = int(input())

        item = item_field(actual_item_name,quantity,mydict[actual_item_name])
        item_list.append(item)
    
    else:
        print('\nPLEASE re-enter item name correctly!!\n'.upper())
    
result = []
weight_distribution(item_list,result)

for data in item_list:
    print(data)
    
print()
print('Total sum of all weight : ' + str(sum_of_list_of_item_field(item_list)))
print('No. of bales : ' + str(len(result)))
print()

for data in result:
    # print(data)
    for item in data:
        print(item)
        file_object.write(f'{str(item)}\n')
    bale_sum = sum_of_list_of_item_field(data)
    print('Bale Sum : ' + str(bale_sum))
    file_object.write(f'Bale Sum : {str(bale_sum)}\n')

    print('-'*40)
    file_object.write(f'{"-"*40}'
                      f'\n')
    file_object.write('\n')
    print()
    
file_object.close()

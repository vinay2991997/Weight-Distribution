import csv


def read_csv_file():
    with open('item_list.csv', mode='r') as infile:
        reader = csv.reader(infile)
        mydict = {rows[0]:float(rows[4]) for rows in reader}
    return mydict
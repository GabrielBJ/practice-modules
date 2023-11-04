#!/usr/bin/env python3

import csv

class Item(object):

    # init function
    def __init__(self):
        self.name = ""
        self.quantity = 0
        self.unitprice = 0.0
        self.total = 0.0

# We want to define reader 
reader = csv.reader(open("shopping.csv", "r"))

headings = None

shopping_list = []

for row in reader:
    if headings == None:
        # First row
        headings = row
    else:
        my_item = Item()
        my_item.name = row[headings.index("item")]
        my_item.quantity = int(row[headings.index("quantity")])
        my_item.unitprice = row[headings.index("unit price")]
        my_item.total = row[headings.index("total")]

        shopping_list.append(my_item)

for i in shopping_list:
    print ("item: {}, quantity: {}, unit price: {}, total: {}".format(i.name, i.quantity, i.unitprice, i.total))

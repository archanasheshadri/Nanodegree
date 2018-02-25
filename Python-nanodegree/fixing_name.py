# -*- coding: utf-8 -*-
"""
Created on Thu Nov 30 15:29:29 2017

@author: archa
"""

"""
In this problem set you work with cities infobox data, audit it, come up with a
cleaning idea and then clean it up.

In the previous quiz(fixiing_the_area) you recognized that the "name" value can be an array (or
list in Python terms). It would make it easier to process and query the data
later if all values for the name are in a Python list, instead of being
just a string separated with special characters, like now.

Finish the function fix_name(). It will recieve a string as an input, and it
will return a list of all the names. If there is only one name, the list will
have only one item in it; if the name is "NULL", the list should be empty.
The rest of the code is just an example on how this function can be used.
"""
import codecs
import csv
import pprint

CITIES = 'cities.csv'


def fix_name(name):

    if name == 'NULL':
        name = []
    else:
            
        name_split =  name.split('|')
        #print area_split
        if len(name_split) > 1:
            name_split[0] = name_split[0][1:]
            name_split[1] = name_split[1][:-1]            
            name = name_split                    
        else:
            #print area_split[0] 
            name = name_split
    

    return name


def process_file(filename):
    data = []
    with open(filename, "r") as f:
        reader = csv.DictReader(f)
        #skipping the extra metadata
        for i in range(3):
            l = reader.next()
        # processing file
        for line in reader:
            # calling your function to fix the area value
            if "name" in line:
                line["name"] = fix_name(line["name"])
            data.append(line)
    return data


def test():
    data = process_file(CITIES)

    print "Printing 20 results:"
    for n in range(20):
        pprint.pprint(data[n]["name"])

    
if __name__ == "__main__":
    test()

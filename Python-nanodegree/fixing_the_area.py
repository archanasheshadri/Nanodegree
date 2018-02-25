# -*- coding: utf-8 -*-
"""
Created on Wed Nov 29 15:45:15 2017

@author: archa
"""

"""
In this problem set you work with cities infobox data, audit it, come up with a
cleaning idea and then clean it up.

Since in the previous quiz you made a decision on which value to keep for the
"areaLand" field, you now know what has to be done.

Finish the function fix_area(). It will receive a string as an input, and it
has to return a float representing the value of the area or None.
You have to change the function fix_area. You can use extra functions if you
like, but changes to process_file will not be taken into account.
The rest of the code is just an example on how this function can be used.
"""
import codecs
import csv
import json
import pprint

CITIES = 'C:\\Users\\archa\\Nanodegree\\cities.csv'

def count_digits(area_split):
    #print area_split[0]
    area_split[0] = area_split[0][1:]
    area_split[1] = area_split[1][:-1]
    if len(area_split[0]) > len(area_split[1]):
        area = float(area_split[0])
    else:
        area = float(area_split[1])
        
    return area
    
def fix_area(area):

    
    if area == 'NULL':
        area = None
    else:
            
        area_split =  area.split('|')
        #print area_split
        if len(area_split) > 1:            
            area = count_digits(area_split)                    
        else:
            #print area_split[0] 
            area = float(area_split[0])
    

        
    
    # YOUR CODE HERE

    return area



def process_file(filename):
    # CHANGES TO THIS FUNCTION WILL BE IGNORED WHEN YOU SUBMIT THE EXERCISE
    data = []

    with open(filename, "r") as f:
        reader = csv.DictReader(f)

        #skipping the extra metadata
        for i in range(3):
            l = reader.next()

        # processing file
        for line in reader:
            # calling your function to fix the area value
            if "areaLand" in line:
                line["areaLand"] = fix_area(line["areaLand"])
            data.append(line)

    return data


def test():
    data = process_file(CITIES)

    print "Printing three example results:"
    for n in range(32,35):
        pprint.pprint(data[n]["areaLand"])

    
if __name__ == "__main__":
    test()
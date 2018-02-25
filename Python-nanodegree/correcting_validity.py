# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 14:57:48 2017

@author: archa
"""

import csv
import pprint


INPUT_FILE = 'autos.csv'
OUTPUT_GOOD = 'autos-valid.csv'
OUTPUT_BAD = 'FIXME-autos.csv'

def process_file(input_file, output_good, output_bad):
    
    data_good = []
    data_bad = []

    with open(input_file, "r") as f:
        reader = csv.DictReader(f)
        header = reader.fieldnames
        for record in reader:
            #Validate URI
            if record['URI'].find("dbpedia.org") < 0:
                continue
            
            ps_year = record['productionStartYear'][:4]
            try:#to filter valid items
                ps_year = int(ps_year)
                record['productionStartYear'] = ps_year
                if (ps_year >= 1886) and (ps_year <=2014):
                    data_good.append(record)
                else:
                    data_bad.append(record)
            except ValueError:
                if ps_year =='NULL':
                    data_bad.append(record)
                    
    with open(output_good, "w") as good:
        writer = csv.DictWriter(good, delimiter = ',', fieldnames = header)
        writer.writeheader()
        for row in data_good:
            writer.writerow(row)
            
    with open(output_bad, "w") as bad:
        writer = csv.DictWriter(bad, delimiter = ',', fieldnames = header)
        writer.writeheader()
        for row in data_bad:
            writer.writerow(row)
                
   
if __name__ == "__main__":
    process_file(INPUT_FILE, OUTPUT_GOOD, OUTPUT_BAD)

# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 14:46:47 2017

@author: archa
"""

import xlrd
import csv

datafile = "2013_ERCOT_Hourly_Load_Data.xls"
def parse_file(datafile):
    workbook = xlrd.open_workbook(datafile)
    sheet = workbook.sheet_by_index(0)
    
    excel_data = [[sheet.cell_value(r, col) 
                for col in range(sheet.ncols - 1)] 
                    for r in range(sheet.nrows)]
    data = []
    for col in range(1, len(excel_data[0])):
        column = []
        column.append(excel_data[0][col])
        max_load = max(sheet.col_values(col, start_rowx=1))
        column.append(0)
        column.append(0)
        column.append(0)
        column.append(0)        
        column.append(max_load)
        data.append(column)
        
    print "DATA:",
    print data
        
        
    print "No. of columns:",
    print len(excel_data[0])
    print excel_data[0][1]
    print sheet.cell_type(1, 0)
    exceltime = sheet.cell_value(1, 0)
    print "Time in Excel format:",
    print exceltime
    print "Convert time to a Python datetime tuple, from the Excel float:",
    print xlrd.xldate_as_tuple(exceltime, 0)
    date_time = xlrd.xldate_as_tuple(exceltime, 0)
    print date_time[0]
    print "Maximum value of column 1:"
    col = 1
    print max(sheet.col_values(col, start_rowx=1))
    
    return data

    
def save_file(data, filename):
    with open(filename, 'wb') as csvfile:
        writer = csv.writer(csvfile, delimiter = '|')
        writer.writerow(['Station', 'Year', 'Month', 'Day', 'Hour', 'Max Load'])
        writer.writerow(data[0])
        writer.writerow(data[1])
        
    

data = parse_file(datafile)
save_file(data, '2013_Max_Loads.csv')

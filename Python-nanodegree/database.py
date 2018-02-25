# -*- coding: utf-8 -*-
"""
Created on Tue Dec 05 16:21:00 2017

@author: archa
"""

import sqlite3

# Fetch records from either chinook.db
db = sqlite3.connect("chinook.db")
c = db.cursor()
QUERY = "SELECT * FROM Invoice;"
c.execute(QUERY)
rows = c.fetchall()

'''Uncomment to see your query in python'''
print "Row data:"
print rows

'''Uncomment to print your query by row'''
#print "your output:"
#for row in rows:
#  print "  ", row[0:]

'''Uncomment to see your query as a pandas dataframe.
This is similar to the output you've been seeing throughout this course
You can learn more about pandas dataframes in our Intro to Data Analysis course!'''

import pandas as pd    
df = pd.DataFrame(rows)
print df

db.close()

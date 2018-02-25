# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import unicodecsv

#Reads a csv file and converts it into dictionary using unicode and 
#returns the data as list
def read_csv(filename):
    with open(filename, 'rb') as f:
        reader = unicodecsv.DictReader(f)
        return list(reader)
    
    
enrollments = read_csv('C:\\Users\\archa\\enrollments.csv')
daily_engagement = read_csv('C:\\Users\\archa\\daily_engagement.csv')
project_submissions = read_csv('C:\\Users\\archa\\project_submissions.csv')
'''
For each of the three files,find the total number of rows and the unique number of 
students
'''

#To rename account key column in daily_engagement so that a common function can be written to get unique students in all the three files
for engagement_record in daily_engagement:   
    engagement_record['account_key'] = engagement_record['acct']
    del[engagement_record['acct']]

#Define function to get unique students for all the files
def get_unique_students(data):
    unique_students = set()
    for data_point in data:
        unique_students.add(data_point['account_key'])
    return unique_students

#print ('Enrollments:')
#print len(enrollments)    
unique_enrolled_students = get_unique_students(enrollments)
#print len(unique_enrolled_students)
#print enrollments[0]

#print('Daily:')
#print len(daily_engagement) 
unique_engagement_students = get_unique_students(daily_engagement)
#print len(unique_engagement_students)
#print daily_engagement[0]

#print('Project:')
#print len(project_submissions)
unique_project_submitters = get_unique_students(project_submissions)
#print len(unique_project_submitters)

#Identifying missing unique daily students(1237) from enrollment(1302)
for enrollment in enrollments:
    student = enrollment['account_key']
    if student not in unique_engagement_students:
        #print enrollment     # We could see that the 'days_to_cancel' field was 0 also 'join_date' and 'cancel_date' were same
        #print('--------')
        break

#Investigate if there are more surprising data
num_problem_students = 0
for enrollment in enrollments:
    student = enrollment['account_key']
    if student not in unique_engagement_students \
        and enrollment['days_to_cancel'] != '0' :
            num_problem_students += 1
            #print enrollment
#print num_problem_students


#Check all the Udacity test accounts(is_udacity = True)
udacity_test_accounts = set()
for enrollment in enrollments:
    if enrollment['is_udacity'] == 'True':
        #print enrollment['is_udacity']
        udacity_test_accounts.add(enrollment['account_key'])
        
print len(udacity_test_accounts)


#Remove Udacity test accounts

def remove_udacity_accounts(data):
    non_udacity_data = []
    for data_point in data:
        if data_point['account_key'] not in udacity_test_accounts:
            non_udacity_data.append(data_point)
    return non_udacity_data


non_udacity_enrollments = remove_udacity_accounts(enrollments)
non_udacity_engagement = remove_udacity_accounts(daily_engagement)
non_udacity_submissions = remove_udacity_accounts(project_submissions)

#print len(non_udacity_enrollments)
#print len(non_udacity_engagement)
#print len(non_udacity_submissions)   
#print non_udacity_enrollments[0]     


#Refining the question -- Data analysis process
paid_students = {}
for enrollment in non_udacity_enrollments:
    if enrollment['is_canceled'] == 'False' or enrollment['days_to_cancel'] > 7 :    
        print (enrollment['days_to_cancel'])   
        paid_students[enrollment['account_key']] = enrollment['join_date']

    
print len(paid_students)


            
        

    





    
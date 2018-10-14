#!/usr/bin/python

import sys
import pickle
sys.path.append("../tools/")

import matplotlib.pyplot as plt
from feature_format import featureFormat, targetFeatureSplit
from tester import dump_classifier_and_data

### Task 1: Select what features you'll use.
### features_list is a list of strings, each of which is a feature name.
### The first feature must be "poi".
features_list = ['poi','salary', 'fraction_from_poi','fraction_to_poi' ] # You will need to use more features

### Load the dictionary containing the dataset
with open("final_project_dataset.pkl", "r") as data_file:
    data_dict = pickle.load(data_file)


print (data_dict.values()[0])
### Task 2: Remove outliers

features = ["salary", "bonus"]
#Remove outlier 'TOTAL'
data_dict.pop('TOTAL',0)
data = featureFormat(data_dict, features)

#Plot features
for point in data:
    salary = point[0]
    bonus = point[1]
    plt.scatter( salary, bonus, color = 'b' )

plt.xlabel("salary")
plt.ylabel("bonus")
plt.show()
### Task 3: Create new feature(s)
## New features: fraction_to_poi_email,fraction_from_poi_email

def computeFraction( poi_messages, all_messages ):
    """ given a number messages to/from POI (numerator) 
        and number of all messages to/from a person (denominator),
        return the fraction of messages to/from that person
        that are from/to a POI
   """
    ### beware of "NaN" when there is no known email address (and so
    ### no filled email features), and integer division!
    ### in case of poi_messages or all_messages having "NaN" value, return 0.
    if poi_messages == "NaN" or all_messages == "NaN" or poi_messages == 0 or all_messages == 0:
        return 0
    else:
        return (float(poi_messages)/float(all_messages))

for name in data_dict:
    from_poi_to_this_person = data_dict[name]["from_poi_to_this_person"]
    to_messages = data_dict[name]["to_messages"]
    from_this_person_to_poi = data_dict[name]["from_this_person_to_poi"]
    from_messages = data_dict[name]["from_messages"]
    
    fraction_from_poi = computeFraction( from_poi_to_this_person, to_messages )
    fraction_to_poi = computeFraction( from_this_person_to_poi, from_messages )
    
    data_dict[name]["fraction_from_poi"] = fraction_from_poi
    data_dict[name]["fraction_to_poi"] = fraction_to_poi
    

### Store to my_dataset for easy export below.
my_dataset = data_dict

data = featureFormat(my_dataset, features_list)
print features_list

### plot new features
for point in data:
    from_poi = point[2]
    to_poi = point[3]
    non_poi = plt.scatter(from_poi, to_poi, color = 'b', label='non-poi' )
    if point[0] == 1:
        poi = plt.scatter(from_poi, to_poi, color="r", label='poi')
plt.xlabel("No. of emails from POI's to this person")
plt.ylabel("No. of emails from this person to POI's")
plt.legend((non_poi, poi),
           ('Non-POI', 'POI'),
           scatterpoints=1,
           #ncol=3,
           fontsize=8)
plt.show()

### Extract features and labels from dataset for local testing
data = featureFormat(my_dataset, features_list, sort_keys = True)
labels, features = targetFeatureSplit(data)

### Task 4: Try a varity of classifiers
### Please name your classifier clf for easy export below.
### Note that if you want to do PCA or other multi-stage operations,
### you'll need to use Pipelines. For more info:
### http://scikit-learn.org/stable/modules/pipeline.html

# Provided to give you a starting point. Try a variety of classifiers.
from sklearn.naive_bayes import GaussianNB
clf = GaussianNB()

### Task 5: Tune your classifier to achieve better than .3 precision and recall 
### using our testing script. Check the tester.py script in the final project
### folder for details on the evaluation method, especially the test_classifier
### function. Because of the small size of the dataset, the script uses
### stratified shuffle split cross validation. For more info: 
### http://scikit-learn.org/stable/modules/generated/sklearn.cross_validation.StratifiedShuffleSplit.html

# Example starting point. Try investigating other evaluation techniques!
from sklearn.cross_validation import train_test_split
features_train, features_test, labels_train, labels_test = \
    train_test_split(features, labels, test_size=0.3, random_state=42)

### Task 6: Dump your classifier, dataset, and features_list so anyone can
### check your results. You do not need to change anything below, but make sure
### that the version of poi_id.py that you submit can be run on its own and
### generates the necessary .pkl files for validating your results.

dump_classifier_and_data(clf, my_dataset, features_list)
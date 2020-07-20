#!/usr/bin/python

"""
    This is the code to accompany the Lesson 3 (decision tree) mini-project.

    Use a Decision Tree to identify emails from the Enron corpus by author:
    Sara has label 0
    Chris has label 1
"""


from time import time
from email_preprocess import preprocess
from sklearn.tree import DecisionTreeClassifier

### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()

print(len(features_train[0]))


#########################################################
### your code goes here ###
clf = DecisionTreeClassifier(min_samples_split=40)
clf = clf.fit(features_train, labels_train)
e = clf.score(features_test, labels_test)
print(e)
#########################################################



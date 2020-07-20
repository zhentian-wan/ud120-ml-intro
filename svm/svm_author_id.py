#!/usr/bin/python

"""
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:
    Sara has label 0
    Chris has label 1
"""

import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess

print "start processing..."

### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()
features_train = features_train[:len(features_train)]
labels_train = labels_train[:len(labels_train)]
print "done processing..."


#########################################################
### your code goes here ###
from sklearn.svm import SVC
clf = SVC(gamma='auto', kernel="rbf", C=10000.0)
print "start training..."
clf.fit(features_train, labels_train)
print "done training..."
print "start scoreing..."
accuracy = clf.score(features_test, labels_test)
predictions = clf.predict(features_test)
print "done scoreing..."
print(accuracy)
print(sum(predictions))
#########################################################

## 1% data
##kernal="linear" accuracy=0.88
##kernal="rbf" accuracy=0.61
##kernal="rbf" C=10.0 accuracy=0.61
##kernal="rbf" C=100.0 accuracy=0.61
##kernal="rbf" C=1000.0 accuracy=0.82
##kernal="rbf" C=10000.0 accuracy=0.89

## 35% data
##kernal="rbf" C=10000.0 accuracy=0.96

## 50% data
##kernal="rbf" C=10000.0 accuracy=0.987

## 100% data
##kernal="rbf" C=10000.0 accuracy>0.99



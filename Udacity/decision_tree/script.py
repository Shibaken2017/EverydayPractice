#!/usr/bin/python

""" lecture and example code for decision tree unit """

from sklearn import datasets
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import LeaveOneOut
from sklearn.metrics import accuracy_score

def classify(features_train, labels_train):
 ### your code goes here--should return a trained decision tree classifer


 clf = DecisionTreeClassifier()
 clf.fit(features_train, labels_train)


 return clf
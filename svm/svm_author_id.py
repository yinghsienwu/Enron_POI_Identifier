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


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()

print "number of features:\t",len(features_train[0])

#########################################################
### your code goes here ###
from sklearn.svm import SVC
clf=SVC(kernel='rbf',C=10000)

features_train=features_train[:len(features_train)/100] 
labels_train=labels_train[:len(labels_train)/100]
#These lines effectively slice the training dataset down to 1% of its original size, tossing out 99% of the training data.

t0=time()
clf.fit(features_train,labels_train)  #much slower than naive_bayes
print "fitting time:\t",round(time()-t0),"s"

t1=time()
pred=clf.predict(features_test)
print "prediction time:\t",round(time()-t1),"s"

import sklearn
accuracy=sklearn.metrics.accuracy_score(pred,labels_test)
print accuracy
print pred[10],pred[26],pred[50]

import numpy as np
print np.count_nonzero(pred)

#########################################################



#!/usr/bin/python


"""
    Starter code for the evaluation mini-project.
    Start by copying your trained/tested POI identifier from
    that which you built in the validation mini-project.

    This is the second step toward building your POI identifier!

    Start by loading/formatting the data...
"""

import pickle
import sys
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit

data_dict = pickle.load(open("../final_project/final_project_dataset.pkl", "r") )

### add more features to features_list!
features_list = ["poi", "salary"]

data = featureFormat(data_dict, features_list)
labels, features = targetFeatureSplit(data)



### your code goes here 
from sklearn import cross_validation
features_train,features_test,labels_train,labels_test=cross_validation.train_test_split(features,labels,test_size=0.3,random_state=42)

from sklearn import tree
clf=tree.DecisionTreeClassifier()
clf.fit(features_train,labels_train)
pred=clf.predict(features_test)
pred2=[0.0]*len(labels_test)
import sklearn
accuracy=sklearn.metrics.accuracy_score(pred,labels_test)
print "accuracy:\t",accuracy

recall=sklearn.metrics.recall_score(labels_test,pred)
precision=sklearn.metrics.precision_score(labels_test,pred)
print "recall:\t",recall
print "precision:\t",precision

poi_test=0
for num in labels_test:
    if num==1.0:
        poi_test+=1

poi_pred=0
for num in pred:
    if num==1.0:
        poi_pred+=1

#print "How many POIs are predicted for the test set? \t"
#print "# of POIs in labels_test: \t",poi_test
#print "# of POIs in prediction: \t",poi_pred

#print "How many people in total are in the test set?\t",len(labels_test)

#print "labels_test:\t",labels_test
#print "pred:\t",pred

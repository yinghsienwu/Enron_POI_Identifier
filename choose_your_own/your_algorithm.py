#!/usr/bin/python

import matplotlib.pyplot as plt
from prep_terrain_data import makeTerrainData
from class_vis import prettyPicture

features_train, labels_train, features_test, labels_test = makeTerrainData()


### the training data (features_train, labels_train) have both "fast" and "slow"
### points mixed together--separate them so we can give them different colors
### in the scatterplot and identify them visually
grade_fast = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]==0]
bumpy_fast = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]==0]
grade_slow = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]==1]
bumpy_slow = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]==1]


#### initial visualization
plt.xlim(0.0, 1.0)
plt.ylim(0.0, 1.0)
plt.scatter(bumpy_fast, grade_fast, color = "b", label="fast")
plt.scatter(grade_slow, bumpy_slow, color = "r", label="slow")
plt.legend()
plt.xlabel("bumpiness")
plt.ylabel("grade")
plt.show()
################################################################################


### your code here!  name your classifier object clf if you want the 
### visualization code (prettyPicture) to show you the decision boundary

#K nearest neighbors
from sklearn import svm
#clf=sklearn.neighbors.KNeighborsClassifier()
#clf=naive_bayes.GaussianNB()
clf=svm.SVC(kernel='rbf',C=1000)
#clf=tree.DecisionTreeClassifier()
#clf=ensemble.AdaBoostClassifier()
#clf=ensemble.RandomForestClassifier(n_estimators=8,min_samples_split=1)
clf.fit(features_train,labels_train)
pred=clf.predict(features_test)

from sklearn import metrics
accuracy=metrics.accuracy_score(pred,labels_test)
print "Accuracy:\t",accuracy


try:
    prettyPicture(clf, features_test, labels_test)
except NameError:
    pass

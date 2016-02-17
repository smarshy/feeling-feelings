
from __future__ import print_function
from sklearn import svm
import arff
import numpy
import pprint
import os

from sklearn import datasets
from sklearn.cross_validation import train_test_split
from sklearn.grid_search import GridSearchCV
from sklearn.metrics import classification_report
from sklearn.svm import SVC

rootdir = os.getcwd() + '/'


with open(rootdir + 'myfeatures_988_train.arff') as f:
	data = f.read()

d = arff.loads(data)
main_data_list = d['data']

mdata = []
labels = []

for lists in main_data_list:
	mdata.append(lists[1:-1])
	labels.append(lists[-1])


# To apply an classifier on this data, we need to flatten the image, to
# turn the data in a (samples, feature) matrix:
n_samples = len(labels)
X = mdata
y = labels

# Split the dataset in two equal parts
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=45)

# Set the parameters by cross-validation
tuned_parameters = [{'kernel': ['rbf'], 'gamma': [1e-3, 1e-4],
                     'C': [1, 10, 100, 1000]},
                    {'kernel': ['linear'], 'C': [1, 10, 100, 1000]}]

scores = ['precision', 'recall']

for score in scores:
    print("# Tuning hyper-parameters for %s" % score)
    print()

    clf = GridSearchCV(SVC(C=1), tuned_parameters, cv=5, scoring=score)
    clf.fit(X_train, y_train)

    print("Best parameters set found on development set:")
    print()
    print(clf.best_estimator_)
    print()
    print("Grid scores on development set:")
    print()
    for params, mean_score, scores in clf.grid_scores_:
        print("%0.3f (+/-%0.03f) for %r"
              % (mean_score, scores.std() / 2, params))
    print()

    print("Detailed classification report:")
    print()
    print("The model is trained on the full development set.")
    print("The scores are computed on the full evaluation set.")
    print()
    y_true, y_pred = y_test, clf.predict(X_test)
    print(classification_report(y_true, y_pred))
    print()

# Note the problem is too easy: the hyperparameter plateau is too flat and the
# output model is the same for precision and recall with ties in quality.

with open(rootdir + 'myfeatures_988_test.arff') as f:
    data = f.read()

d = arff.loads(data)
test_data_list = d['data']

mdatat = []
labelst = []

for lists in test_data_list:
    mdatat.append(lists[1:-1])
    labelst.append(lists[-1])

print(clf.predict(mdatat))
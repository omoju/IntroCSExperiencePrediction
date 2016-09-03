
import time
from sklearn import cross_validation
from sklearn.metrics import f1_score
from sklearn.metrics import confusion_matrix

import matplotlib.pyplot as plt
import matplotlib.cm as cm
import pandas as pd
import numpy as np
from sklearn.decomposition import pca


def shuffle_split_data(X, y, num_train):
    """ Shuffles and splits data into 75% training and 25% testing subsets,
        then returns the training and testing subsets. """

    ### test_size is the percentage of events assigned to the test set
    ### (remainder go into training)
    
    X_train, X_test, y_train, y_test = cross_validation.train_test_split(X, y, 
                                                                        train_size=num_train, random_state=42) # 
    

    # Return the training and testing data subsets
    return X_train, y_train, X_test, y_test


# Train a model
def train_classifier(clf, X_train, y_train):
    start = time.time()
    clf.fit(X_train, y_train)
    end = time.time()
    return end - start

# Predict on training set and compute F1 score

def predict_labels(clf, features, target):
    start = time.time()
    y_pred = clf.predict(features)
    end = time.time()
    return f1_score(target.values, y_pred), end - start 

# Train and predict using different training set sizes
def train_predict(clf, X_train, y_train, X_test, y_test):
    
    train_time = train_classifier(clf, X_train, y_train)
    
    F1_score_train, prediction_time_train = predict_labels(clf, X_train, y_train)
    F1_score_test, prediction_time_test = predict_labels(clf, X_test, y_test)
    
    return train_time, F1_score_train, F1_score_test, prediction_time_test



## Confusion Matrix
## Predicted Class by Actual Class


def makeConfusionMatrix(clf, X_test, y_test):
    """Print confusion matrix.

    Keyword arguments:
    clf -- classifier (scikit learn classifier model)
    X_test -- array of features (float)
    y_test -- array of labels (float)
    
    """
    
    y_true = y_test
    y_pred = clf.predict(X_test)

    cM = confusion_matrix(y_true, y_pred)

    print "{:^40}".format(clf.__class__.__name__)
    print "{:>40}".format('Actual Gender')
    print "{:15}{:10}{:10}{:10}".format('Predicted', '', 'Female', 'Male')
    print "{:15}{:10}{:<10.3f}{:<10.3f}".format('', 'Female', cM[0][0], cM[0][1])
    print "{:15}{:10}{:<10.3f}{:<10.3f}".format('', 'Male', cM[1][0], cM[1][1])

    
def pca_results(good_data, pca):
	'''
	Create a DataFrame of the PCA results
	Includes dimension feature weights and explained variance
	Visualizes the PCA results
	'''

	# Dimension indexing
	dimensions = dimensions = ['Dimension {}'.format(i) for i in range(1,len(pca.components_)+1)]

	# PCA components
	components = pd.DataFrame(np.round(pca.components_, 4), columns = good_data.keys())
	components.index = dimensions

	# PCA explained variance
	ratios = pca.explained_variance_ratio_.reshape(len(pca.components_), 1)
	variance_ratios = pd.DataFrame(np.round(ratios, 4), columns = ['Explained Variance'])
	variance_ratios.index = dimensions

	# Create a bar plot visualization
	#fig, ax = plt.subplots(figsize = (14,8))

	# Plot the feature weights as a function of the components
	#components.plot(ax = ax, kind = 'bar');
	#ax.set_ylabel("Feature Weights")
	#ax.set_xticklabels(dimensions, rotation=0)


	# Display the explained variance ratios
	#for i, ev in enumerate(pca.explained_variance_ratio_):
		#ax.text(i-0.40, ax.get_ylim()[1] + 0.05, "Explained Variance\n          %.4f"%(ev))

	# Return a concatenated DataFrame
	return pd.concat([variance_ratios, components], axis = 1)

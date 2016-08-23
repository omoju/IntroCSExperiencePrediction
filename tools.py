
import time
from sklearn import cross_validation
from sklearn.metrics import f1_score
from sklearn.metrics import confusion_matrix


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


def print_Output_Table(clf, train_time, prediction_time, F1_score_train, F1_score_test, prntLatex):
    """Print output table for classifier scores.

    Keyword arguments:
    clf -- classifier (scikit learn classifier model)
    train_time -- array (float)
    prediction_time -- array (float)
    F1_score_train -- array (float)
    F1_score_test -- array (float)
    prntLatex -- 1 for print optimized for latex, 0 for regular printing
    
    """
    
    print "{:>53}".format(clf.__class__.__name__)
    print "{:>53}".format('Training set size')
    print "{:>30}{:>d}\t{:>d}\t{:>d}".format('',200,400,600)
    print "-"*55

    if prntLatex:
        for i in range(1):
            print "{:30}{:3}{:.3f}{:3}{:.3f}{:3}{:.3f}{:3}".format('Training time (secs)','&',
                                           train_time[i], '&',train_time[i+1], '&',train_time[i+2], '\\\\')
            print "{:30}{:3}{:.3f}{:3}{:.3f}{:3}{:.3f}{:3}".format('Prediction time (secs)','&',
                                        prediction_time[i], '&',prediction_time[i+1], '&',prediction_time[i+2], '\\\\')
            print "{:30}{:3}{:.3f}{:3}{:.3f}{:3}{:.3f}{:3}".format('F1 score for training set','&',
                                          F1_score_train[i], '&',F1_score_train[i+1],'&',F1_score_train[i+2], '\\\\')
            print "{:30}{:3}{:.3f}{:3}{:.3f}{:3}{:.3f}{:3}".format('F1 score for test set','&',
                                          F1_score_test[i],'&',F1_score_test[i+1],'&',F1_score_test[i+2], '\\\\')
    else:
        for i in range(1):
            print "{:30}{:.3f}\t{:.3f}\t{:.3f}".format('Training time (secs)',
                                           train_time[i], train_time[i+1], train_time[i+2])
            print "{:30}{:.3f}\t{:.3f}\t{:.3f}".format('Prediction time (secs)',
                                           prediction_time[i], prediction_time[i+1], prediction_time[i+2])
            print "{:30}{:.3f}\t{:.3f}\t{:.3f}".format('F1 score for training set',
                                          F1_score_train[i], F1_score_train[i+1],F1_score_train[i+2])
            print "{:30}{:.3f}\t{:.3f}\t{:.3f}".format('F1 score for test set',
                                          F1_score_test[i],F1_score_test[i+1],F1_score_test[i+2])
            

def makeTable(clf, X_train, y_train, X_test, y_test, prntLatex):
    """Print output table for classifier scores by creating scores based on incrementally growing the feature space.

    Keyword arguments:
    clf -- classifier (scikit learn classifier model)
    X_test -- array of features (float)
    y_test -- array of labels (float)
    prntLatex -- 1 for print optimized for latex, 0 for regular printing
    
    """
    train_set_size = [0] * 3
    train_time = [0] * 3
    prediction_time = [0] * 3
    F1_score_train = [0] * 3
    F1_score_test = [0] * 3

    for i in xrange(100, 600, 200):
        (train_time[(i//200)-1], F1_score_train[(i//200)-1], 
         F1_score_test[(i/200)-1], prediction_time[(i//200)-1]) = train_predict(clf, 
                                                              X_train[:i], y_train[:i], X_test, y_test)
        train_set_size[(i//200)-1] = i


    print_Output_Table(clf, train_time, prediction_time, F1_score_train, F1_score_test, prntLatex)
    
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

import numpy
import scipy.stats
import pandas

def compare_averages(filename):
    """
    Performs a t-test on two sets of baseball data (left-handed and right-handed hitters).

    You will be given a csv file that has three columns.  A player's
    name, handedness (L for lefthanded or R for righthanded) and their
    career batting average (called 'avg'). You can look at the csv
    file by downloading the baseball_stats file from Downloadables below. 
    
    Write a function that will read that the csv file into a pandas data frame,
    and run Welch's t-test on the two cohorts defined by handedness.
    
    One cohort should be a data frame of right-handed batters. And the other
    cohort should be a data frame of left-handed batters.
    
    We have included the scipy.stats library to help you write
    or implement Welch's t-test:
    http://docs.scipy.org/doc/scipy/reference/stats.html
    
    With a significance level of 95%, if there is no difference
    between the two cohorts, return a tuple consisting of
    True, and then the tuple returned by scipy.stats.ttest.  
    
    If there is a difference, return a tuple consisting of
    False, and then the tuple returned by scipy.stats.ttest.
    
    For example, the tuple that you return may look like:
    (True, (9.93570222, 0.000023))
    """
    # READ FILE INTO PANDAS
    df = pandas.read_csv(filename)
    
    # SPLIT BY HANDEDNESS
    dfl = df[df.handedness=='L']
    dfr = df[df.handedness=='R']
    
    # RUN THE T TEST (equal_var = FALSE is welch's ttest)
    t = scipy.stats.ttest_ind(dfl['avg'],dfr['avg'], equal_var =False)
    
    # CONFIDENCE INTERVAL OF (100-5) = 95
    a = (False,t) if t[1] <= 0.05 else (True,t)
    
    # RETURN T TEST RESULTS PRECEDED WITH A TRUE OR FALSE
    print a
    return a

#  gradient descent -- Not really sure about this yet
import numpy
import pandas

def compute_cost(features, values, theta):
    """
    Compute the cost of a list of parameters, theta, given a list of features 
    (input data points) and values (output data points).
    """
    m = len(values)
    sum_of_square_errors = numpy.square(numpy.dot(features, theta) - values).sum()
    cost = sum_of_square_errors / (2*m)

    return cost

def gradient_descent(features, values, theta, alpha, num_iterations):
    """
    Perform gradient descent given a data set with an arbitrary number of features.
    """

    # Write code here that performs num_iterations updates to the elements of theta.
    # times. Every time you compute the cost for a given list of thetas, append it 
    # to cost_history.
    # See the Instructor notes for hints. 
    m = len(values)
    cost_history = []
    for i in range (num_iterations):
        predicted_values= numpy.dot(features,theta)
        theta = theta - alpha / m * numpy.dot((predicted_values-values),features)
        cost = compute_cost(features,values,theta)
        cost_history.append(cost)

    ###########################
    ### YOUR CODE GOES HERE ###
    ###########################

    return theta, pandas.Series(cost_history) # leave this line for the grader

# R squared stuff -- still not really sure about this something to do with testing our model

import numpy as np

def compute_r_squared(data, predictions):
    # Write a function that, given two input numpy arrays, 'data', and 'predictions,'
    # returns the coefficient of determination, R^2, for the model that produced 
    # predictions.
    # 
    # Numpy has a couple of functions -- np.mean() and np.sum() --
    # that you might find useful, but you don't have to use them.

    SST = (( data - np.mean(data))**2).sum()
    SSReg = (( predictions - data)**2).sum()
    r_squared = 1-SSReg /SST

    return r_squared



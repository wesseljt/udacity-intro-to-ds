# Quiz 4
import json
import requests

def api_get_request(url):
    # In this exercise, you want to call the last.fm API to get a list of the
    # top artists in Spain. <- Spain is set in the URL
    #
    # Once you've done this, return the name of the number 1 top artist in Spain.
    data = requests.get(url).text
    data = json.loads(data)
    return data['topartists']['artist'][0]['name'] # return the top artist in Spain

# Quiz 5 
from pandas import *
import numpy

def imputation(filename):
    # Pandas dataframes have a method called 'fillna(value)', such that you can
    # pass in a single value to replace any NAs in a dataframe or series. You
    # can call it like this: 
    #     dataframe['column'] = dataframe['column'].fillna(value)
    #
    # Using the numpy.mean function, which calculates the mean of a numpy
    # array, impute any missing values in our Lahman baseball
    # data sets 'weight' column by setting them equal to the average weight.
    # 
    # You can access the 'weight' colum in the baseball data frame by
    # calling baseball['weight']

    baseball = pandas.read_csv(filename)
    
    baseball['weight'] = baseball['weight'].fillna(numpy.mean(baseball['weight']))

    return baseball
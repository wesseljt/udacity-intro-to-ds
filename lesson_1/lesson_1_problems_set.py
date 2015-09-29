import numpy
import pandas
import statsmodels.api as sm

'''
def simple_heuristic(file_path):

    Here's a simple heuristic to start off:
       1) If the passenger is female, your heuristic should assume that the
       passenger survived.
       2) If the passenger is male, you heuristic should
       assume that the passenger did not survive.

    predictions = {}
    df = pandas.read_csv(file_path)
    for passenger_index, passenger in df.iterrows():
        passenger_id = passenger['PassengerId']
        if passenger['Sex'] == 'male':
            predictions[passenger_id] = 1
        else:
            predictions[passenger_id] = 0
    return predictions
'''

'''
def simple_heuristic(file_path):

    predictions = {}
    df = pandas.read_csv(file_path)
    for passenger_index, passenger in df.iterrows():
        passenger_id = passenger['PassengerId']
        if passenger['Sex'] == 'female' or (passenger['Age'] < 18 and passenger['Pclass'] == 1):
            predictions[passenger_id] = 1  # lived
        else:
            predictions[passenger_id] = 0  # died
    return predictions

simple_heuristic('titanic_data.csv')

'''

def simple_heuristic(file_path):

    predictions = {}
    df = pandas.read_csv(file_path)
    for passenger_index, passenger in df.iterrows():
        passenger_id = passenger['PassengerId']
        if (passenger['Sex'] == 'female' and passenger['SibSp'] <3) or (passenger['Age'] < 18 and passenger['Pclass'] == 1):
            predictions[passenger_id] = 1 #lived
        else:
            predictions[passenger_id] = 0 # died
    return predictions

simple_heuristic('titanic_data.csv')
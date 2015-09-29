# Quiz #1

import pandas


def add_full_name(path_to_csv, path_to_new_csv):

    # Assume you will be reading in a csv file with the same columns that the
    # Lahman baseball data set has -- most importantly, there are columns
    # called 'nameFirst' and 'nameLast'.
    # 1) Write a function that reads a csv
    # located at "path_to_csv" into a pandas dataframe and adds a new column
    # called 'nameFull' with a player's full name.
    #
    # For example:
    # for Hank Aaron, nameFull would be 'Hank Aaron',

    dataframe = pandas.read_csv(path_to_csv)
    dataframe['nameFull'] = dataframe.nameFirst + " " + dataframe.nameLast
    dataframe.to_csv(path_to_new_csv)

if __name__ == "__main__":
    # For local use only
    # If you are running this on your own machine add the path to the
    # Lahman baseball csv and a path for the new csv.
    # The dataset can be downloaded from this website: http://www.seanlahman.com/baseball-archive/statistics
    # We are using the file Master.csv
    path_to_csv = "/Users/jwessel/udacity-intro-to-ds/lesson_2/lahman-csv_2015-01-24/Master.csv"
    path_to_new_csv = "/Users/jwessel/udacity-intro-to-ds/lesson_2/lahman-csv_2015-01-24/fullname.csv"
    add_full_name(path_to_csv, path_to_new_csv)


# Quiz #2
# WRITE A SIMPLE QUERY <-- skipping this b/c I am very familiar with relational databases

# Quiz #3
import pandas
import pandasql

def aggregate_query(filename):
    # Read in our aadhaar_data csv to a pandas dataframe.  Afterwards, we rename the columns
    # by replacing spaces with underscores and setting all characters to lowercase, so the
    # column names more closely resemble columns names one might find in a table.
    
    aadhaar_data = pandas.read_csv(filename)
    aadhaar_data.rename(columns = lambda x: x.replace(' ', '_').lower(), inplace=True)

    # Write a query that will select from the aadhaar_data table how many men and how 
    # many women over the age of 50 have had aadhaar generated for them in each district.
    # aadhaar_generated is a column in the Aadhaar Data that denotes the number who have had
    # aadhaar generated in each row of the table.
    #
    # Note that in this quiz, the SQL query keywords are case sensitive. 
    # For example, if you want to do a sum make sure you type 'sum' rather than 'SUM'.
    #

    # The possible columns to select from aadhaar data are:
    #     1) registrar
    #     2) enrolment_agency
    #     3) state
    #     4) district
    #     5) sub_district
    #     6) pin_code
    #     7) gender
    #     8) age
    #     9) aadhaar_generated
    #     10) enrolment_rejected
    #     11) residents_providing_email,
    #     12) residents_providing_mobile_number
    #
    # You can download a copy of the aadhaar data that we are passing 
    # into this exercise below:
    # https://www.dropbox.com/s/vn8t4uulbsfmalo/aadhaar_data.csv
        
    q = """select gender,district,sum(aadhaar_generated) from aadhaar_data where age > 50
        group by gender,district; """

    # Execute your SQL command against the pandas frame
    aadhaar_solution = pandasql.sqldf(q.lower(), locals())
    return aadhaar_solution    


# Author: Danny Lillard
# Date: 9/27/2021
# Desc: Transforms data for the COVID-19 analysis.

import pandas as pd

#------------------General for files---------------------------------
#just to check if the file is empty, we use a falsy here.
def checkEmpty(ourData):
    if not ourData:
        return True
    return False

#Lets change the csv to a df for easy cleaning
def csvTodf(filename, wantedCols):
    df = pd.read_csv(filename,usecols=wantedCols)
    return df

#------------------Vaccines------------------------------------------
def cleanVaccine(df):
    df = df.dropna()
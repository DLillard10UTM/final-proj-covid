# Author: Danny Lillard
# Date: 9/27/2021
# Desc: Extract of the ETL process, simplest part.

import requests
import pandas as pd
import io

#Grabs the data from an online, public csv, returns the data.
#url: the api point we are grabbing from
#wantedCols: only the columns we want.
def csvTodf(url, wantedCols):
    #lets grab as many as possible
    url = url + '?$limit=50000'
    df = pd.read_csv(url, usecols=wantedCols)
    #we now need to start appending.
    appendNum = 1
    url1 = url + '&$offset=' + str(appendNum*50000)
    df1 = pd.read_csv(url1, usecols=wantedCols)
    print(len(df1))
    while(not df1.empty):
        df = df.append(df1,ignore_index=True)
        appendNum += 1
        url1 = url + '&$offset=' + str(appendNum*50000)
        df1 = pd.read_csv(url1, usecols=wantedCols)
    return df

def grabCaseData(ourURL):
    response = requests.get(ourURL)

    file_object = io.StringIO(response.content.decode('utf-8'))
    df = pd.read_csv(file_object)
    return df
# Author: Danny Lillard
# Date: 9/27/2021
# Desc: Extract of the ETL process, simplest part.

import requests
import pandas as pd
import io
#Grabs the data from an online, public csv, returns the data.
#url: the api point we are grabbing from
#wantedCols: only the columns we want.

def grabCaseData(ourURL):
    response = requests.get(ourURL)

    file_object = io.StringIO(response.content.decode('utf-8'))
    df = pd.read_csv(file_object)
    return df
# Author: Danny Lillard
# Date: 9/27/2021
# Desc: Extract of the ETL process, simplest part.

import requests

#Grabs the data from an online, public csv, returns the data.
#url: the api point we are grabbing from
#wantedCols: only the columns we want.
def grabData(url,wantedCols):
    r = requests.get(url, usecols=wantedCols, stream=True)
    return r.text
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

def joinFIPS(df):
    #drops all rows that are not a state.
    df = df[(df['FIPS_State'] < 60)]
    #combining the fips.
    df['FIPS_State'] = df['FIPS_State'].apply(lambda x: '{0:0>2}'.format(x))
    df['FIPS_County'] = df['FIPS_County'].apply(lambda x: '{0:0>3}'.format(x))
    df['FIPS'] = df['FIPS_State'] + df['FIPS_County']
    df = df.drop(['FIPS_State', 'FIPS_County'], axis=1)
    return df

#------------------Vaccines------------------------------------------
def cleanVaccine(df):
    df = df.dropna()
    df = df[(df['FIPS'] != 'UNK')]
    return df

#------------------Vaccines hesitancy--------------------------------
def cleanVaccineHes(df):
    df['FIPS Code'] = df['FIPS Code'].apply(lambda x: '{0:0>5}'.format(x))
    #removing the percent from the columns
    toClean = ['Series_Comp_Pop_Pct', 'Series_Complete_12PlusPop_Pct', 
              'Series_Complete_18PlusPop_Pct', 'Series_Complete_65PlusPop_Pct', 'Administered_Dose1_Pop_Pct',
              'Administered_Dose1_Recip_12PlusPop_Pct', 'Administered_Dose1_Recip_18PlusPop_Pct',
              'Administered_Dose1_Recip_65PlusPop_Pct']
    df[toClean] = (df[toClean].str.strip('%').astype(int))
    return df

#-------------------------deaths-------------------------------------
def cleanDeaths(df):
    df['FIPS Code'] = df['FIPS Code'].apply(lambda x: '{0:0>5}'.format(x))
    df = df.dropna()
    return df

#-------------------------mask mandate by county---------------------
def cleanMaskMandate(df):
    df = joinFIPS(df)
    df = df.dropna()
    return df

#-------------------------bars---------------------------------------
def cleanBars(df):
    df = joinFIPS(df)
    #copying codes, descs, and unit into own table.
    df1 = df[['order_code', 'Action']]
    df1 = df1.drop_duplicates()
    #TODO: Write function to save df1
    df.dropna()
    return df

#-------------------------rests--------------------------------------
def cleanRests(df):
    df = joinFIPS(df)
    #copying codes, descs, and unit into own table.
    df1 = df[['order_code', 'Action']]
    df1 = df1.drop_duplicates()
    #TODO: Write function to save df1
    df.dropna()
    return df

#-------------------------stay at home-------------------------------
def cleanStayAtHome(df):
    df = joinFIPS(df)
    #copying codes, descs, and unit into own table.
    df1 = df[['order_code', 'Stay_At_Home_Order_Recommendation']]
    df1 = df1.drop_duplicates()
    #TODO: Write function to save df1
    df.dropna()
    return df
# Author: Danny Lillard
# Date: 9/27/2021
# Desc: Transforms data for the COVID-19 analysis.

import pandas as pd
import numpy as np
import load

#------------------General for files---------------------------------

def dfToCsv(df,fileName):
    df.to_csv(fileName)

def getCols(url):
    df = pd.read_csv(url)
    for col in df.columns:
        print(col)

#we need state and county variables because not all CSV's are the same.
def joinFIPS(df, stateTitle, countyTitle):
    #drops all rows that are not a state.
    df = df[(df[stateTitle] < 60)]
    #combining the fips.
    df[stateTitle] = df[stateTitle].apply(lambda x: '{0:0>2}'.format(x))
    df[countyTitle] = df[countyTitle].apply(lambda x: '{0:0>3}'.format(x))
    df['fips'] = df[stateTitle] + df[countyTitle]
    df = df.drop([stateTitle, countyTitle], axis=1)
    return df

#------------------------cases---------------------------------------
#for this one we must switch from wide to long format.
def cleanCases(df):
    #dropping where fips is 0
    df = df[(df['countyFIPS'] != 0)]
    df = df.drop(['County Name', 'State', 'StateFIPS'], axis=1)
    #we only set the id as no val_vars means all but the id.
    df = pd.melt(df, id_vars=['countyFIPS'])
    #naming the cols right
    df = df.rename(columns = {'countyFIPS':'fips', 'variable':'date', 'value':'cases'})
    return df
#------------------Vaccines------------------------------------------
def cleanVaccine(df):
    df = df.dropna()
    df['date'] = df['date'].str.slice(start=0, stop=10)
    df = df[(df['fips'] != 'UNK')]
    df['fips'] = df['fips'].astype(int)
    df = df[(df['fips'] <= 56045)]
    df = df.dropna()
    return df

#------------------Vaccines hesitancy--------------------------------
def cleanVaccineHes(df):
    df['fips_code'] = df['fips_code'].apply(lambda x: '{0:0>5}'.format(x))

    df = df.rename(columns = {'fips_code':'fips', 'estimated_hesitant':'est_hestitant', 
                              'estimated_hesitant_or_unsure':'est_hesitant_or_unsure', 
                              'estimated_strongly_hesitant':'est_strongly_hesitant',
                              'ability_to_handle_a_covid':'cvac_concern',
                            })
    df = df.dropna()
    return df

#-------------------------deaths-------------------------------------
def cleanDeaths(df):
    #dropping where fips is 0
    df = df[(df['countyFIPS'] != 0)]
    df = df.drop(['County Name', 'State', 'StateFIPS'], axis=1)
    #we only set the id as no val_vars means all but the id.
    df = pd.melt(df, id_vars=['countyFIPS'])
    #naming the cols right
    df = df.rename(columns = {'countyFIPS':'fips', 'variable':'date', 'value':'deaths'})
    #swapping date and fips due to a DB design.
    titles = list(df.columns)
    titles[0],titles[1] = titles[1],titles[0]
    df = df[titles]
    return df

#-------------------------mask mandate by county---------------------
def cleanMaskMandate(df):
    df = joinFIPS(df, 'fips_state', 'fips_county')
    #copying codes, descs, and unit into own table.
    df1 = df[['order_code', 'face_masks_required_in_public']]
    df1 = df1.drop_duplicates()
    #function to save df1
    df1 = df1.dropna()
    load.loadToCSV(df1,'mask_orders_codes', False, index_name='order_code')
    load.loadToSQL(df1,'mask_orders_codes',False)
    df = df.drop(['face_masks_required_in_public'],axis=1)
    df = df.dropna()
    return df

#-------------------------bars---------------------------------------
def cleanBars(df):
    df = joinFIPS(df, 'fips_state', 'fips_county')
    #copying codes, descs, and unit into own table.
    df1 = df[['order_code', 'action']]
    df1 = df1.drop_duplicates()
    #function to save df1
    df1 = df1.replace({np.nan:None})
    load.loadToCSV(df1,'bar_orders_codes', False, index_name='order_code')
    load.loadToSQL(df1,'bar_orders_codes',False)
    df = df.drop(['action'],axis=1)
    df.dropna()
    return df

#-------------------------rests--------------------------------------
def cleanRests(df):
    df = joinFIPS(df,'fips_state','fips_county')
    #copying codes, descs, and unit into own table.
    df1 = df[['order_code', 'action']]
    df1 = df1.drop_duplicates()
    #function to save df1
    df1 = df1.replace({np.nan:None})
    load.loadToCSV(df1,'rest_orders_codes', False, index_name='order_code')
    load.loadToSQL(df1,'rest_orders_codes',False)
    df = df.drop(['action'],axis=1)
    df.dropna()
    return df

#-------------------------stay at home-------------------------------
def cleanStayAtHome(df):
    df = joinFIPS(df,'fips_state', 'fips_county')
    #copying codes, descs, and unit into own table.
    df1 = df[['order_code', 'stay_at_home_order']]
    df1 = df1.drop_duplicates()
    #Dropping artefact where NaN and another one exists.
    df1 = df1.dropna()
    load.loadToCSV(df1,'home_orders_codes', False, index_name='order_code')
    load.loadToSQL(df1,'home_orders_codes',False)
    df = df.drop(['stay_at_home_order'],axis=1)
    df.dropna()
    return df
#Author: Danny Lillard
#Date: 10/27/2021
#Desc: Join documentation with COVID-19 data for the COVID project

#NOTE: I DO NOT reccomend opening ANY file with Excel, it will attempt to change the formatting

#Data file:
#-Data:
#--All files which are updated by ETL
#--static
#----All files not affected by ETL

#for all columns that are date dependent we have the index saved(all the way to the left)

#what is join: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.join.html

#left join vs right vs etc: https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fi.stack.imgur.com%2FVQ5XP.png&f=1&nofb=1

import pandas as pd

#insert own path here.
df = pd.read_csv('D:\\Documents\\UTM\\CSCI\\495\\final-proj-covid\\data\\static\\uscounties.csv')
print(df.head())

df1 = pd.read_csv('D:\\Documents\\UTM\\CSCI\\495\\final-proj-covid\\data\\cases.csv')
print(df1.head())

#telling pandas the date column is a date column (lets us grab ranges)
df1['date'] = pd.to_datetime(df1['date'], format='%Y-%m-%d')

#lets grab the latest case data we currently have. 2021-10-24
latest_only = df1[(df1['date'] == '2021-10-24')]
print(latest_only.head())

#joining them on fips codes
joined = df.merge(latest_only,left_on='county_fips',right_on='fips')
print(joined.head())

#------Merging on range---------
april_2021 = df1[(df1['date'] >= '2021-04-01') & (df1['date'] <= '2021-04-30')]
joined_april = df.merge(april_2021,left_on='county_fips',right_on='fips')
print(joined_april.head())

#left_on and right_on tell us which variables will be the same for the two, must have
#same value columns.

#we can create a sub df from any dataframe with this form:
#df_new = df[(statement about df row) & (statement about df row)]

#creating a df that shows growth in cases per county in april.
#NOTE: there are probably better ways of doing this.
april_2021_diff = df1[(df1['date'] == '2021-04-30')]
april_2021_diff = april_2021_diff.merge(df1[(df1['date'] == '2021-04-01')],left_on='fips', right_on='fips')
april_2021_diff['countyGrowth'] = april_2021_diff['cases_x'] - april_2021_diff['cases_y']
print(april_2021_diff.head())
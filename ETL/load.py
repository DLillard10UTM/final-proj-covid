# Author: Danny Lillard
# Date: 10/20/2021
# Desc: contains loading code for the COVID county analysis.

import pandas as pd
import pyodbc

#Loads to my csv to be loaded to sql
def loadToCSV(df, tableName, val, index_name='fips'):
    df.to_csv(tableName + '.csv',index=val)
    print('saved to csv: ' + tableName)

# Args:
#   df: the dataframe we are reading from
#   tableName: the tableName to be loaded to.
#   val: whether to insert the df index as well or not.
# Output:
#   Either stops due to SQL error or inserts table and says on terminal
#   that the table has been inserted.
def loadToSQL(df,tableName,val):
    # Connect to SQL Server
    conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=DESKTOP-QV0VILT;'
                      'Database=senior_proj_covid;'
                      'Trusted_Connection=yes;')
    cursor = conn.cursor()
    cursor.execute("DELETE FROM " + tableName)
    #df.shape[1] = num of columns
    #in the query ? will be filled by args.
    for row in df.itertuples(index=val):
        if(val):
            query = ('''
                INSERT INTO ''' + tableName + 
                ''' VALUES (''' + '?,'*(df.shape[1]) + '''?)'''
                )
        else:
            query = ('''
                INSERT INTO ''' + tableName + 
                ''' VALUES (''' + '?,'*(df.shape[1]-1) + '''?)'''
                )
        #the * operator in python unpacks an array
        #here we are passing the row into args.
        cursor.execute(query, *grabRow(row))
    conn.commit()
    print("loaded to db: " + tableName)

#grabs the values for a row and puts them in a list
def grabRow(row):
    ourRow = []
    for item in row:
        ourRow.append(item)
    return ourRow

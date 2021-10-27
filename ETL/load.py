# Author: Danny Lillard
# Date: 10/20/2021
# Desc: contains loading code for the COVID county analysis.

import pandas as pd

#Loads to my csv to be loaded to sql
def loadToCSV(df, tableName, val, index_name='fips'):
    df.to_csv(tableName + '.csv',index=val)
    print('Loaded: ' + tableName)

def loadToSQL(df):
    # Connect to SQL Server
    conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=RON\SQLEXPRESS;'
                      'Database=test_database;'
                      'Trusted_Connection=yes;')
    cursor = conn.cursor()
    for row in df.itertuples():
        cursor.execute('''
                INSERT INTO products (product_id, product_name, price)
                VALUES (?,?,?)
                ''',
                row.product_id, 
                row.product_name,
                row.price
                )
    conn.commit()
# Author: Danny Lillard
# Date: 9/27/2021
# Desc: Main driver for ETL process.b

import extract
import transform
import load


#-------------------Cases by county (over time):---------------------
ourURL = "https://static.usafacts.org/public/data/covid-19/covid_confirmed_usafacts.csv?_ga=2.117311823.850253249.1634047657-1224035268.1634047657"

df = extract.grabCaseData(ourURL)

#check if empty and clean file.
if(df.empty):
    print("ERROR empty cases by county.")
    exit()
df = transform.cleanCases(df)
load.loadToCSV(df, 'cases', True,index_name='id')
load.loadToSQL(df,'cases',True)
print(len(df))

#-----------------stay at home---------------------------------------
ourURL = "https://data.cdc.gov/resource/y2iy-8irm.csv"

#only grab the wanted columns and load those into a df.
wantedCols = ['fips_state','fips_county', 'date', 'order_code', 'stay_at_home_order']

#check if empty and clean file.
df = extract.csvTodf(ourURL, wantedCols)
if(df.empty):
    print("ERROR empty stay at home.")
    exit()
print(len(df))
df = transform.cleanStayAtHome(df)
load.loadToCSV(df, 'home_order',True,index_name='id')
load.loadToSQL(df,'home_order',True)

#-----------------restaurants----------------------------------------
ourURL = "https://data.cdc.gov/resource/azmd-939x.csv"
#TODO: check if empty and clean each file.
wantedCols = ['fips_state', 'fips_county', 'date', 'order_code','action']
df = extract.csvTodf(ourURL, wantedCols)
#check if empty and clean file.
if(df.empty):
    print("ERROR empty rest openings.")
    exit()
df = transform.cleanRests(df)
load.loadToCSV(df, 'rest_orders', True,index_name='id')
load.loadToSQL(df,'rest_orders',True)

#-----------------bars opening---------------------------------------
ourURL = "https://data.cdc.gov/resource/9kjw-3miq.csv"
#TODO: check if empty and clean each file.

wantedCols = ['fips_state', 'fips_county', 'date', 'order_code', 'action']
df = extract.csvTodf(ourURL, wantedCols)

if(df.empty):
    print("ERROR empty bar openings.")
    exit()
df = transform.cleanBars(df)
load.loadToCSV(df, 'bar_orders', True,index_name='id')
load.loadToSQL(df,'bar_orders',True)

#-----------------mask mandates--------------------------------------
ourURL = "https://data.cdc.gov/resource/62d6-pm5i.csv"
#TODO: check if empty and clean each file.

wantedCols = ['fips_state', 'fips_county', 'date', 'order_code', 'face_masks_required_in_public']
df = extract.csvTodf(ourURL, wantedCols)

if(df.empty):
    print("ERROR empty mask mandates.")
    exit()
df = transform.cleanMaskMandate(df)
load.loadToCSV(df, 'mask_mandates', True)
load.loadToSQL(df,'mask_mandates',True)

#-----------------deaths(over time)----------------------------------
ourURL = "https://static.usafacts.org/public/data/covid-19/covid_deaths_usafacts.csv?_ga=2.175383649.2141588741.1635868472-1224035268.1634047657"

df = extract.grabCaseData(ourURL)

#check if empty and clean file.
if(df.empty):
    print("ERROR empty deaths.")
    exit()
df = transform.cleanDeaths(df)
load.loadToCSV(df, 'deaths', True,index_name='id')
load.loadToSQL(df,'deaths',True)

#-----------------vaccine hesitancy----------------------------------
ourURL = "https://data.cdc.gov/resource/q9mh-h2tw.csv"
#TODO: check if empty and clean each file.

#we have to grab the SVI to drop into the county table.
wantedCols = ['fips_code', 'estimated_hesitant', 'estimated_hesitant_or_unsure', 'estimated_strongly_hesitant',
              'social_vulnerability_index', 'svi_category', 'ability_to_handle_a_covid',
              'cvac_category']

df = extract.csvTodf(ourURL, wantedCols)
#check if empty and clean file.
if(df.empty):
    print("ERROR empty vaccine hes.")
    exit()
df = transform.cleanVaccineHes(df)
print(len(df))
load.loadToCSV(df, 'vaccine_hes', False)
load.loadToSQL(df,'vaccine_hes',True)

#-----------------vaccinated by county-------------------------------
ourURL = "https://data.cdc.gov/resource/8xkx-amqh.csv"
#TODO: check if empty and clean each file.

wantedCols = ['date', 'fips', 'series_complete_pop_pct', 'series_complete_12pluspop', 
              'series_complete_18pluspop', 'series_complete_65pluspop', 'administered_dose1_pop_pct',
              'administered_dose1_recip_12pluspop_pct', 'administered_dose1_recip_18pluspop_pct',
              'administered_dose1_recip_65pluspop_pct']

df = extract.csvTodf(ourURL, wantedCols)
if(df.empty):
    print("ERROR empty vaccine by county.")
    exit()
df = transform.cleanVaccine(df)
load.loadToCSV(df, 'vaccinated', True,index_name='id')
load.loadToSQL(df,'vaccinated',True)

print("ETL job finished")
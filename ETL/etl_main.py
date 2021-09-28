# Author: Danny Lillard
# Date: 9/27/2021
# Desc: Main driver for ETL process.b

from transform import csvTodf
import extract

#-----------------stay at home---------------------------------------
ourURL = "https://data.cdc.gov/resource/y2iy-8irm.csv"
dataAsText = extract.grabData(ourURL)
#TODO: check if empty and clean each file.

#only grab the wanted columns and load those into a df.
#-----------------restaurants----------------------------------------
ourURL = "https://data.cdc.gov/resource/azmd-939x.csv"
dataAsText = extract.grabData(ourURL)
#TODO: check if empty and clean each file.

#-----------------bars opening---------------------------------------
ourURL = "https://data.cdc.gov/resource/9kjw-3miq.csv"
dataAsText = extract.grabData(ourURL)
#TODO: check if empty and clean each file.

wantedCols = ['FIPS_State', 'FIPS_County', 'date', 'order_code', 'Face_Masks_Required_in_Public']
csvTodf(dataAsText, wantedCols)

#-----------------mask mandates--------------------------------------
ourURL = "https://data.cdc.gov/resource/62d6-pm5i.csv"
dataAsText = extract.grabData(ourURL)
#TODO: check if empty and clean each file.

wantedCols = ['FIPS_State', 'FIPS_County', 'date', 'order_code', 'Face_Masks_Required_in_Public']
csvTodf(dataAsText, wantedCols)

#-----------------deaths---------------------------------------------
ourURL = "https://data.cdc.gov/resource/kn79-hsxy.csv"
dataAsText = extract.grabData(ourURL)
#TODO: check if empty and clean each file.

wantedCols = ['Date as of', 'FIPS County Code', 'Urban Rural Code', 'Deaths involving COVID-19']
csvTodf(dataAsText, wantedCols)

#-----------------vaccine hesitancy----------------------------------
ourURL = "https://data.cdc.gov/resource/q9mh-h2tw.csv"
dataAsText = extract.grabData(ourURL)
#TODO: check if empty and clean each file.

#we have to grab the SVI to drop into the county table.
#TODO: if no-one else has county name get it from here.
wantedCols = ['FIPS Code', 'Estimated hesitant', 'Estimated hesitant or unsure', 'Estimated strongly hesitant',
              'Social Vulnerability Index (SVI)', 'SVI Category', 'CVAC level of concern for vaccination rollout',
              'CVAC Level Of Concern']
csvTodf(dataAsText, wantedCols)

#-----------------vaccinated by county-------------------------------
ourURL = "https://data.cdc.gov/resource/8xkx-amqh.csv"
dataAsText = extract.grabData(ourURL)
#TODO: check if empty and clean each file.

wantedCols = ['Date', 'FIPS', 'Series_Comp_Pop_Pct', 'Series_Complete_12PlusPop_Pct', 
              'Series_Complete_18PlusPop_Pct', 'Series_Complete_65PlusPop_Pct', 'Administered_Dose1_Pop_Pct',
              'Administered_Dose1_Recip_12PlusPop_Pct', 'Administered_Dose1_Recip_18PlusPop_Pct',
              'Administered_Dose1_Recip_65PlusPop_Pct']
csvTodf(dataAsText, wantedCols)


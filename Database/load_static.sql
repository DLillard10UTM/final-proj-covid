--Author: Danny L
--Date: 10/25/2021
--Desc: load for the static, non updating data. (not grabbed by ETL)

BULK
INSERT [senior_proj_covid].[dbo].[us_counties]
FROM 'C:\Users\danny\OneDrive\Desktop\sql\uscounties.csv'
WITH
(
FIRSTROW=2,
FIELDTERMINATOR = ',',
ROWTERMINATOR = '\n',
FIELDQUOTE = '"'
)
GO

SELECT *
FROM [senior_proj_covid].[dbo].[us_counties]
GO

BULK
INSERT [senior_proj_covid].[dbo].[income]
FROM 'D:\Documents\UTM\CSCI\495\final-proj-covid\data\static\income.csv'
WITH
(
FIELDTERMINATOR = ',',
ROWTERMINATOR = '\n'
)
GO

BULK
INSERT [senior_proj_covid].[dbo].[income_codes]
FROM 'D:\Documents\UTM\CSCI\495\final-proj-covid\data\static\income_codes.csv'
WITH
(
FIELDTERMINATOR = ',',
ROWTERMINATOR = '\n'
)
GO

BULK
INSERT [senior_proj_covid].[dbo].[metro_codes]
FROM 'D:\Documents\UTM\CSCI\495\final-proj-covid\data\static\metro_codes.csv'
WITH
(
FIELDTERMINATOR = ',',
ROWTERMINATOR = '\n'
)
GO
BULK
INSERT bar_orders
FROM 'D:\Documents\UTM\CSCI\495\final-proj-covid\data\bar_orders.csv'
WITH
(
FIELDTERMINATOR = ',',
ROWTERMINATOR = 'D:\Documents\UTM\CSCI\495\final-proj-covid\data\bar_orders_codes.csv'
)
GO

BULK
INSERT deaths
FROM 'D:\Documents\UTM\CSCI\495\final-proj-covid\data\deaths.csv'
WITH
(
FIELDTERMINATOR = ',',
ROWTERMINATOR = '\n'
)
GO

BULK
INSERT home_order
FROM 'D:\Documents\UTM\CSCI\495\final-proj-covid\data\home_order.csv'
WITH
(
FIELDTERMINATOR = ',',
ROWTERMINATOR = '\n'
)
GO

BULK
INSERT home_orders_codes
FROM 'D:\Documents\UTM\CSCI\495\final-proj-covid\data\home_order_codes.csv'
WITH
(
FIELDTERMINATOR = ',',
ROWTERMINATOR = '\n'
)
GO

BULK
INSERT mask_mandates
FROM 'D:\Documents\UTM\CSCI\495\final-proj-covid\data\mask_mandates.csv'
WITH
(
FIELDTERMINATOR = ',',
ROWTERMINATOR = '\n'
)
GO

BULK
INSERT mask_orders_codes
FROM 'D:\Documents\UTM\CSCI\495\final-proj-covid\data\mask_orders_codes.csv'
WITH
(
FIELDTERMINATOR = ',',
ROWTERMINATOR = '\n'
)
GO

BULK
INSERT rest_orders
FROM 'D:\Documents\UTM\CSCI\495\final-proj-covid\data\rest_orders.csv'
WITH
(
FIELDTERMINATOR = ',',
ROWTERMINATOR = '\n'
)
GO

BULK
INSERT rest_orders_codes
FROM 'D:\Documents\UTM\CSCI\495\final-proj-covid\data\rest_orders_codes.csv'
WITH
(
FIELDTERMINATOR = ',',
ROWTERMINATOR = '\n'
)
GO

BULK
INSERT vaccinated
FROM 'D:\Documents\UTM\CSCI\495\final-proj-covid\data\vaccinated.csv'
WITH
(
FIELDTERMINATOR = ',',
ROWTERMINATOR = '\n'
)
GO

BULK
INSERT vaccine_hes
FROM 'D:\Documents\UTM\CSCI\495\final-proj-covid\data\vaccine_hes.csv'
WITH
(
FIELDTERMINATOR = ',',
ROWTERMINATOR = '\n'
)
GO
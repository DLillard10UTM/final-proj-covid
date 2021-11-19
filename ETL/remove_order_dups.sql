/****** Script for SelectTopNRows command from SSMS  ******/
DELETE t1 FROM [senior_proj_covid].[dbo].[home_order] t1
WHERE EXISTS (SELECT 1 from [senior_proj_covid].[dbo].[home_order] as t2
              WHERE t1.order_code = t2.order_code
              AND t2.id + 1 = t1.id);
GO

DELETE t1 FROM [senior_proj_covid].[dbo].[bar_orders] t1
WHERE EXISTS (SELECT 1 from [senior_proj_covid].[dbo].[bar_orders] as t2
              WHERE t1.order_code = t2.order_code
              AND t2.id + 1 = t1.id);
GO

DELETE t1 FROM [senior_proj_covid].[dbo].[mask_mandates] t1
WHERE EXISTS (SELECT 1 from [senior_proj_covid].[dbo].[mask_mandates] as t2
              WHERE t1.order_code = t2.order_code
              AND t2.id + 1 = t1.id);
GO

DELETE t1 FROM [senior_proj_covid].[dbo].[rest_orders] t1
WHERE EXISTS (SELECT 1 from [senior_proj_covid].[dbo].[rest_orders] as t2
              WHERE t1.order_code = t2.order_code
              AND t2.id + 1 = t1.id);
GO
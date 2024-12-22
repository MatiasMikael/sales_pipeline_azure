SELECT TOP 1 Product_Category, SUM(Quantity) AS TotalQuantity
FROM retail_sales_dataset
GROUP BY Product_Category
ORDER BY TotalQuantity DESC;

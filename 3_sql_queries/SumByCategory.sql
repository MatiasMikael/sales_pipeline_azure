SELECT Product_Category, SUM(Total_Amount) AS TotalSales
FROM retail_sales_dataset
GROUP BY Product_Category
ORDER BY TotalSales DESC;

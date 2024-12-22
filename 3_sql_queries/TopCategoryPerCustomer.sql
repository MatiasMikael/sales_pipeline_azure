SELECT Customer_ID, Product_Category, SUM(Total_Amount) AS TotalSpent
FROM retail_sales_dataset
GROUP BY Customer_ID, Product_Category
ORDER BY Customer_ID, TotalSpent DESC;

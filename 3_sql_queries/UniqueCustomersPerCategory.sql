SELECT Product_Category, COUNT(DISTINCT Customer_ID) AS UniqueCustomers
FROM retail_sales_dataset
GROUP BY Product_Category
ORDER BY UniqueCustomers DESC;

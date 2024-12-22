SELECT MONTH(Date) AS SaleMonth, SUM(Total_Amount) AS MonthlySales
FROM retail_sales_dataset
GROUP BY MONTH(Date)
ORDER BY SaleMonth;

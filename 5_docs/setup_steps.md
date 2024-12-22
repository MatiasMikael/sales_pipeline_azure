### SQL Setup Instructions
Perform these steps before creating SQL queries.

1. Create Master Key
Name: CreateMasterKey
Create a master key to encrypt sensitive credentials in the database.

CREATE MASTER KEY ENCRYPTION BY PASSWORD = 'YourPassword';

2. Create Blob Credential
Name: CreateBlobCredential
Set up a database-scoped credential to securely access Azure Blob Storage using a SAS token.

3. CREATE DATABASE SCOPED CREDENTIAL MyBlobCredential
WITH IDENTITY = 'SHARED ACCESS SIGNATURE',
SECRET = 'YourSAS-token';

4. Create External Data Source
Name: CreateExternalDataSource
Link the database to the Azure Blob Storage container where the CSV file is stored.

5. CREATE EXTERNAL DATA SOURCE MyBlobStorage
WITH (
TYPE = BLOB_STORAGE,
LOCATION = 'https://salespipelineazure.blob.core.windows.net/raw-data',
CREDENTIAL = MyBlobCredential
);

6. Load Data
Name: BulkInsertRetailSalesData
Load the CSV file from Blob Storage into the SQL table retail_sales_dataset.

BULK INSERT retail_sales_dataset
FROM 'retail_sales_dataset.csv'
WITH (
DATA_SOURCE = 'MyBlobStorage',
FORMAT = 'CSV',
FIRSTROW = 2,
FIELDTERMINATOR = ',',
ROWTERMINATOR = '\n'
);

7. Verify Loaded Data
Name: CheckRetailSalesData
Confirm that data was successfully loaded into the table.

8. SELECT TOP 10 * FROM retail_sales_dataset;
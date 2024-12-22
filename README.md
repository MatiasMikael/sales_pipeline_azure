## sales_pipeline_azure
This project sets up a semi-automated pipeline for managing, storing, and analyzing retail sales data. It involves manually downloading a dataset, uploading it to Azure Blob Storage using a script, and querying it in Azure SQL Database, with some steps requiring manual intervention.

### Project Structure
#### Project Folder
The project folder contains subfolders and files structured as follows:

- 1_scripts: Python scripts for data processing.
- 2_data: Raw and unprocessed data files.
- 3_sql_queries: SQL scripts for querying the data.
- 4_results: Query results and analysis outputs.
- 5_docs: Documentation related to the project.

#### Virtual Environment
A Python virtual environment (venv) is created and activated to manage dependencies.

#### Dataset
The retail sales dataset is downloaded as a .zip file from Kaggle and extracted into the 2_data folder.

### Tools and Technologies
#### Python

- Libraries: azure-storage-blob, os, and others for handling data and Azure interactions.

#### Azure

- Azure Blob Storage: Used to store the raw dataset.
- Azure SQL Database: Used for storing and querying the dataset.

#### SQL

- SQL scripts stored in the 3_sql_queries folder for data analysis.

### Workflow
**Data Preparation**
The dataset is downloaded and extracted into the 2_data folder.

**Upload to Azure**
The load_to_blob.py script uploads the data from the local folder to Azure Blob Storage.

**SQL Setup**
The data is loaded into an Azure SQL table for querying.

**Data Analysis**
SQL queries from the 3_sql_queries folder are executed, and results are stored in the 4_results folder.

### License
This project is licensed under the MIT License. The dataset is provided under the CC0: Public Domain license: Retail Sales Dataset. https://www.kaggle.com/datasets/mohammadtalib786/retail-sales-dataset

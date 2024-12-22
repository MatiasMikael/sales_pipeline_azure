from azure.storage.blob import BlobServiceClient
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Azure Blob Storage configuration
connection_string = os.getenv("AZURE_CONNECTION_STRING")
if not connection_string:
    raise ValueError("Connection string not found in environment variables.")

container_name = "raw-data"
blob_name = "retail_sales_dataset.csv"
file_path = r"C:\Users\Matias\Desktop\sales_pipeline_azure\2_data\retail_sales_dataset.csv"

if not os.path.exists(file_path):
    raise FileNotFoundError(f"File {file_path} does not exist.")

try:
    blob_service_client = BlobServiceClient.from_connection_string(connection_string)
    container_client = blob_service_client.get_container_client(container_name)

    if not container_client.exists():
        container_client.create_container()

    blob_client = blob_service_client.get_blob_client(container=container_name, blob=blob_name)
    with open(file_path, "rb") as data:
        blob_client.upload_blob(data, overwrite=True)

    print("File uploaded successfully.")

except Exception as e:
    print(f"Error: {e}")

# Databricks notebook source
# MAGIC %md
# MAGIC <img src="https://cdn.eleflow.com.br/ef-web/wp-content/uploads/2016/08/21181642/Eleflow.png" alt="Eleflow BigData" width="200"/>
# MAGIC 
# MAGIC ---
# MAGIC 
# MAGIC # Google Sheets

# COMMAND ----------

## Importing required modules
from eleflow.connector.google_sheet import GoogleSheetConnection

# COMMAND ----------

## Setting the credentials_info that can get by the Azure KeyVault
credentials_info = {
    "client_email":"airbyte-775@inlaid-isotope-307013.iam.gserviceaccount.com",
    "token_uri":"https://oauth2.googleapis.com/token",
    "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvAIBADANBgkqhkiG9w0BAQEFAASCBKYwggSiAgEAAoIBAQCv3F4UZRL3AhqH\nC/82Gb/XkS0Alk0iUyWRGwR/qzK/R3450uCQ2Ha8clid7pF1Lt4FDaHDPLNK9aG1\n0sbQFo/kxcEhLklWoR14A31uhEOmhTH6vv04jgDWPF550c3SKACxi5NELKmyiWCM\nRGV3tAhYhS70lzS5MhUZykp33LkVqboohBX149wjoI8cyyGugNdWbO5lLUnoPCuu\nuTNUS2OaRvnGSo8b0gZJvlMfomSyaWcl/aUtLplOjgXEyQoK7vkaYPEbcbZxZq8C\n6G/2Zg4bhs44qjVK/RLWx01QCCmJnbSsxe1pel0v54cC+M9jwvJprAszcWTwk6Uv\nCbw+AHelAgMBAAECggEADoQIifNr1NKqIOKHHs6STLdReR5u4HnvfGI4BVe6uRos\nG5bB7YLIjjZ8BRE3lW4Yal9dLlHY1MOgpPLwcSWjm/UMw3HgINPsrEbReClXsiuF\nXBaerSfffs991t1P+VxO7ljAf5yWJ0P6oalVnMNR+wiHPy4p7m1pW3ccnXctGdIE\nscrZeMF0tYiMxrpceWLwsqD0VHFGKtCCMNNxdIwhYzUVhX9sSDzASuPZ5r3ToakE\n7nIMc23IT0zEVutGP5IJTXgYgiNFsJpkt1h5jGRR65TMXa07Vvmz1IZsVt47pKL8\na/9t5TK+JzPHROyiUMlQGeutfv3ZaJLj6BfT45tWAwKBgQD4hOFFZOJCOXVSZAwG\nI6czz0BFkhg/aqdfy7WgmEsXRAPJaBJs0cuDdI6/nneuHW80gF0VAHP56V+zDUyi\n7x83N6w0Qr+kimjEafP2NB6MEiWkB29PNjRaKVHcGHVI8p1Hh8L1lcUvYh3Di+oK\n7QBcvnRN9mLZnY5vqCja2e5McwKBgQC1J5LanipxkkaTbhYOX+JFfd44vf6Oi14v\nIiNWidtvjcZocXua3Q9b+RMMsoPgv5Xp40SR5zLiu83esVoh1VsoGwC9yCqKrfBL\nq/JTz62kcisllFJ9M3jGxPeE4+Cnba57V7PrCx4mowi0vNd7Qdh6NbLbYD/odj0x\nyf8lI3Z9hwKBgGD0dm58TUlI4Vyja415m2G7GXgK5yrWkTXuY42j3KfXASMyVv3d\nW2iNsKNRT5++HAR/j9EBvD1jrtJL/foTEDqanbRF1j57QSRfsa37527+JXE49VQR\n8Zq7RBR59kffXzzo2ka1h5hUzwfbLhPVIq8MHpPL7AS6Uzd8g3PeUfnBAoGAbGKo\nB6s4Q8k79ruX8LPHosJDMfnjExApotOvBvjmVKEjw5uaU7bNmL62ehNYuiCGpnB2\nt0D3/hZVf1bnUXTg3GcDk4jugxi8u9m93A1WnBw+2nYawJQKQAra+SSKZkJGcb+w\ngwGc4YsMC28tEa78wWndgEnfEsujo2VzBZppK4MCgYBLqVWzsXlqWemddLmrZ6em\nQSoRMOyUeYltAZzrTm8Q/xh2RuUyT8dIR0bsmjiJ9tPLHCQqRytuikRcO4PTUbsM\nRy+OL+BidBIQuCoezX+bx5IPO0kw9NVhN8a66RgI+blGTQ0hKz04se55GKRvaANd\nvpaXwlG8VOi1beDv1WdJcA==\n-----END PRIVATE KEY-----\n",
}

# COMMAND ----------

## Create a connection
connection = GoogleSheetConnection.from_credentials_info(credentials_info)
# connection = GoogleSheetConnection.from_credentials_info(credentials_info)

# COMMAND ----------

## Getting the service client
service_client = connection.get_service_client()

# COMMAND ----------

## Getting a spreadsheet
spreadsheet = service_client.get_spreadsheet('1XignRPBe8WoXMONRtAu1Ip0Y7OcFxfgICZWI1LOTJP0')

# COMMAND ----------

## Displaying sheets names
print(
    spreadsheet.get_sheets_names()
)

# COMMAND ----------

## Gett a specific sheet
sheet = spreadsheet.get_sheet_from_name('medals')

# COMMAND ----------

## From this sheet we can view values as SparkDataFrame
dataframe = sheet.to_spark_dataframe()
display(
    dataframe
)

# COMMAND ----------

## From this Spark DataFrame we can export/save to another format, as DeltaTable for example
dataframe.write.format('delta').mode('overwrite').save('dbfs:/FileStore/databricks_training/google_sheets/medals')

# COMMAND ----------

# MAGIC %sql
# MAGIC -- After saved our Delta Table, we can create a table from this Delta with SQL
# MAGIC CREATE DATABASE IF NOT EXISTS google_sheet;
# MAGIC CREATE TABLE IF NOT EXISTS google_sheet.medals USING DELTA LOCATION 'dbfs:/FileStore/databricks_training/google_sheets/medals' 

# COMMAND ----------

# MAGIC %sql
# MAGIC -- Visualizing the medals Delta Table
# MAGIC SELECT * FROM google_sheet.medals

# Databricks notebook source
# MAGIC %md
# MAGIC <img src="https://cdn.eleflow.com.br/ef-web/wp-content/uploads/2016/08/21181642/Eleflow.png" alt="Eleflow BigData" width="200"/>
# MAGIC 
# MAGIC ---
# MAGIC 
# MAGIC # Google Sheets
# MAGIC 
# MAGIC _Obs: Os dados usados neste exemplo são dados públicos e foram obtidos no site da ANAC_

# COMMAND ----------

# DBTITLE 1,Importing required modules
from eleflow.connector.google_sheet import GoogleSheetConnection

# COMMAND ----------

# DBTITLE 1,Create a connection
connection = GoogleSheetConnection.from_credentials_info({
    "client_email" : dbutils.secrets.get(scope="kv-eleflow", key="google-sheets-api-email"),
    "private_key" : dbutils.secrets.get(scope="kv-eleflow", key="google-sheets-api-key"),
    "token_uri" : "https://oauth2.googleapis.com/token"
})

# COMMAND ----------

# DBTITLE 1,Getting the service client
service_client = connection.get_service_client()

# COMMAND ----------

# DBTITLE 1,Getting a spreadsheet
spreadsheet = service_client.get_spreadsheet(spreadsheet_id='1XignRPBe8WoXMONRtAu1Ip0Y7OcFxfgICZWI1LOTJP0')

# COMMAND ----------

# DBTITLE 1,Displaying sheets names
print(
    spreadsheet.get_sheets_names()
)

# COMMAND ----------

# DBTITLE 1,Getting a specific sheet
sheet = spreadsheet.get_sheet_from_name('Cias Aéreas')

# COMMAND ----------

display(
    sheet.to_spark_dataframe()
)

# COMMAND ----------

# DBTITLE 1,Saving in bronze layer
(
    sheet
    .to_spark_dataframe()
    .write
    .format('delta')
    .mode('append')
    .save(bronze_cias_aereas_location)
)

# COMMAND ----------

# DBTITLE 1,Creating table using Delta location
spark.sql(f"""CREATE TABLE IF NOT EXISTS bronze.cias_aereas USING DELTA LOCATION '{bronze_cias_aereas_location}'""")

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT * FROM bronze.cias_aereas

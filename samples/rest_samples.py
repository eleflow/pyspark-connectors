# Databricks notebook source
# MAGIC %md
# MAGIC <img src="https://cdn.eleflow.com.br/ef-web/wp-content/uploads/2016/08/21181642/Eleflow.png" alt="Eleflow BigData" width="200"/>
# MAGIC 
# MAGIC ---
# MAGIC 
# MAGIC # REST API
# MAGIC 
# MAGIC _Obs: Os dados usados neste exemplo são dados públicos e foram obtidos no site da ANAC_

# COMMAND ----------

# DBTITLE 1,Importing required modules
from eleflow.connector.rest_api import RestApiConnection

# COMMAND ----------

# DBTITLE 1,Create a connection
connection = RestApiConnection.build(url_base='https://apimngt-databricks-training.azure-api.net',
                                     api_token_key='Authorization',
                                     api_token_value=dbutils.secrets.get(scope="kv-eleflow", key="vra-api-authorization-key"))
# https://apimngt-databricks-training.azure-api.net/vra/v1/{icao}/{ano}

# COMMAND ----------

# DBTITLE 1,Getting the service client
client = connection.get('vra', 'v1', 'AZU', '2021')

# COMMAND ----------

# DBTITLE 1,Displaying response in a Spark Dataframe
display(
    client.to_spark_dataframe()
)

# COMMAND ----------

# DBTITLE 1,Displaying specific key from response in a Spark Dataframe
api_df = client.to_spark_dataframe('data')
display(
    api_df
)

# COMMAND ----------

# DBTITLE 1,Get response as JSON
response = client.to_json()

# COMMAND ----------

for page in range(2, response['total_pages']):
    print(f'Extracting page {page}...')
    api_df = api_df.union(connection.get('vra', 'v1', 'AZU', '2021', **{'page':page}).to_spark_dataframe('data'))

# COMMAND ----------

# DBTITLE 1,Saving in bronze layer
(
    api_df
    .write
    .format('delta')
    .mode('append')
    .save(bronze_vra_location)
)

# COMMAND ----------

# DBTITLE 1,Creating table using Delta location
spark.sql(f"""CREATE TABLE IF NOT EXISTS bronze.vra USING DELTA LOCATION '{bronze_vra_location}'""")

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT * FROM bronze.vra

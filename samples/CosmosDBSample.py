# Databricks notebook source
# MAGIC %md
# MAGIC <img src="https://cdn.eleflow.com.br/ef-web/wp-content/uploads/2016/08/21181642/Eleflow.png" alt="Eleflow BigData" width="200"/>
# MAGIC 
# MAGIC ---
# MAGIC 
# MAGIC # CosmosDB

# COMMAND ----------

## Importing required modules
from eleflow.connector import CosmosDBConnection

# COMMAND ----------

connection = CosmosDBConnection.build("https://cosmosdb-eleflow-training.documents.azure.com:443/", "JUpaJH2a6NIKjQV5KIAd2yDpK30hURk1TI81tTe4g5sUbKs2WyVrysRA3752xguvYJkJ6EeASc4P5hyulWu1BA==")

# COMMAND ----------

client = connection.get_service_client(database="db_training", colection="character", partition_key="/id")

# COMMAND ----------

doc = client.query_items("select * from c where CONTAINS(c.title,'Star')")

# COMMAND ----------

display(
    doc.to_spark_dataframe()
)

# COMMAND ----------

doc = client.get_by_id("1")

# COMMAND ----------

doc.get_document()

# COMMAND ----------

display(
    doc.to_spark_dataframe()
)

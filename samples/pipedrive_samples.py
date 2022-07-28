# Databricks notebook source
# MAGIC %md
# MAGIC <img src="https://cdn.eleflow.com.br/ef-web/wp-content/uploads/2016/08/21181642/Eleflow.png" alt="Eleflow BigData" width="200"/>
# MAGIC 
# MAGIC ---
# MAGIC 
# MAGIC # PipeDrive

# COMMAND ----------

# DBTITLE 1,Importing required modules
from eleflow.integrator.pipe_drive import PipeDriveConnection

# COMMAND ----------

# DBTITLE 1,Create a connection
connection = PipeDriveConnection.v1_from_token_api(dbutils.secrets.get(scope='kv-eleflow', key='pipedrive-api-token'))

# COMMAND ----------

# DBTITLE 1,Getting the service client
client = connection.get_service_client()

# COMMAND ----------

# DBTITLE 1,Displaying 'activity types' in Spark Dataframe
display(
    client.activity_types_service.get_all_activity_types().to_spark_dataframe('data')
)

# COMMAND ----------

# DBTITLE 1,Displaying 'users' in Spark Dataframe
display(
    client.users_service.get_all_users().to_spark_dataframe('data').drop('name', 'email')
)

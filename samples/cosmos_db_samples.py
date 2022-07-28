# Databricks notebook source
# MAGIC %md
# MAGIC <img src="https://cdn.eleflow.com.br/ef-web/wp-content/uploads/2016/08/21181642/Eleflow.png" alt="Eleflow BigData" width="200"/>
# MAGIC 
# MAGIC ---
# MAGIC 
# MAGIC # Azure CosmosDB
# MAGIC 
# MAGIC _Obs: Os dados usados neste exemplo são dados públicos e foram obtidos no site da ANAC_

# COMMAND ----------

# DBTITLE 1,Importing required modules
from eleflow.connector.azure_cosmosdb import CosmosDBConnection

# COMMAND ----------

# DBTITLE 1,Create a connection
connection = CosmosDBConnection.build(host=dbutils.secrets.get(scope="kv-eleflow", key="cosmos-db-host"), key=dbutils.secrets.get(scope="kv-eleflow", key="cosmos-db-key"))

# COMMAND ----------

# DBTITLE 1,Getting the service client
service_client = connection.get_service_client(database='db_training', colection='aerodromos', partition_key='/country')

# COMMAND ----------

# DBTITLE 1,Getting a document
doc = service_client.query_items('SELECT * FROM a')

# COMMAND ----------

# DBTITLE 1,Creating a schema for data
from pyspark.sql.types import StructType, StructField, StringType

schema = StructType([
    StructField(name='city', dataType=StringType(), nullable=True),
    StructField(name='country', dataType=StringType(), nullable=True),
    StructField(name='country_iso', dataType=StringType(), nullable=True),
    StructField(name='county', dataType=StringType(), nullable=True),
    StructField(name='iata', dataType=StringType(), nullable=True),
    StructField(name='icao', dataType=StringType(), nullable=True),
    StructField(name='id', dataType=StringType(), nullable=True),
    StructField(name='latitude', dataType=StringType(), nullable=True),
    StructField(name='location', dataType=StringType(), nullable=True),
    StructField(name='longitude', dataType=StringType(), nullable=True),
    StructField(name='name', dataType=StringType(), nullable=True),
    StructField(name='phone', dataType=StringType(), nullable=True),
    StructField(name='postal_code', dataType=StringType(), nullable=True),
    StructField(name='state', dataType=StringType(), nullable=True),
    StructField(name='street', dataType=StringType(), nullable=True),
    StructField(name='street_number', dataType=StringType(), nullable=True),
    StructField(name='uct', dataType=StringType(), nullable=True),
    StructField(name='website', dataType=StringType(), nullable=True),
])

# COMMAND ----------

# DBTITLE 1,Diplaying data with a specific schema
display(
    doc.to_spark_dataframe(schema)
)

# COMMAND ----------

# DBTITLE 1,Saving in bronze layer
(
    doc
    .to_spark_dataframe(schema)
    .write
    .format('delta')
    .mode('append')
    .save(bronze_aerodromos_location)
)

# COMMAND ----------

# DBTITLE 1,Creating table using Delta location
spark.sql(f"""CREATE TABLE IF NOT EXISTS bronze.aerodromos USING DELTA LOCATION '{bronze_aerodromos_location}'""")

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT * FROM bronze.aerodromos

# COMMAND ----------

# MAGIC %sql
# MAGIC DROP TABLE bronze.vra

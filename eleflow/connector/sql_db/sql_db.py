from pyspark.sql import SparkSession

class SQLDatabaseConnection(object):
  
  def __init__(self, db_type=None, db_domain=None, db_name=None, username=None, password=None, jdbc_url=None):
    self.db_type = db_type
    self.db_domain = db_domain
    self.db_name = db_name
    self.username = username
    self.password = password
    self.jdbc_url = jdbc_url
    
    if db_type is not None or db_domain is not None or db_name is not None or username is not None or password is not None or jdbc_url is not None:
      print(f"""Setting default SQL Database connection parameters, passed at object declaration:
db_type = '{db_type}', db_domain = '{db_domain}', db_name = '{db_name}', username length = {len(username)}, password length = {len(password)},
jdbc_url = '{jdbc_url}'""")
    
  def _get_connection(self, db_type=None, db_domain=None, db_name=None, username=None, password=None, jdbc_url=None):
    if db_type == None:
      db_type = self.db_type
    if db_domain == None:
      db_domain = self.db_domain
    if db_name == None:
      db_name = self.db_name
    if username == None:
      username = self.username
    if password == None:
      password = self.password
    if jdbc_url == None:
      jdbc_url = self.jdbc_url
    
    print("Setting connection to SQL Database by JDBC URL using Spark")
    
    if jdbc_url is not None:
      print(f"Setting connection by JDBC URL: '{jdbc_url}'")
    else:
      print(f"Setting connection to Database Type '{db_type}' at Domain '{db_domain}' and Database Name '{db_name}'")
      jdbc_url = f"jdbc:{db_type}://{db_domain};database={db_name}"
    
    _SPARK = SparkSession.builder.getOrCreate()
    spark_conn = _SPARK.read.format("jdbc").option("url", jdbc_url)
    
    print(f"Setting connection credentials. Username length is {len(username)} and Password length is {len(password)}")
    spark_conn = spark_conn.option("user", username).option("password", password)
    
    return spark_conn
  
  def query(self, query_string, db_type=None, db_domain=None, db_name=None, username=None, password=None, jdbc_url=None):
    query_conn = self._get_connection(db_type, db_domain, db_name, username, password, jdbc_url)
    
    print(f"Executing query at Database:\n{query_string}")
    result_df = query_conn.option("query", query_string).load()
    
    print("Showing query Spark Dataframe response:")
    result_df.show()
    
    return result_df
  
  def get_full_table(self, table_name, db_type=None, db_domain=None, db_name=None, username=None, password=None, jdbc_url=None):
    table_conn = self._get_connection(db_type, db_domain, db_name, username, password, jdbc_url)
    
    print(f"Getting full table '{table_name}' from Database")
    table_df = table_conn.option("dbtable", table_name).load()
    
    print("Showing table Spark Dataframe:")
    table_df.show()
    
    return table_df
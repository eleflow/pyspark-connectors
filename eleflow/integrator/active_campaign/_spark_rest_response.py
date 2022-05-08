from urllib import request

import requests
from pyspark.sql import SparkSession

class SparkRestResponse:
    
    def __init__(self, response: requests.Response) -> None:
        self.response = response
        
    def to_spark_dataframe(self):
        _SPARK = SparkSession.builder.getOrCreate()
        json = self.response.json()
        return _SPARK.read.json(_SPARK.sparkContext.parallelize([json['data']]))
    
    def to_json(self):
        return self.response.json()
    
    def to_text(self):
        return self.response.text

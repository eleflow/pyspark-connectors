import requests
from eleflow.converters.json_dataframe_converter import JSONDataFrameConverter

class SparkRestResponse:
    
    def __init__(self, response: requests.Response) -> None:
        self.response = response
        
    def to_spark_dataframe(self, key = None, schema = None):
        return JSONDataFrameConverter.convert(json=self.to_json(), key=key, schema=schema)
        
    def to_json(self):
        return self.response.json()
    
    def to_text(self):
        return self.response.text
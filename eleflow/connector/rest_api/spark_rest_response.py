import requests
from eleflow.converter.json_dataframe_converter import JSONDataFrameConverter

class SparkRestResponse:
    
    def __init__(self, url, method, data, headers) -> None:
        self.response = self.__make_request(url, method, data, headers)
        
    def to_spark_dataframe(self, key = None, schema = None):
        return JSONDataFrameConverter.convert(json=self.to_json(), key=key, schema=schema)
        
    def to_json(self):
        return self.response.json()
    
    def to_text(self):
        return self.response.text
    
    def __make_request(self, url, method, data, headers):
        if method == 'GET':
            return requests.get(url, headers=headers)
        elif method == 'POST':
            return requests.post(url, data=data, headers=headers)
        elif method == 'PUT':
            return requests.put(url, data=data, headers=headers)
        elif method == 'DELETE':
            return requests.delete(url, data=data, headers=headers)
        elif method == 'PATCH':
            return requests.patch(url, data=data, headers=headers)
        else:
            raise Exception('Method not supported')
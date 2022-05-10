from eleflow.converter.json_dataframe_converter import JSONDataFrameConverter

class CosmosDBDocument:
    
    def __init__(self, document):
        self.__doc__ = document
    
    def to_json(self):
        return list(self.__doc__)
    
    def to_spark_dataframe(self):
        return JSONDataFrameConverter.to_spark_dataframe(self.to_json())
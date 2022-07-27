from eleflow.converter.json_dataframe_converter import JSONDataFrameConverter

class CosmosDBDocument:
    
    def __init__(self, document):
        self.document = list(document)

    def to_json(self):
        return self.document
    
    def to_spark_dataframe(self, schema=None):
        return JSONDataFrameConverter.convert(self.to_json(), schema=schema)
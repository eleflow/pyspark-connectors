from pyspark.sql import SparkSession
from pyspark.sql.types import StructField, IntegerType, FloatType, StringType, StructType, BooleanType

class JSONDataFrameConverter:
    
    @classmethod
    def convert(cls, json, key = None, schema = None):
        _SPARK = SparkSession.builder.getOrCreate()
        json = json.get(key) if key else json
        if type(json) is not list:
            json = [json]
        if schema is None:
            schema = cls._create_schema_from_json(cls, json)
        return _SPARK.createDataFrame(_SPARK.sparkContext.parallelize(json), schema)

    def _create_schema_from_json(self, obj):
        struct_types = []
        for key, value in obj[0].items():
            try:
                if type(value) is int:
                    struct_types.append(StructField(key.lower().replace(' ', '_'), IntegerType(), True))
                elif type(value) is float:
                    struct_types.append(StructField(key.lower().replace(' ', '_'), FloatType(), True))
                elif type(value) is bool:
                    struct_types.append(StructField(key.lower().replace(' ', '_'), BooleanType(), True))
                else:
                    struct_types.append(StructField(key.lower().replace(' ', '_'), StringType(), True))
            except IndexError as ie:
                struct_types.append(StructField(key.lower().replace(' ', '_'), StringType(), True))

        return StructType(struct_types)
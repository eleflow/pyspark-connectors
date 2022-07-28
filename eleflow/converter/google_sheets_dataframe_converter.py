from pyspark.sql import SparkSession
from pyspark.sql.types import ArrayType, StructField, StructType, StringType, IntegerType, FloatType, BooleanType

import eleflow.utils.string_utils as string_utils

class GoogleSheetDataframeConverter:
    
    @classmethod
    def convert(cls, sheet_values):
        _SPARK = SparkSession.builder.getOrCreate()
        schema = cls.create_schema_from_values(sheet_values)
        sheet_values = cls.normalize_empty_columns(sheet_values, schema)
        rdd = _SPARK.sparkContext.parallelize(sheet_values[0:])
        return _SPARK.createDataFrame(rdd, schema)
        
    def create_schema_from_values(sheet_values):
        struct_types = []
        for idx, header in enumerate(sheet_values[0]):
            try:
                sample = sheet_values[1][idx]
                if type(sample) is int:
                    struct_types.append(StructField(string_utils.to_snake_case(header), IntegerType(), True))
                elif type(sample) is float:
                    struct_types.append(StructField(string_utils.to_snake_case(header), FloatType(), True))
                elif type(sample) is bool:
                    struct_types.append(StructField(string_utils.to_snake_case(header), BooleanType(), True))
                else:
                    struct_types.append(StructField(string_utils.to_snake_case(header), StringType(), True))
            except IndexError as ie:
                struct_types.append(StructField(string_utils.to_snake_case(header), StringType(), True))

        return StructType(struct_types)
    
    def normalize_empty_columns(values, schema):
        sheet_values = []
        for i in values[1:]:
            row_value = []
            for j in range(0, len(schema)):
                try:
                    row_value.append(i[j])
                except:
                    row_value.append(None)
            sheet_values.append(row_value)
        return sheet_values
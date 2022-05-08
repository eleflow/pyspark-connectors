import pyspark
from pyspark.sql import SparkSession
from pyspark.sql.types import ArrayType, StructField, StructType, StringType, IntegerType, FloatType, BooleanType

def _create_schema_from_values(sheet_values):
    struct_types = []
    for idx, header in enumerate(sheet_values[0]):
        try:
            sample = sheet_values[1][idx]
            if type(sample) is int:
                struct_types.append(StructField(header.lower().replace(' ', '_'), IntegerType(), True))
            elif type(sample) is float:
                struct_types.append(StructField(header.lower().replace(' ', '_'), FloatType(), True))
            elif type(sample) is bool:
                struct_types.append(StructField(header.lower().replace(' ', '_'), BooleanType(), True))
            else:
                struct_types.append(StructField(header.lower().replace(' ', '_'), StringType(), True))
        except IndexError as ie:
            struct_types.append(StructField(header.lower().replace(' ', '_'), StringType(), True))

    return StructType(struct_types)

def _create_dataframe_from_sheet_values(sheet_values):
    _SPARK = SparkSession.builder.getOrCreate()
    schema = _create_schema_from_values(sheet_values)
    sheet_values = _normalize_empty_columns(sheet_values, schema)
    rdd = _SPARK.sparkContext.parallelize(sheet_values[0:])
    return _SPARK.createDataFrame(rdd, schema)

def _normalize_empty_columns(values, schema):
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

def _parse_csv_list_to_json(values):
    values_dict = list()
    for val in values[1:]:
        item = dict()
        for idx, hdr in enumerate(values[0]):
            item[hdr] = val[idx]
        values_dict.append(item)
    return values_dict

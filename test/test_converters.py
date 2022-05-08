import unittest
from eleflow.converter.json_dataframe_converter import JSONDataFrameConverter

class TestJSONDataFrameConverter(unittest.TestCase):

    STARWARS_CHARS_LIST = [{'name': 'Darth Vader', 'age': 42, 'is_dark_side_star': True}, 
                        {'name': 'Luke Skywalker', 'age': 18, 'is_dark_side_star': False},
                        {'name': 'Obi-Wan Kenobi', 'age': 55, 'is_dark_side_star': False}]

    def test_convert_json_to_dataframe_without_key_value(self):
        json = self.STARWARS_CHARS_LIST
        df = JSONDataFrameConverter.convert(json)
        assert df.count() == 3
        
    def test_convert_json_to_dataframe_with_key_value(self):
        json = {'data': self.STARWARS_CHARS_LIST}
        df = JSONDataFrameConverter.convert(json, key='data')
        assert df.count() == 3
    
if __name__ == '__main__':
    unittest.main()
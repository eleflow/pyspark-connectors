from eleflow.converter.google_sheets_dataframe_converter import GoogleSheetDataframeConverter

class GoogleSheet:
    
    def __init__(self, google_sheet) -> None:
        self._sheet = google_sheet.execute()
        
    def get_values(self):
        return self._sheet.get('values', [])
    
    def to_spark_dataframe(self):
        return GoogleSheetDataframeConverter.convert(self.get_values())
    
    def to_json(self):
        values_dict = list()
        for val in self.get_values[1:]:
            item = dict()
            for idx, hdr in enumerate(self.get_values[0]):
                item[hdr] = val[idx]
            values_dict.append(item)
        return values_dict
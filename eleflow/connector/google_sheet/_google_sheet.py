import google_sheet._utils as _utils

class GoogleSheet:
    
    def __init__(self, google_sheet) -> None:
        self._sheet = google_sheet.execute()
        self._json_values = _utils._parse_csv_list_to_json(self.get_values())
        
    def get_values(self):
        return self._sheet.get('values', [])
    
    def get_values_spark_dataframe(self):
        return _utils._create_dataframe_from_sheet_values(self.get_values())
    
    def get_values_json(self):
        return self._json_values
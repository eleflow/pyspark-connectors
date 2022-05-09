from .google_sheet import GoogleSheet

class GoogleSpreadsheet():
    
    def __init__(self, google_spreadsheet, google_service, spreadsheet_id) -> None:
        self._spreadsheet = google_spreadsheet
        self._service = google_service
        self._spreadsheet_id = spreadsheet_id
        
    def get_sheets_names(self) -> list:
        return [x['properties']['title'] for x in self._spreadsheet['sheets']]

    def get_sheet_from_name(self, sheet_name: str) -> GoogleSheet:
        return GoogleSheet(self._service.spreadsheets().values().get(spreadsheetId=self._spreadsheet_id, range=sheet_name))
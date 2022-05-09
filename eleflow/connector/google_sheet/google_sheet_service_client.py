from .google_spreadsheet import GoogleSpreadsheet

from googleapiclient.discovery import build

class GoogleSheetServiceClient():
    
    def __init__(self, google_crendentials, scopes) -> None:
        self._google_crendentials = google_crendentials
        self._scopes = scopes
        
        self._service = build('sheets', 'v4', credentials=self._google_crendentials)
        
    def get_spreadsheet(self, spreadsheet_id: str) -> GoogleSpreadsheet:
        _google_spreadsheet = self._service.spreadsheets().get(spreadsheetId=spreadsheet_id).execute()
        return GoogleSpreadsheet(_google_spreadsheet, self._service, spreadsheet_id)
from eleflow.__builder__ import EleflowAbstractConnectionBuilder
from .google_sheet_service_client import GoogleSheetServiceClient

from google.oauth2.service_account import Credentials
from google.auth import _service_account_info

class GoogleSheetConnection(EleflowAbstractConnectionBuilder):
    
    _DEFAULT_SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']
    
    def __init__(self, credentials, scopes) -> None:
        self._credentials = credentials
        self._scopes = scopes
        
    def add_scope(self, scope: str):
        self._scopes.append(scope)
        return self.__class__(
            credentials = self._credentials,
            scopes = self._scopes
        )
  
    def get_service_client(self) -> GoogleSheetServiceClient:
        return GoogleSheetServiceClient(self._credentials, self._scopes)
    
    @classmethod
    def from_credentials_info(cls, info):
        signer = _service_account_info.from_dict(info, require=["client_email", "token_uri"])
        return cls(
            credentials = Credentials(signer, service_account_email=info["client_email"], token_uri=info["token_uri"], project_id=info.get("project_id")),
            scopes = cls._DEFAULT_SCOPES
        )
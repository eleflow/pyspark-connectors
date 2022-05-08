import os
from pipe_drive._pipe_drive_service_client import PipeDriveServiceClient

class PipeDriveConnection():

    def __init__(self, token_api, base_url) -> None:
        self._TOKEN_API = token_api
        self._BASE_URL = base_url

    @classmethod
    def v1_from_token_api(cls, token_api):
        return cls(
            token_api, 
            os.getenv('BASE_URL_V1', 'https://api.pipedrive.com/v1')
        )

    def get_service_client(self):
        return PipeDriveServiceClient('api_token', self._TOKEN_API, self._BASE_URL)
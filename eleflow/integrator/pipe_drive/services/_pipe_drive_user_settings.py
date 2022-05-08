

from rest_api._rest_base import Restbase
from rest_api._spark_rest_response import SparkRestResponse


class PipeDriveUserSettings(Restbase):
    
    def __init__(self, url_base,api_token_key, api_token_value) -> None:
        super().__init__(url_base+'/userSettings/',api_token_key, api_token_value)
    
    def list_settings_of_an_authorized_user(self):
        """Lists settings of an authorized user.
        
        Returns:
            SparkRestResponse: _description_
        """
        return self.get()
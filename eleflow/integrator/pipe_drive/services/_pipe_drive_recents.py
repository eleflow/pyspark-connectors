

from rest_api._rest_base import Restbase
from rest_api._spark_rest_response import SparkRestResponse


class PipeDriveRecents(Restbase):
    
    def __init__(self, url_base,api_token_key, api_token_value) -> None:
        super().__init__(url_base+'/recents/',api_token_key, api_token_value)
    
    def get_recents(self, **kwargs):
        """Gets recents.
        
        Args:
            kwargs (dict): _description_
        
        Returns:
            SparkRestResponse: _description_
        """
        return self.get(**kwargs)
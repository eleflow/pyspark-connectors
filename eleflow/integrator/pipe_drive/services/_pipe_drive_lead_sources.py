

from rest_api._rest_base import Restbase
from rest_api._spark_rest_response import SparkRestResponse


class PipeDriveLeadSources(Restbase):
    
    def __init__(self, url_base,api_token_key, api_token_value) -> None:
        super().__init__(url_base+'/leadSources/',api_token_key, api_token_value)
    
    def get_all_lead_sources(self):
        """Gets all lead sources.
        
        Returns:
            SparkRestResponse: _description_
        """
        return self.get()
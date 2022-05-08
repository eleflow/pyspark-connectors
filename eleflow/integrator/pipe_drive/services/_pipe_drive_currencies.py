from eleflow.connector.rest_api.rest_base import Restbase
from eleflow.connector.rest_api.spark_rest_response import SparkRestResponse

class PipeDriveCurrencies(Restbase):
    
    def __init__(self, url_base,api_token_key, api_token_value) -> None:
        super().__init__(url_base+'/currencies/',api_token_key, api_token_value)
    
    def get_all_supported_currencies(self, term):
        """Gets all supported currencies.
        
        Args:
            term (str): (Required) The search term.
        
        Returns:
            SparkRestResponse: _description_
        """
        return self.get(**{'term':term})
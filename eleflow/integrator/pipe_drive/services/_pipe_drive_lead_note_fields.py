from eleflow.connector.rest_api.rest_base import Restbase
from eleflow.connector.rest_api.spark_rest_response import SparkRestResponse

class PipeDriveNoteFields(Restbase):
    
    def __init__(self, url_base,api_token_key, api_token_value) -> None:
        super().__init__(url_base+'/noteFields/',api_token_key, api_token_value)
    
    def get_all_note_fields(self):
        """Gets all note fields.
        
        Returns:
            SparkRestResponse: _description_
        """
        return self.get()
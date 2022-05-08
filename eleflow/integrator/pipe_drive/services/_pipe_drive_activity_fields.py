from eleflow.connector.rest_api.rest_base import Restbase
from eleflow.connector.rest_api.spark_rest_response import SparkRestResponse

class PipeDriveActivityFields(Restbase):
    
    def __init__(self, url_base,api_token_key, api_token_value) -> None:
        super().__init__(url_base+'/activityFields/',api_token_key, api_token_value)
    
    def get_all_activity_fields(self):
        """Gets all activity fields.
        
        Returns:
            SparkRestResponse: _description_
        """
        return self.get()
from eleflow.connector.rest_api.rest_base import Restbase
from eleflow.connector.rest_api.spark_rest_response import SparkRestResponse

class PipeDriveGlobalMessages(Restbase):
    
    def __init__(self, url_base,api_token_key, api_token_value) -> None:
        super().__init__(url_base+'/globalMessages/',api_token_key, api_token_value)
    
    def get_global_messages(self, **kwargs):
        """Returns all global messages.
        
        Args:
            start (int): The start offset for the returned items
            limit (int): The maximum number of items to return
        
        Returns:
            SparkRestResponse: _description_
        """
        return self.get(**kwargs)

    def dismiss_a_global_message(self, id):
        """Dismisses a global message.
        
        Args:
            id (int): The ID of the global message to dismiss
        
        Returns:
            SparkRestResponse: _description_
        """
        return self.delete(*(id))
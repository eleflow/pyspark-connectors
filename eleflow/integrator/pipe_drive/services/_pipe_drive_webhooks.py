from eleflow.connector.rest_api.rest_base import Restbase
from eleflow.connector.rest_api.spark_rest_response import SparkRestResponse

class PipeDriveWebhooks(Restbase):
    
    def __init__(self, url_base,api_token_key, api_token_value) -> None:
        super().__init__(url_base+'/webhooks/',api_token_key, api_token_value)
    
    def get_all_webhooks(self):
        """Gets all webhooks.
        
        Returns:
            SparkRestResponse: _description_
        """
        return self.get()
    
    def create_a_new_webhook(self, data):
        """Creates a new webhook.
        
        Args:
            data (dict): (Required) The data to update.
        
        Returns:
            SparkRestResponse: _description_
        """
        return self.post(data)

    def delete_existing_webhook(self, id):
        """Deletes an existing webhook.
        
        Args:
            id (int): (Required) The ID of the webhook.
        
        Returns:
            SparkRestResponse: _description_
        """
        return self.delete(*(id))
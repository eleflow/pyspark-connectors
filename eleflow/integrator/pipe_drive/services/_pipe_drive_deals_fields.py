from eleflow.connector.rest_api.rest_base import Restbase
from eleflow.connector.rest_api.spark_rest_response import SparkRestResponse

class PipeDriveDealsFields(Restbase):
    
    def __init__(self, url_base,api_token_key, api_token_value) -> None:
        super().__init__(url_base+'/dealFields/',api_token_key, api_token_value)
    
    def get_one_deal_field(self, id):
        """Returns a single deal field.
        
        Args:
            id (int): The ID of the deal field to return
            
        Returns:
            SparkRestResponse: _description_
        """
        return self.get(*(id))

    def delete_a_deal_field(self, id):
        """Deletes a deal field.
        
        Args:
            id (int): The ID of the deal field to delete
            
        Returns:
            SparkRestResponse: _description_
        """
        return self.delete(*(id))

    def update_a_deal_field(self, data, id):
        """Updates a deal field.
        
        Args:
            data (json): The data to add the deal field with
            id (int): (Required) The ID of the deal field
            
        Returns:
            SparkRestResponse: _description_
        """
        return self.put(data, *(id))

    def get_all_deal_fields(self, **kwargs):
        """Returns all deal fields.
        
        Args:
            start (int): The start offset for the returned items
            limit (int): The maximum number of items to return

        Returns:
            SparkRestResponse: _description_
        """
        return self.get(**kwargs)

    def add_new_deal_field(self, data):
        """Adds a new deal field.
        
        Args:
            data (json): The data to add the deal field with
            
        Returns:
            SparkRestResponse: _description_
        """
        return self.post(data)

    def delete_multiple_deal_fields_in_bulk(self, ids):
        """Deletes multiple deal fields.
        
        Args:
            ids (list): The IDs of the deal fields to delete
            
        Returns:
            SparkRestResponse: _description_
        """
        return self.delete(**{'ids':ids})
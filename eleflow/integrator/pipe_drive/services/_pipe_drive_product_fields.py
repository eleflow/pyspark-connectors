from eleflow.connector.rest_api.rest_base import Restbase
from eleflow.connector.rest_api.spark_rest_response import SparkRestResponse

class PipeDriveProductFields(Restbase):
    
    def __init__(self, url_base,api_token_key, api_token_value) -> None:
        super().__init__(url_base+'/productFields/',api_token_key, api_token_value)
    
    def delete_a_product_field(self, id):
        """Deletes a product field.
        
        Args:
            id (int): (Required) The ID of the product field.
        
        Returns:
            SparkRestResponse: _description_
        """
        return self.delete(*(id))

    def get_one_product_field(self, id):
        """Gets one product field.
        
        Args:
            id (int): (Required) The ID of the product field.
        
        Returns:
            SparkRestResponse: _description_
        """
        return self.get(*(id))

    def update_a_product_field(self, id, data):
        """Updates a product field.
        
        Args:
            id (int): (Required) The ID of the product field.
            data (dict): (Required) The data to update.
        
        Returns:
            SparkRestResponse: _description_
        """
        return self.put(data, *(id))

    def get_all_product_fields(self, **kwargs):
        """Gets all product fields.
        
        Returns:
            SparkRestResponse: _description_
        """
        return self.get(*('all'), **kwargs)

    def delete_multiple_product_field_in_bulk(self, ids):
        """Deletes multiple product field in bulk.
        
        Args:
            ids (list): (Required) The IDs of the product fields.
        
        Returns:
            SparkRestResponse: _description_
        """
        return self.delete(**{'ids':ids})
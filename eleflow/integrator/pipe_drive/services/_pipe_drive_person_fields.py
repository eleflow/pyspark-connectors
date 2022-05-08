from eleflow.connector.rest_api.rest_base import Restbase
from eleflow.connector.rest_api.spark_rest_response import SparkRestResponse

class PipeDrivePersonFields(Restbase):
    
    def __init__(self, url_base,api_token_key, api_token_value) -> None:
        super().__init__(url_base+'/personFields/',api_token_key, api_token_value)
    
    def get_one_person_field(self, id):
        """Gets one person field.
        
        Args:
            id (int): (Required) The ID of the person field.
        
        Returns:
            SparkRestResponse: _description_
        """
        return self.get(*(id))

    def delete_a_person_field(self, id):
        """Deletes a person field.
        
        Args:
            id (int): (Required) The ID of the person field.
        
        Returns:
            SparkRestResponse: _description_
        """
        return self.delete(*(id))

    def update_a_person_field(self, id, data):
        """Updates a person field.
        
        Args:
            id (int): (Required) The ID of the person field.
            data (dict): (Required) The data to update.
        
        Returns:
            SparkRestResponse: _description_
        """
        return self.put(data, *(id))

    def get_all_person_fields(self, **kwargs):
        """Gets all person fields.
        
        Returns:
            SparkRestResponse: _description_
        """
        return self.get(**kwargs)

    def add_a_new_person_field(self, data):
        """Adds a new person field.
        
        Args:
            data (dict): (Required) The data to add.
        
        Returns:
            SparkRestResponse: _description_
        """
        return self.post(data)

    def delete_multiple_person_fields_in_bulk(self, ids):
        """Deletes multiple person fields in bulk.
        
        Args:
            ids (str): (Required) The comma-separated field IDs to delete
        
        Returns:
            SparkRestResponse: _description_
        """
        return self.delete(**{'ids':ids})
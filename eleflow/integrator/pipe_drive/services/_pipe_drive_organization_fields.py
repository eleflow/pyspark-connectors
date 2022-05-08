from eleflow.connector.rest_api.rest_base import Restbase
from eleflow.connector.rest_api.spark_rest_response import SparkRestResponse

class PipeDriveOrganizationFields(Restbase):
    
    def __init__(self, url_base,api_token_key, api_token_value) -> None:
        super().__init__(url_base+'/organizationFields/',api_token_key, api_token_value)
    
    def get_one_organization_field(self, id):
        """Gets one organization field.
        
        Args:
            id (int): (Required) The ID of the organization field.
        
        Returns:
            SparkRestResponse: _description_
        """
        return self.get(*(id,))

    def delete_an_organization_field(self, id):
        """Deletes an organization field.
        
        Args:
            id (int): (Required) The ID of the organization field.
        
        Returns:
            SparkRestResponse: _description_
        """
        return self.delete(*(id,))

    def update_an_organization_field(self, id, data):
        """Updates an organization field.
        
        Args:
            id (int): (Required) The ID of the organization field.
            data (dict): (Required) The data to update.
        
        Returns:
            SparkRestResponse: _description_
        """
        return self.put(data, *(id,))

    def get_all_organization_fields(self, **kwargs):
        """Gets all organization fields.
        
        Args:
            **kwargs: _description_
        
        Returns:
            SparkRestResponse: _description_
        """
        return self.get(**kwargs)

    def add_a_new_organization_field(self, data):
        """Adds a new organization field.
        
        Args:
            data (dict): (Required) The data to add.
        
        Returns:
            SparkRestResponse: _description_
        """
        return self.post(data)

    def delete_multiple_organization_fields(self, ids):
        """Deletes multiple organization fields.
        
        Args:
            ids (list): (Required) The IDs of the organization fields.
        
        Returns:
            SparkRestResponse: _description_
        """
        return self.delete(**{'ids':ids})
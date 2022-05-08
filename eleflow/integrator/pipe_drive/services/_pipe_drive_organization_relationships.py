from eleflow.connector.rest_api.rest_base import Restbase
from eleflow.connector.rest_api.spark_rest_response import SparkRestResponse

class PipeDriveOrganizationRelationships(Restbase):
    
    def __init__(self, url_base,api_token_key, api_token_value) -> None:
        super().__init__(url_base+'/organizationRelationships/',api_token_key, api_token_value)
    
    def delete_an_organization_relationship(self, id):
        """Deletes an organization relationship.
        
        Args:
            id (int): (Required) The ID of the organization relationship.
        
        Returns:
            SparkRestResponse: _description_
        """
        return self.delete(*(id))

    def get_one_organization_relationship(self, id, **kwargs):
        """Gets one organization relationship.
        
        Args:
            id (int): (Required) The ID of the organization relationship.
        
        Returns:
            SparkRestResponse: _description_
        """
        return self.get(*(id), **kwargs)

    def update_an_organization_relationship(self, id, data):
        """Updates an organization relationship.
        
        Args:
            id (int): (Required) The ID of the organization relationship.
            data (dict): (Required) The data to update.
        
        Returns:
            SparkRestResponse: _description_
        """
        return self.put(data, *(id))

    def get_all_relationships_for_an_organization(self, **kwargs):
        """Gets all relationships for an organization.
                
        Returns:
            SparkRestResponse: _description_
        """
        return self.get(**kwargs)

    def create_an_organization_relationship(self, data):
        """Creates an organization relationship.
        
        Args:
            data (dict): (Required) The data to create.
        
        Returns:
            SparkRestResponse: _description_
        """
        return self.post(data)
from eleflow.connector.rest_api.rest_base import Restbase
from eleflow.connector.rest_api.spark_rest_response import SparkRestResponse

class PipeDriveRoles(Restbase):
    
    def __init__(self, url_base,api_token_key, api_token_value) -> None:
        super().__init__(url_base+'/roles/',api_token_key, api_token_value)
    
    def delete_a_role_assignment(self, id):
        """Deletes a role assignment.
        
        Args:
            id (int): (Required) The ID of the role assignment.
        
        Returns:
            SparkRestResponse: _description_
        """
        return self.delete(*(id,'assignments'))

    def list_role_assignments(self, id, **kwargs):
        """Lists all role assignments.
        
        Args:
            id (int): (Required) The ID of the role.
        
        Returns:
            SparkRestResponse: _description_
        """
        return self.get(*(id,'assignments'), **kwargs)

    def add_a_role_assignment(self, id, data):
        """Adds a role assignment.
        
        Args:
            id (int): (Required) The ID of the role.
            data (dict): (Required) The data to add.
        
        Returns:
            SparkRestResponse: _description_
        """
        return self.post(data, *(id,'assignments'))

    def list_role_settings(self, id, **kwargs):
        """Lists all role settings.
        
        Args:
            id (int): (Required) The ID of the role.
        
        Returns:
            SparkRestResponse: _description_
        """
        return self.get(*(id,'settings'), **kwargs)

    def add_or_updates_role_setting(self, id, data):
        """Adds or updates a role setting.
        
        Args:
            id (int): (Required) The ID of the role.
            data (dict): (Required) The data to add.
        
        Returns:
            SparkRestResponse: _description_
        """
        return self.post(data, *(id,'settings'))

    def delete_a_role(self, id):
        """Deletes a role.
        
        Args:
            id (int): (Required) The ID of the role.
        
        Returns:
            SparkRestResponse: _description_
        """
        return self.delete(*(id))

    def get_one_role(self, id):
        """Gets one role.
        
        Args:
            id (int): (Required) The ID of the role.
        
        Returns:
            SparkRestResponse: _description_
        """
        return self.get(*(id))

    def update_a_role_details(self, id, data):
        """Updates a role.
        
        Args:
            id (int): (Required) The ID of the role.
            data (dict): (Required) The data to add.
        
        Returns:
            SparkRestResponse: _description_
        """
        return self.put(data, *(id))

    def list_role_sub_roles(self, id, **kwargs):
        """Lists all sub roles.
        
        Args:
            id (int): (Required) The ID of the role.
        
        Returns:
            SparkRestResponse: _description_
        """
        return self.get(*(id,'sub_roles'), **kwargs)

    def get_all_roles(self, **kwargs):
        """Gets all roles.
        
        Returns:
            SparkRestResponse: _description_
        """
        return self.get('', **kwargs)

    def add_a_role(self, data):
        """Adds a role.
        
        Args:
            data (dict): (Required) The data to add.
        
        Returns:
            SparkRestResponse: _description_
        """
        return self.post(data)
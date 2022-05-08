from eleflow.connector.rest_api.rest_base import Restbase
from eleflow.connector.rest_api.spark_rest_response import SparkRestResponse

class PipeDriveUsers(Restbase):
    
    def __init__(self, url_base,api_token_key, api_token_value) -> None:
        super().__init__(url_base+'/users/',api_token_key, api_token_value)
    
    def delete_a_role_assignment(self, id, role_id):
        """Deletes a role assignment.
        
        Args:
            id (int): (Required) The ID of the user.
            role_id (int): (Required) The ID of the role.
        
        Returns:
            SparkRestResponse: _description_
        """
        return self.delete(*(id,'roleAssignments'), data={'role_id':role_id})

    def list_role_assingments(self, id, **kwargs):
        """Lists role assignments.
        
        Args:
            id (int): (Required) The ID of the user.
        
        Returns:
            SparkRestResponse: _description_
        """
        return self.get(*(id,'roleAssignments'), **kwargs)

    def add_role_assignment(self, id, data):
        """Adds a role assignment.
        
        Args:
            id (int): (Required) The ID of the user.
            data (dict): (Required) The data to update.
        
        Returns:
            SparkRestResponse: _description_
        """
        return self.post(data, *(id,'roleAssignments'))

    def get_one_user(self, id):
        """Gets a single user.
        
        Args:
            id (int): (Required) The ID of the user.
        
        Returns:
            SparkRestResponse: _description_
        """
        return self.get(*(id))

    def update_user_details(self, id, data):
        """Updates a user.
        
        Args:
            id (int): (Required) The ID of the user.
            data (dict): (Required) The data to update.
        
        Returns:
            SparkRestResponse: _description_
        """
        return self.put(data, *(id))

    def list_followers_of_a_user(self, id):
        """Lists followers of a user.
        
        Args:
            id (int): (Required) The ID of the user.
        
        Returns:
            SparkRestResponse: _description_
        """
        return self.get(*(id,'followers'))

    def list_user_permissions(self, id):
        """Lists user permissions.
        
        Args:
            id (int): (Required) The ID of the user.
        
        Returns:
            SparkRestResponse: _description_
        """
        return self.get(*(id,'permissions'))

    def list_user_role_settings(self, id):
        """Lists user role settings.
        
        Args:
            id (int): (Required) The ID of the user.
        
        Returns:
            SparkRestResponse: _description_
        """
        return self.get(*(id,'roleSettings'))

    def get_all_users(self):
        """Gets all users.
        
        Args:
        
        Returns:
            SparkRestResponse: _description_
        """
        return self.get()

    def add_new_user(self, data):
        """Adds a new user.
        
        Args:
            data (dict): (Required) The data to update.
        
        Returns:
            SparkRestResponse: _description_
        """
        return self.post(data)

    def find_users_by_name(self, **kwargs):
        """Finds users by name.
        
        Args:
            name (str): (Required) The name of the user.
        
        Returns:
            SparkRestResponse: _description_
        """
        return self.get('find', **kwargs)

    def get_current_user_data(self):
        """Gets current user data.
        
        Args:
        
        Returns:
            SparkRestResponse: _description_
        """
        return self.get('me')
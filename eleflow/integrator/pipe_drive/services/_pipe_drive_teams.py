from eleflow.connector.rest_api.rest_base import Restbase
from eleflow.connector.rest_api.spark_rest_response import SparkRestResponse

class PipeDriveTeams(Restbase):
    
    def __init__(self, url_base,api_token_key, api_token_value) -> None:
        super().__init__(url_base+'/teams/',api_token_key, api_token_value)
    
    def get_all_users_in_a_team(self, id):
        """Gets all users in a team.
        
        Args:
            id (int): (Required) The ID of the team.
        
        Returns:
            SparkRestResponse: _description_
        """
        return self.get(*(id,'users'))

    def add_users_to_a_team(self, id, data):
        """Adds users to a team.
        
        Args:
            id (int): (Required) The ID of the team.
            data (dict): (Required) The data to update.
        
        Returns:
            SparkRestResponse: _description_
        """
        return self.post(data, *(id,'users'))
    
    def get_a_single_team(self, id, **kwargs):
        """Gets a single team.
        
        Args:
            id (int): (Required) The ID of the team.
        
        Returns:
            SparkRestResponse: _description_
        """
        return self.get(*(id), **kwargs)

    def update_a_team(self, id, data):
        """Updates a team.
        
        Args:
            id (int): (Required) The ID of the team.
            data (dict): (Required) The data to update.
        
        Returns:
            SparkRestResponse: _description_
        """
        return self.put(data, *(id))

    def get_all_teams(self, **kwargs):
        """Gets all teams.
        
        Args:
        
        Returns:
            SparkRestResponse: _description_
        """
        return self.get(**kwargs)

    def add_a_new_team(self, data):
        """Adds a new team.
        
        Args:
            data (dict): (Required) The data to update.
        
        Returns:
            SparkRestResponse: _description_
        """
        return self.post(data)

    def get_all_teams_of_a_user(self, id, **kwargs):
        """Gets all teams of a user.
        
        Args:
            id (int): (Required) The ID of the user.
        
        Returns:
            SparkRestResponse: _description_
        """
        return self.get(*('user',id), **kwargs)
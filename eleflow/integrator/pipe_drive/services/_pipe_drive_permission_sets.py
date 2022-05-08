from eleflow.connector.rest_api.rest_base import Restbase
from eleflow.connector.rest_api.spark_rest_response import SparkRestResponse

class PipeDrivePermissionSets(Restbase):
    
    def __init__(self, url_base,api_token_key, api_token_value) -> None:
        super().__init__(url_base+'/permissionSets/',api_token_key, api_token_value)
    
    def get_one_permission_set(self, id):
        """Gets one permission set.
        
        Args:
            id (int): (Required) The ID of the permission set.
        
        Returns:
            SparkRestResponse: _description_
        """
        return self.get(*(id))

    def list_perssion_set_assignments(self, id, **kwargs):
        """Lists perssion set assignments.
        
        Args:
            id (int): (Required) The ID of the permission set.
        
        Returns:
            SparkRestResponse: _description_
        """
        return self.get(*(id, 'assignments'), **kwargs)

    def get_all_permission_sets(self):
        """Gets all permission sets.
        
        Returns:
            SparkRestResponse: _description_
        """
        return self.get()
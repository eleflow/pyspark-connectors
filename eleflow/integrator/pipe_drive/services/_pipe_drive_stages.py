from eleflow.connector.rest_api.rest_base import Restbase
from eleflow.connector.rest_api.spark_rest_response import SparkRestResponse

class PipeDriveStages(Restbase):
    
    def __init__(self, url_base,api_token_key, api_token_value) -> None:
        super().__init__(url_base+'/stages/',api_token_key, api_token_value)
    
    def delete_a_stage(self, id):
        """Deletes a stage.
        
        Args:
            id (int): (Required) The ID of the stage.
        
        Returns:
            SparkRestResponse: _description_
        """
        return self.delete(*(id))

    def get_one_stage(self, id):
        """Gets one stage.
        
        Args:
            id (int): (Required) The ID of the stage.
        
        Returns:
            SparkRestResponse: _description_
        """
        return self.get(*(id))

    def update_stage_details(self, id, data):
        """Updates a stage's details.
        
        Args:
            id (int): (Required) The ID of the stage.
            data (dict): (Required) The data to update.
        
        Returns:
            SparkRestResponse: _description_
        """
        return self.put(data, *(id))

    def get_deals_is_a_stage(self, id, **kwargs):
        """Gets all deals that are a stage.
        
        Args:
            id (int): (Required) The ID of the stage.
        
        Returns:
            SparkRestResponse: _description_
        """
        return self.get(*(id,'deals'), **kwargs)

    def delete_multiple_stages_in_bulk(self, ids):
        """Deletes multiple stages in bulk.
        
        Args:
            ids (list): (Required) The comma-separated stage IDs to delete
        
        Returns:
            SparkRestResponse: _description_
        """
        return self.delete(**{'ids':ids})

    def get_all_stages(self, **kwargs):
        """Gets all stages.
        
        Returns:
            SparkRestResponse: _description_
        """
        return self.get('', **kwargs)

    def add_a_stage(self, data):
        """Adds a stage.
        
        Args:
            data (dict): (Required) The data to add.
        
        Returns:
            SparkRestResponse: _description_
        """
        return self.post(data)
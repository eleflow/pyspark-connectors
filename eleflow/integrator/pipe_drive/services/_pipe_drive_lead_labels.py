from eleflow.connector.rest_api.rest_base import Restbase
from eleflow.connector.rest_api.spark_rest_response import SparkRestResponse

class PipeDriveLeadLabels(Restbase):
    
    def __init__(self, url_base,api_token_key, api_token_value) -> None:
        super().__init__(url_base+'/leadLabels/',api_token_key, api_token_value)
    
    def update_a_lead_label(self, id, data):
        """Updates a lead label.
        
        Args:
            id (int): (Required) The ID of the lead label.
            data (dict): (Required) The data to update.
        
        Returns:
            SparkRestResponse: _description_
        """
        return self.patch(data, *(id))
    
    def delete_a_lead_label(self, id):
        """Deletes a lead label.
        
        Args:
            id (int): (Required) The ID of the lead label.
        
        Returns:
            SparkRestResponse: _description_
        """
        return self.delete(*(id))

    def get_all_lead_labels(self):
        """Gets all lead labels.
        
        Returns:
            SparkRestResponse: _description_
        """
        return self.get()

    def add_a_lead_label(self, data):
        """Adds a lead label.
        
        Args:
            data (dict): (Required) The data to add.
        
        Returns:
            SparkRestResponse: _description_
        """
        return self.post(data)
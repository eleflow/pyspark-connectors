from eleflow.connector.rest_api.rest_base import Restbase
from eleflow.connector.rest_api.spark_rest_response import SparkRestResponse

class PipeDriveLeads(Restbase):
    
    def __init__(self, url_base,api_token_key, api_token_value) -> None:
        super().__init__(url_base+'/leads/',api_token_key, api_token_value)
    
    def get_one_lead(self, id):
        """Gets one lead.
        
        Args:
            id (int): (Required) The ID of the lead.
        
        Returns:
            SparkRestResponse: _description_
        """
        return self.get(*(id))

    def update_a_lead(self, id, data):
        """Updates a lead.
        
        Args:
            id (int): (Required) The ID of the lead.
            data (dict): (Required) The data to update.
        
        Returns:
            SparkRestResponse: _description_
        """
        return self.patch(data, *(id))

    def delete_a_lead(self, id):
        """Deletes a lead.
        
        Args:
            id (int): (Required) The ID of the lead.
        
        Returns:
            SparkRestResponse: _description_
        """
        return self.delete(*(id))

    def get_all_leads(self, **kwargs):
        """Gets all leads.
        
        Returns:
            SparkRestResponse: _description_
        """
        return self.get(**kwargs)

    def add_a_lead(self, data):
        """Adds a lead.
        
        Args:
            data (dict): (Required) The data to add.
        
        Returns:
            SparkRestResponse: _description_
        """
        return self.post(data)
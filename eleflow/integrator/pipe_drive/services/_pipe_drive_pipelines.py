from eleflow.connector.rest_api.rest_base import Restbase
from eleflow.connector.rest_api.spark_rest_response import SparkRestResponse

class PipeDrivePipelines(Restbase):
    
    def __init__(self, url_base,api_token_key, api_token_value) -> None:
        super().__init__(url_base+'/pipelines/',api_token_key, api_token_value)
    
    def delete_a_pipeline(self, id):
        """Deletes a pipeline.
        
        Args:
            id (int): (Required) The ID of the pipeline.
        
        Returns:
            SparkRestResponse: _description_
        """
        return self.delete(*(id))

    def get_one_pipeline(self, id):
        """Gets one pipeline.
        
        Args:
            id (int): (Required) The ID of the pipeline.
        
        Returns:
            SparkRestResponse: _description_
        """
        return self.get(*(id))

    def update_a_pipeline(self, id, data):
        """Updates a pipeline.
        
        Args:
            id (int): (Required) The ID of the pipeline.
            data (dict): (Required) The data to update.
        
        Returns:
            SparkRestResponse: _description_
        """
        return self.put(data, *(id))

    def get_deals_conversion_rates_in_pipe_drive(self, id, **kwargs):
        """Gets deals conversion rates in pipe drive.
        
        Args:
            id (int): (Required) The ID of the pipeline.
        
        Returns:
            SparkRestResponse: _description_
        """
        return self.get(*(id, 'conversion_statistics'), **kwargs)

    def get_deals_in_a_pipeline(self, id, **kwargs):
        """Gets deals in a pipeline.
        
        Args:
            id (int): (Required) The ID of the pipeline.
        
        Returns:
            SparkRestResponse: _description_
        """
        return self.get(*(id, 'deals'), **kwargs)

    def get_deals_movementes_in_a_pipeline(self, id, **kwargs):
        """Gets deals movementes in a pipeline.
        
        Args:
            id (int): (Required) The ID of the pipeline.
        
        Returns:
            SparkRestResponse: _description_
        """
        return self.get(*(id, 'movement_statistics'), **kwargs)

    def get_all_pipelines(self):
        """Gets all pipelines.
        
        Returns:
            SparkRestResponse: _description_
        """
        return self.get()

    def add_a_new_pipeline(self, data):
        """Adds a new pipeline.
        
        Args:
            data (dict): (Required) The data to add.
        
        Returns:
            SparkRestResponse: _description_
        """
        return self.post(data)
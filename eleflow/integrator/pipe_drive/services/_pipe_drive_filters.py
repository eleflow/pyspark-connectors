from eleflow.connector.rest_api.rest_base import Restbase
from eleflow.connector.rest_api.spark_rest_response import SparkRestResponse

class PipeDriveFilters(Restbase):
    
    def __init__(self, url_base,api_token_key, api_token_value) -> None:
        super().__init__(url_base+'/filters/',api_token_key, api_token_value)
    
    def delete_a_filter(self, id):
        """Deletes a filter.
        
        Args:
            id (int): The ID of the filter to delete
            
        Returns:
            SparkRestResponse: _description_
        """
        return self.delete(*(id))

    def get_one_filter(self, id):
        """Returns a single filter.
        
        Args:
            id (int): The ID of the filter to return
            
        Returns:
            SparkRestResponse: _description_
        """
        return self.get(*(id))

    def update_filter(self, data, id):
        """Updates a filter.
        
        Args:
            data (json): The data to add the filter with
            id (int): (Required) The ID of the filter
            
        Returns:
            SparkRestResponse: _description_
        """
        return self.put(data, *(id))

    def delete_multiple_filters_in_bulk(self, ids):
        """Deletes multiple filters in bulk.
        
        Args:
            ids (list): The IDs of the filters to delete
            
        Returns:
            SparkRestResponse: _description_
        """
        return self.delete(**{'ids': ids})

    def get_all_filters(self, **kwargs):
        """Returns all filters.
        
        Args:
            start (int): The start offset for the returned items
            limit (int): The maximum number of items to return
            
        Returns:
            SparkRestResponse: _description_
        """
        return self.get(**kwargs)

    def add_new_filter(self, data):
        """Adds a new filter.
        
        Args:
            data (json): The data to add the filter with
            
        Returns:
            SparkRestResponse: _description_
        """
        return self.post(data)

    def get_all_filter_helpers(self):
        """Returns all filter helpers.
        
        Args:
            start (int): The start offset for the returned items
            limit (int): The maximum number of items to return
            
        Returns:
            SparkRestResponse: _description_
        """
        return self.get(*('helpers'))
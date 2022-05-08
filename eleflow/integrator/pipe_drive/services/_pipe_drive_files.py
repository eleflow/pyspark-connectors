from eleflow.connector.rest_api.rest_base import Restbase
from eleflow.connector.rest_api.spark_rest_response import SparkRestResponse

class PipeDriveFiles(Restbase):
    
    def __init__(self, url_base,api_token_key, api_token_value) -> None:
        super().__init__(url_base+'/files/',api_token_key, api_token_value)
    
    def delete_a_file(self, id):
        """Deletes a file.
        
        Args:
            id (int): The ID of the file to delete
            
        Returns:
            SparkRestResponse: _description_
        """
        return self.delete(*(id))

    def get_one_file(self, id):
        """Returns a single file.
        
        Args:
            id (int): The ID of the file to return
            
        Returns:
            SparkRestResponse: _description_
        """
        return self.get(*(id))

    def update_file_details(self, data, id):
        """Updates a file.
        
        Args:
            data (json): The data to add the file with
            id (int): (Required) The ID of the file
            
        Returns:
            SparkRestResponse: _description_
        """
        return self.put(data, *(id))

    def download_one_file(self, id):
        """Downloads a file.
        
        Args:
            id (int): The ID of the file to download
            
        Returns:
            SparkRestResponse: _description_
        """
        return self.get(*(id, 'download'))

    def get_all_files(self, **kwargs):
        """Returns all files.
        
        Args:
            start (int): The start offset for the returned items
            limit (int): The maximum number of items to return
        
        Returns:
            SparkRestResponse: _description_
        """
        return self.get(**kwargs)

    def add_file(self, data):
        """Adds a new file.
        
        Args:
            data (json): The data to add the file with
            
        Returns:
            SparkRestResponse: _description_
        """
        return self.post(data)

    def create_a_remote_file_and_link_it_to_an_item(self, data):
        """Creates a remote file and link it to an item.
        
        Args:
            data (json): The data to create the remote file with
            
        Returns:
            SparkRestResponse: _description_
        """
        return self.post(data, *('remote'))

    def link_a_remote_file_to_an_item(self, data):
        """Links a remote file to an item.
        
        Args:
            data (json): The data to link the remote file with
            id (int): (Required) The ID of the item
            
        Returns:
            SparkRestResponse: _description_
        """
        return self.post(data, *('remoteLink'))
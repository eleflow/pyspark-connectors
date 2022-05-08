from eleflow.connector.rest_api.rest_base import Restbase
from eleflow.connector.rest_api.spark_rest_response import SparkRestResponse

class PipeDriveProducts(Restbase):
    
    def __init__(self, url_base,api_token_key, api_token_value) -> None:
        super().__init__(url_base+'/products/',api_token_key, api_token_value)
    
    def list_followers_of_a_product(self, id, **kwargs):
        """Lists all followers of a product.
        
        Args:
            id (int): (Required) The ID of the product.
        
        Returns:
            SparkRestResponse: _description_
        """
        return self.get(*(id, 'followers'), **kwargs)

    def add_a_follower_to_a_product(self, id, data):
        """Adds a follower to a product.
        
        Args:
            id (int): (Required) The ID of the product.
            data (dict): (Required) The data to add.
        
        Returns:
            SparkRestResponse: _description_
        """
        return self.post(data, *(id, 'followers'))

    def delete_a_follower_from_a_product(self, id, follower_id):
        """Deletes a follower from a product.
        
        Args:
            id (int): (Required) The ID of the product.
            follower_id (int): (Required) The ID of the follower.
        
        Returns:
            SparkRestResponse: _description_
        """
        return self.delete(*(id, 'followers', follower_id))

    def delete_a_product(self, id):
        """Deletes a product.
        
        Args:
            id (int): (Required) The ID of the product.
        
        Returns:
            SparkRestResponse: _description_
        """
        return self.delete(*(id))

    def get_one_product(self, id):
        """Gets one product.
        
        Args:
            id (int): (Required) The ID of the product.
        
        Returns:
            SparkRestResponse: _description_
        """
        return self.get(*(id))

    def update_a_product(self, id, data):
        """Updates a product.
        
        Args:
            id (int): (Required) The ID of the product.
            data (dict): (Required) The data to update.
        
        Returns:
            SparkRestResponse: _description_
        """
        return self.put(data, *(id))

    def get_deals_where_a_product_is_attached_to(self, id, **kwargs):
        """Gets deals where a product is attached to.
        
        Args:
            id (int): (Required) The ID of the product.
        
        Returns:
            SparkRestResponse: _description_
        """
        return self.get(*(id, 'deals'), **kwargs)

    def list_files_attached_to_a_product(self, id, **kwargs):
        """Lists all files attached to a product.
        
        Args:
            id (int): (Required) The ID of the product.
        
        Returns:
            SparkRestResponse: _description_
        """
        return self.get(*(id, 'files'), **kwargs)

    def list_permitted_users(self, id):
        """Lists all permitted users.
        
        Args:
            id (int): (Required) The ID of the product.
        
        Returns:
            SparkRestResponse: _description_
        """
        return self.get(*(id, 'permitted_users'))

    def get_all_products(self, **kwargs):
        """Gets all products.
        
        Returns:
            SparkRestResponse: _description_
        """
        return self.get('', **kwargs)

    def add_a_product(self, data):
        """Adds a product.
        
        Args:
            data (dict): (Required) The data to add.
        
        Returns:
            SparkRestResponse: _description_
        """
        return self.post(data)

    def search_products(self, **kwargs):
        """Searches products.
        
        Args:
            query (str): (Required) The query to search.
        
        Returns:
            SparkRestResponse: _description_
        """
        return self.get(*('search'), **kwargs)
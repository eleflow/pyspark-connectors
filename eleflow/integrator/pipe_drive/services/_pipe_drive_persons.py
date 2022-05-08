from eleflow.connector.rest_api.rest_base import Restbase
from eleflow.connector.rest_api.spark_rest_response import SparkRestResponse

class PipeDrivePersons(Restbase):
    
    def __init__(self, url_base,api_token_key, api_token_value) -> None:
        super().__init__(url_base+'/persons/',api_token_key, api_token_value)
    
    def list_followers_of_a_person(self, id):
        """Lists all followers of a person.
        
        Args:
            id (int): (Required) The ID of the person.
        
        Returns:
            SparkRestResponse: _description_
        """
        return self.get(*(id, 'followers')) 

    def add_a_follower_to_a_person(self, id, data):
        """Adds a follower to a person.
        
        Args:
            id (int): (Required) The ID of the person.
            data (dict): (Required) The data to add.
        
        Returns:
            SparkRestResponse: _description_
        """
        return self.post(data, *(id, 'followers'))

    def delete_a_follower_from_a_person(self, id, follower_id):
        """Deletes a follower from a person.
        
        Args:
            id (int): (Required) The ID of the person.
            follower_id (int): (Required) The ID of the follower.
        
        Returns:
            SparkRestResponse: _description_
        """
        return self.delete(*(id, 'followers', follower_id))

    def delete_a_person(self, id):
        """Deletes a person.
        
        Args:
            id (int): (Required) The ID of the person.
        
        Returns:
            SparkRestResponse: _description_
        """
        return self.delete(*(id))

    def get_details_of_a_person(self, id):
        """Gets details of a person.
        
        Args:
            id (int): (Required) The ID of the person.
        
        Returns:
            SparkRestResponse: _description_
        """
        return self.get(*(id))

    def update_a_person(self, id, data):
        """Updates a person.
        
        Args:
            id (int): (Required) The ID of the person.
            data (dict): (Required) The data to update.
        
        Returns:
            SparkRestResponse: _description_
        """
        return self.put(data, *(id))

    def list_activities_associated_with_a_person(self, id, **kwargs):
        """Lists all activities associated with a person.
        
        Args:
            id (int): (Required) The ID of the person.
        
        Returns:
            SparkRestResponse: _description_
        """
        return self.get(*(id, 'activities'), **kwargs)

    def list_deals_associated_with_a_person(self, id, **kwargs):
        """Lists all deals associated with a person.
        
        Args:
            id (int): (Required) The ID of the person.
        
        Returns:
            SparkRestResponse: _description_
        """
        return self.get(*(id, 'deals'), **kwargs)

    def list_files_attached_to_a_person(self, id, **kwargs):
        """Lists all files attached to a person.
        
        Args:
            id (int): (Required) The ID of the person.
        
        Returns:
            SparkRestResponse: _description_
        """
        return self.get(*(id, 'files'), **kwargs)

    def list_updates_about_a_person(self, id, **kwargs):
        """Lists all updates about a person.
        
        Args:
            id (int): (Required) The ID of the person.
        
        Returns:
            SparkRestResponse: _description_
        """
        return self.get(*(id, 'flow'), **kwargs)

    def list_mail_messages_associated_with_a_person(self, id, **kwargs):
        """Lists all mail messages associated with a person.
        
        Args:
            id (int): (Required) The ID of the person.
        
        Returns:
            SparkRestResponse: _description_
        """
        return self.get(*(id, 'mailMessages'), **kwargs)

    def merge_two_persons(self, id, merge_with_id):
        """Merges two persons.
        
        Args:
            id (int): (Required) The ID of the person.
            merge_with_id (int): (Required) The ID of the person to merge with.
        
        Returns:
            SparkRestResponse: _description_
        """
        return self.put(*(id, 'merge'), **{'id': merge_with_id})

    def list_permitted_users(self, id):
        """Lists all permitted users.
        
        Args:
            id (int): (Required) The ID of the person.
        
        Returns:
            SparkRestResponse: _description_
        """
        return self.get(*(id, 'permittedUsers'))

    def list_products_associated_with_a_person(self, id, **kwargs):
        """Lists all products associated with a person.
        
        Args:
            id (int): (Required) The ID of the person.
        
        Returns:
            SparkRestResponse: _description_
        """
        return self.get(*(id, 'products'), **kwargs)

    def delete_multiple_persons_in_bulk(self, ids):
        """Deletes multiple persons in bulk.
        
        Args:
            ids (list): (Required) The IDs of the persons.
        
        Returns:
            SparkRestResponse: _description_
        """
        return self.delete(*('bulk'), **{'ids': ids})

    def get_all_persons(self, **kwargs):
        """Gets all persons.
        
        Returns:
            SparkRestResponse: _description_
        """
        return self.get(**kwargs)

    def add_a_person(self, data):
        """Adds a person.
        
        Args:
            data (dict): (Required) The data to add.
        
        Returns:
            SparkRestResponse: _description_
        """
        return self.post(data)

    def search_persons(self, **kwargs):
        """Searches persons.
        
        Returns:
            SparkRestResponse: _description_
        """
        return self.get(*('search'), **kwargs)
    
from eleflow.connector.rest_api.rest_base import Restbase
from eleflow.connector.rest_api.spark_rest_response import SparkRestResponse

class PipeDriveOrganizations(Restbase):
    
    def __init__(self, url_base,api_token_key, api_token_value) -> None:
        super().__init__(url_base+'/organizations/',api_token_key, api_token_value)
    
    def list_followers_of_an_organization(self, id):
        """Lists the followers of an organization.
        
        Args:
            id (int): (Required) The ID of the organization.
        
        Returns:
            SparkRestResponse: _description_
        """
        return self.get(*(id,'followers'))

    def add_a_follower_to_an_organization(self, id, data):
        """Adds a follower to an organization.
        
        Args:
            id (int): (Required) The ID of the organization.
            data (dict): (Required) The data to add.
        
        Returns:
            SparkRestResponse: _description_
        """
        return self.post(data, *(id,'followers'))

    def delete_a_follower_from_an_organization(self, id, follower_id):
        """Deletes a follower from an organization.
        
        Args:
            id (int): (Required) The ID of the organization.
            follower_id (int): (Required) The ID of the follower.
        
        Returns:
            SparkRestResponse: _description_
        """
        return self.delete(*(id,'followers',follower_id))

    def delete_an_organization(self, id):
        """Deletes an organization.
        
        Args:
            id (int): (Required) The ID of the organization.
        
        Returns:
            SparkRestResponse: _description_
        """
        return self.delete(*(id,))

    def get_details_of_an_organization(self, id):
        """Gets details of an organization.
        
        Args:
            id (int): (Required) The ID of the organization.
        
        Returns:
            SparkRestResponse: _description_
        """
        return self.get(*(id,))

    def update_an_organization(self, id, data):
        """Updates an organization.
        
        Args:
            id (int): (Required) The ID of the organization.
            data (dict): (Required) The data to update.
        
        Returns:
            SparkRestResponse: _description_
        """
        return self.put(data, *(id,))

    def list_activities_associated_with_an_organization(self, id, **kwargs):
        """Lists the activities associated with an organization.
        
        Args:
            id (int): (Required) The ID of the organization.
        
        Returns:
            SparkRestResponse: _description_
        """
        return self.get(*(id,'activities'), **kwargs)

    def list_deals_associated_with_an_organization(self, id, **kwargs):
        """Lists the deals associated with an organization.
        
        Args:
            id (int): (Required) The ID of the organization.
        
        Returns:
            SparkRestResponse: _description_
        """
        return self.get(*(id,'deals'), **kwargs)

    def list_files_attached_to_an_organization(self, id, **kwargs):
        """Lists the files attached to an organization.
        
        Args:
            id (int): (Required) The ID of the organization.
        
        Returns:
            SparkRestResponse: _description_
        """
        return self.get(*(id,'files'), **kwargs)

    def list_updates_about_an_organization(self, id, **kwargs):
        """Lists the updates about an organization.
        
        Args:
            id (int): (Required) The ID of the organization.
        
        Returns:
            SparkRestResponse: _description_
        """
        return self.get(*(id,'flow'), **kwargs)

    def list_mail_messages_associated_with_an_organization(self, id, **kwargs):
        """Lists the mail messages associated with an organization.
        
        Args:
            id (int): (Required) The ID of the organization.
        
        Returns:
            SparkRestResponse: _description_
        """
        return self.get(*(id,'mailMessages'), **kwargs)

    def merge_two_organizations(self, id, merge_with_id):
        """Merges two organizations.
        
        Args:
            id (int): (Required) The ID of the organization.
            merge_with_id (int): (Required) The ID of the organization to merge with.
        
        Returns:
            SparkRestResponse: _description_
        """
        return self.put({'merge_with_id': merge_with_id}, *(id,'merge'))

    def list_permitted_users(self, id):
        """Lists the permitted users of an organization.
        
        Args:
            id (int): (Required) The ID of the organization.
        
        Returns:
            SparkRestResponse: _description_
        """
        return self.get(*(id,'permittedUsers'))

    def list_persons_of_an_organization(self, id, **kwargs):
        """Lists the persons of an organization.
        
        Args:
            id (int): (Required) The ID of the organization.
        
        Returns:
            SparkRestResponse: _description_
        """
        return self.get(*(id,'persons'), **kwargs)

    def delete_multiple_organizations_in_bulk(self, ids):
        """Deletes multiple organizations in bulk.
        
        Args:
            ids (list): (Required) The IDs of the organizations.
        
        Returns:
            SparkRestResponse: _description_
        """
        return self.delete(**{'ids':ids})

    def get_all_organizations(self, **kwargs):
        """Gets all organizations.
        
        Returns:
            SparkRestResponse: _description_
        """
        return self.get(**kwargs)

    def add_an_organization(self, data):
        """Adds an organization.
        
        Args:
            data (dict): (Required) The data to add.
        
        Returns:
            SparkRestResponse: _description_
        """
        return self.post(data)

    def search_organizations(self, **kwargs):
        """Searches organizations.
        
        Returns:
            SparkRestResponse: _description_
        """
        return self.get(*('search'), **kwargs)
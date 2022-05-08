from eleflow.connector.rest_api.rest_base import Restbase
from eleflow.connector.rest_api.spark_rest_response import SparkRestResponse

class PipeDriveDeals(Restbase):
    
    def __init__(self, url_base,api_token_key, api_token_value) -> None:
        super().__init__(url_base+'/deals/',api_token_key, api_token_value)
        
    def get_all_deals(self, **kwargs):
        """Returns all deals. For more information, see the tutorial for getting all deals.

        Returns:
            SparkRestResponse: _description_
        """
        return self.get(**kwargs)
    
    def add_a_deal(self, data):
        """Adds a new deal. Note that you can supply additional custom fields along with the request that are not described here. 
        These custom fields are different for each Pipedrive account and can be recognized by long hashes as keys. 
        To determine which custom fields exists, fetch the dealFields and look for key values.

        Args:
            data (json): _description_

        Returns:
            SparkRestResponse: _description_
        """
        return self.post(data)
    
    def delete_multiple_deals_in_bulk(self, ids):
        """Marks multiple deals as deleted.
        
        Args:
            ids (list): (Required) The comma-separated IDs that will be deleted
        
        Returns:
            SparkRestResponse: _description_
        """
        return self.delete(*(ids))
        
    def search_deals(self, **kwargs):
        """Searches all deals by title, notes and/or custom fields. This endpoint is a wrapper of /v1/itemSearch with a narrower OAuth scope. Found deals can be filtered by the person ID and the organization ID.
        
        Args:
            term (str): (Required) The search term to look for. Minimum 2 characters (or 1 if using exact_match).
            fields (str): (Required) A comma-separated string array. The fields to perform the search from. Defaults to all of them.
            exact_match (bool): (Optional) When enabled, only full exact matches against the given term are returned. It is not case sensitive.
            person_id (int): (Optional) Will filter deals by the provided person ID. The upper limit of found deals associated with the person is 2000.
            organization_id (int): (Optional) Will filter deals by the provided organization ID. The upper limit of found deals associated with the organization is 2000.
            status (str): (Optional) Will filter deals by the provided specific status. open = Open, won = Won, lost = Lost. The upper limit of found deals associated with the status is 2000.
            include_fields (str): (oprtional) Supports including optional fields in the results which are not provided by default.
            start (int): (Optional) Pagination start. Note that the pagination is based on main results and does not include related items when using search_for_related_items parameter.
            limit (int) : (Optional) Items shown per page.
        
        Returns:
            SparkRestResponse: _description_
        """
        return self.get(*('search'), **kwargs)
        
    def get_deals_summary(self, **kwargs):
        """Returns a summary of all the deals.
        
        Args:
            status (str): Only fetch deals with a specific status. open = Open, won = Won, lost = Lost
            filter_id (int): user_id will not be considered. Only deals matching the given filter will be returned.
            user_id (int): Only deals matching the given user will be returned. user_id will not be considered if you use filter_id.
            stage_id (int): Only deals within the given stage will be returned
        
        Returns:
            SparkRestResponse: _description_
        """
        return self.get(*('summary'), **kwargs)
        
    def get_deals_timeline(self, **kwargs):
        """Returns open and won deals, grouped by a defined interval of time set in a date-type dealField (field_key) — e.g. when month is the chosen interval, and 3 months are asked starting from January 1st, 2012, deals are returned grouped into 3 groups — January, February and March — based on the value of the given field_key.

        Args:
            start_date (str): (Required) The date when the first interval starts. Format: YYYY-MM-DD
            interval (str): (Required) The type of the interval
            amount (int): (Required) The number of given intervals, starting from start_date, to fetch. E.g. 3 (months).
            field_key (str): (Required) The date field key which deals will be retrieved from
            user_id (int): If supplied, only deals matching the given user will be returned
            pipeline_id (int): If supplied, only deals matching the given pipeline will be returned
            filter_id (int): If supplied, only deals matching the given filter will be returned
            exclude_deals (int): Whether to exclude deals list (1) or not (0). Note that when deals are excluded, the timeline summary (counts and values) is still returned.
            totals_convert_currency (str): The 3-letter currency code of any of the supported currencies. When supplied, totals_converted is returned per each interval which contains the currency-converted total amounts in the given currency. You may also set this parameter to default_currency in which case the user's default currency is used.
        
        Returns:
            SparkRestResponse: _description_
        """
        return self.get(*('timeline'), **kwargs)

    def list_followers_of_a_deal(self, deal_id):
        """Returns all the users that are following the given deal.
        
        Args:
            deal_id (int): The deal ID.

        Returns:
            SparkRestResponse: _description_
        """
        return self.get(*(deal_id, 'followers'))

    def add_a_follower_to_a_deal(self, deal_id, data):
         """
         Adds a follower to a deal.

         Args:
             deal_id (int): The deal ID.
             data (json): _description_

         Returns:
             SparkRestResponse: _description_
         """
         return self.post(data, *(deal_id, 'followers'))

    def delete_multiple_deals(self, deal_id, follower_id):
        """Deletes a follower from a deal.
        
        Args:
            deal_id (int): The deal ID.
            follower_id (int): The follower ID.

        Returns:
            SparkRestResponse: _description_
        """
        return self.delete(*(deal_id, 'followers', follower_id))

    def list_participants_of_a_deal(self, deal_id, **kwargs):
        """Returns all the participants of the given deal.
        
        Args:
            deal_id (int): The deal ID.
        
        Returns:
            SparkRestResponse: _description_
        """
        return self.get(*(deal_id, 'participants'), **kwargs)

    def add_a_participant_to_a_deal(self, deal_id, data):
        """Adds a participant to a deal.
        
        Args:
            deal_id (int): The deal ID.
            data (json): _description_

        Returns:
            SparkRestResponse: _description_
        """
        return self.post(data, *(deal_id, 'participants'))

    def felete_a_participant_from_a_deal(self, deal_id, participant_id):
        """Deletes a participant from a deal.
        
        Args:
            deal_id (int): The deal ID.
            participant_id (int): The participant ID.

        Returns:
            SparkRestResponse: _description_
        """
        return self.delete(*(deal_id, 'participants', participant_id))

    def update_product_attachment_details_of_the_deal(self, deal_id, product_attachment_id, data):
        """Updates the details of a product attachment of a deal.
        
        Args:
            deal_id (int): The deal ID.
            product_attachment_id (int): The product attachment ID.

        Returns:
            SparkRestResponse: _description_
        """
        return self.put(data, *(deal_id, 'products', product_attachment_id))

    def delete_an_attachment_product_from_a_deal(self, deal_id, product_attachment_id):
        """Deletes a product attachment from a deal.
        
        Args:
            deal_id (int): The deal ID.
            product_attachment_id (int): The product attachment ID.

        Returns:
            SparkRestResponse: _description_
        """
        return self.delete(*(deal_id, 'products', product_attachment_id))

    def list_products_attached_to_a_deal(self, deal_id, **kwargs):
        """Returns all the products attached to a deal.
        
        Args:
            deal_id (int): The deal ID.
            start (int): Pagination start.
            limit (int): Items shown per page.
            include_product_data (int): Whether to include product data (1) or not (0, default).
        
        Returns:
            SparkRestResponse: _description_
        """
        return self.get(*(deal_id, 'products'), **kwargs)

    def add_a_product_to_a_deal(self, deal_id, data):
        """Adds a product to a deal.
        
        Args:
            deal_id (int): The deal ID.
            data (json): _description_

        Returns:
            SparkRestResponse: _description_
        """
        return self.post(data, *(deal_id, 'products'))

    def delete_a_deal(self, deal_id):
        """Deletes a deal.
        
        Args:
            deal_id (int): The deal ID.

        Returns:
            SparkRestResponse: _description_
        """
        return self.delete(*(deal_id))

    def get_details_of_a_deal(self, deal_id):
        """Returns the details of a deal.
        
        Args:
            deal_id (int): The deal ID.
        
        Returns:
            SparkRestResponse: _description_
        """
        return self.get(*(deal_id))

    def update_a_deal(self, deal_id, data):
        """Updates a deal.
        
        Args:
            deal_id (int): The deal ID.
            data (json): _description_

        Returns:
            SparkRestResponse: _description_
        """
        return self.put(data, *(deal_id))

    def list_activities_associated_with_a_deal(self, deal_id, **kwargs):
        """Returns all the activities associated with a deal.
        
        Args:
            deal_id (int): The deal ID.
            start (int): Pagination start.
            limit (int): Items shown per page.
        
        Returns:
            SparkRestResponse: _description_
        """
        return self.get(*(deal_id, 'activities'), **kwargs)

    def duplicate_deal(self, deal_id):
        """Duplicates a deal.
        
        Args:
            deal_id (int): The deal ID.

        Returns:
            SparkRestResponse: _description_
        """
        return self.post(None, *(deal_id, 'duplicate'))
    
    def list_files_attached_to_a_deal(self, deal_id, **kwargs):
        """Returns all the files attached to a deal.
        
        Args:
            deal_id (int): The deal ID.
            start (int): Pagination start.
            limit (int): Items shown per page.
        
        Returns:
            SparkRestResponse: _description_
        """
        return self.get(*(deal_id, 'files'), **kwargs)

    def list_updated_about_a_deal(self, deal_id, **kwargs):
        """Returns all the updates about a deal.
        
        Args:
            deal_id (int): The deal ID.
            start (int): Pagination start.
            limit (int): Items shown per page.
        
        Returns:
            SparkRestResponse: _description_
        """
        return self.get(*(deal_id, 'flow'), **kwargs)

    def list_mail_messages_associated_with_a_deal(self, deal_id, **kwargs):
        """Returns all the mail messages associated with a deal.
        
        Args:
            deal_id (int): The deal ID.
            start (int): Pagination start.
            limit (int): Items shown per page.
        
        Returns:
            SparkRestResponse: _description_
        """
        return self.get(*(deal_id, 'mailMessages'), **kwargs)

    def merge_two_deals(self, deal_id, data, merge_deal_id):
        """Merges two deals.
        
        Args:
            deal_id (int): The deal ID.
            other_deal_id (int): The other deal ID.

        Returns:
            SparkRestResponse: _description_
        """
        return self.put({'merge_with_id': merge_deal_id}, *(deal_id, 'merge'))

    def list_permitted_users(self, deal_id):
        """Returns all the permitted users associated with a deal.
        
        Args:
            deal_id (int): The deal ID.
        
        Returns:
            SparkRestResponse: _description_
        """
        return self.get(*(deal_id, 'permittedUsers'))

    def list_all_persons_associated_with_a_deal(self, deal_id, **kwargs):
        """Returns all the persons associated with a deal.
        
        Args:
            deal_id (int): The deal ID.
            start (int): Pagination start.
            limit (int): Items shown per page.
        
        Returns:
            SparkRestResponse: _description_
        """
        return self.get(*(deal_id, 'persons'), **kwargs)
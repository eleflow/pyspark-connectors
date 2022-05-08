from eleflow.connector.rest_api.rest_base import Restbase
from eleflow.connector.rest_api.spark_rest_response import SparkRestResponse

class PipeDriveItemSearch(Restbase):
    
    def __init__(self, url_base,api_token_key, api_token_value) -> None:
        super().__init__(url_base+'/itemSearch/',api_token_key, api_token_value)
    
    def perform_a_search_from_multiple_item_types(self, **kwargs):
        """Performs a search from multiple item types.
        
        Args:
            term (str): (Required) The search term to look for. Minimum 2 characters (or 1 if using `exact_match`).
            item_types (str): A comma-separated string array. The type of items to perform the search from. Defaults to all.
            fields (str): A comma-separated string array. The fields to perform the search from. Defaults to all. Relevant for each item type are:<br> <table> <tr><th><b>Item type</b></th><th><b>Field</b></th></tr> <tr><td>Deal</td><td>`custom_fields`, `notes`, `title`</td></tr> <tr><td>Person</td><td>`custom_fields`, `email`, `name`, `notes`, `phone`</td></tr> <tr><td>Organization</td><td>`address`, `custom_fields`, `name`, `notes`</td></tr> <tr><td>Product</td><td>`code`, `custom_fields`, `name`</td></tr> <tr><td>Lead</td><td>`custom_fields`, `notes`, `email`, `organization_name`, `person_name`, `phone`, `title`</td></tr> <tr><td>File</td><td>`name`</td></tr> <tr><td>Mail attachment</td><td>`name`</td></tr> </table> <br> When searching for leads, the email, organization_name, person_name, and phone fields will return results only for leads not linked to contacts. For searching leads by person or organization values, please use `search_for_related_items`.
            search_for_related_iems (bool): When enabled, the response will include up to 100 newest related leads and 100 newest related deals for each found person and organization and up to 100 newest related persons for each found organization.
            exact_match (bool): When enabled, only full exact matches against the given term are returned. It is <b>not</b> case sensitive.
            include_fields (str): A comma-separated string array. Supports including optional fields in the results which are not provided by default.
            start (int): Pagination start. Note that the pagination is based on main results and does not include related items when using `search_for_related_items` parameter.
            limit (int): Items shown per page

        Returns:
            SparkRestResponse: _description_
        """
        return self.get(**kwargs)

    def perform_a_search_using_a_specific_field_from_an_item_type(self, **kwargs):
        """Performs a search using a specific field from an item type.
        
        Args:
            term (str): (Required) (Required) The search term to look for. Minimum 2 characters (or 1 if using exact_match).
            field_type (str): (Required) The type of the field to perform the search from
            exact_match (bool): When enabled, only full exact matches against the given term are returned. The search is case sensitive.
            field_key (str): (Required) The key of the field to search from. The field key can be obtained by fetching the list of the fields using any of the fields' API GET methods (dealFields, personFields, etc.).
            return_item_ids (bool): Whether to return the IDs of the matching items or not. When not set or set to 0 or false, only distinct values of the searched field are returned. When set to 1 or true, the ID of each found item is returned.
            start (int): Pagination start.
            limit (int): Items shown per page

        Returns:
            SparkRestResponse: _description_
        """
        return self.get(*('field'), **kwargs)
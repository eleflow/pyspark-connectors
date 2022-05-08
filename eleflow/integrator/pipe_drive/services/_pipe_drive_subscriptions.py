from eleflow.connector.rest_api.rest_base import Restbase
from eleflow.connector.rest_api.spark_rest_response import SparkRestResponse

class PipeDriveSubscriptions(Restbase):
    
    def __init__(self, url_base,api_token_key, api_token_value) -> None:
        super().__init__(url_base+'/subscriptions/',api_token_key, api_token_value)
    
    def get_details_of_a_subscription(self, id):
        """Gets details of a subscription.
        
        Args:
            id (int): (Required) The ID of the subscription.
        
        Returns:
            SparkRestResponse: _description_
        """
        return self.get(*(id))

    def delete_a_subscription(self, id):
        """Deletes a subscription.
        
        Args:
            id (int): (Required) The ID of the subscription.
        
        Returns:
            SparkRestResponse: _description_
        """
        return self.delete(*(id))

    def get_all_payments_of_a_subscription(self, id):
        """Gets all payments of a subscription.
        
        Args:
            id (int): (Required) The ID of the subscription.
        
        Returns:
            SparkRestResponse: _description_
        """
        return self.get(*(id,'payments'))

    def update_a_recurring_subscription(self, id, data):
        """Updates a recurring subscription.
        
        Args:
            id (int): (Required) The ID of the subscription.
            data (dict): (Required) The data to update.
        
        Returns:
            SparkRestResponse: _description_
        """
        return self.put(data, *('recurring',id))

    def cancel_a_recurring_subscription(self, id, end_date):
        """Cancels a recurring subscription.
        
        Args:
            id (int): (Required) The ID of the subscription.
        
        Returns:
            SparkRestResponse: _description_
        """
        return self.put({'end_date': end_date}, *('recurring',id,'cancel'))

    def add_a_recurring_subscription(self, data):
        """Adds a recurring subscription.
        
        Args:
            data (dict): (Required) The data to add.
        
        Returns:
            SparkRestResponse: _description_
        """
        return self.post(data, *('recurring'))

    def add_an_installment_subscription(self, data):
        """Adds an installment subscription.
        
        Args:
            data (dict): (Required) The data to add.
        
        Returns:
            SparkRestResponse: _description_
        """
        return self.post(data, *('installment'))

    def update_an_installment_subscription(self, id, data):
        """Updates an installment subscription.
        
        Args:
            id (int): (Required) The ID of the subscription.
            data (dict): (Required) The data to update.
        
        Returns:
            SparkRestResponse: _description_
        """
        return self.put(data, *('installment',id))

    def find_subscription_by_deal(self, deal_id):
        """Finds a subscription by deal.
        
        Args:
            deal_id (int): (Required) The ID of the deal.
        
        Returns:
            SparkRestResponse: _description_
        """
        return self.get(*('find',deal_id))
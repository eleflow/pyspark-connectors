from eleflow.connector.rest_api.rest_base import Restbase
from eleflow.connector.rest_api.spark_rest_response import SparkRestResponse

class PipeDriveMailbox(Restbase):
    
    def __init__(self, url_base,api_token_key, api_token_value) -> None:
        super().__init__(url_base+'/mailbox/',api_token_key, api_token_value)
    
    def delete_mail_thread(self, id):
        """Deletes a mail thread.
        
        Args:
            id (int): (Required) The ID of the mail thread.
        
        Returns:
            SparkRestResponse: _description_
        """
        return self.delete(*('mailThreads',id))

    def get_one_mail_thread(self, id):
        """Gets one mail thread.
        
        Args:
            id (int): (Required) The ID of the mail thread.
        
        Returns:
            SparkRestResponse: _description_
        """
        return self.get(*('mailThreads',id))

    def update_mail_thread_details(self, id, data):
        """Updates a mail thread.
        
        Args:
            id (int): (Required) The ID of the mail thread.
            data (dict): (Required) The data to update.
        
        Returns:
            SparkRestResponse: _description_
        """
        return self.put(data, *('mailThreads',id))

    def get_all_mail_messages_of_mail_thread(self, id):
        """Gets all mail messages of a mail thread.
        
        Args:
            id (int): (Required) The ID of the mail thread.
        
        Returns:
            SparkRestResponse: _description_
        """
        return self.get(*('mailThreads',id,'mailMessages'))

    def get_mail_threads(self, **kwargs):
        """Returns mail threads in a specified folder ordered by the most recent message within.
        
        Args:
            **kwargs: (Optional) Parameters to filter the results.
        
        kwargs:
            folder (str): (Required) The type of folder to fetch
            start (int): Pagination start
            limit (int): Items shown per page

        Returns:
            SparkRestResponse: _description_
        """
        return self.get(*('mailThreads'), **kwargs)

    def get_one_mail_message(self, id, **kwargs):
        """Gets one mail message.
        
        Args:
            id (int): (Required) The ID of the mail message to fetch
            **kwargs: (Optional) Parameters to filter the results.
        
        kwargs:
            include_body (int): Whether to include the full message body or not. 0 = Don't include, 1 = Include
        
        Returns:
            SparkRestResponse: _description_
        """
        return self.get(*('mailMessages',id), **kwargs)
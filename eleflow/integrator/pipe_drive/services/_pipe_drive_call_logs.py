from eleflow.connector.rest_api.rest_base import Restbase
from eleflow.connector.rest_api.spark_rest_response import SparkRestResponse

class PipeDriveCallLogs(Restbase):
    
    def __init__(self, url_base,api_token_key, api_token_value) -> None:
        super().__init__(url_base+'/callLogs/',api_token_key, api_token_value)
        
    def add_a_call_log(self, data):
        """Adds a new call log.

        Args:
            data (json): _description_

        Returns:
            SparkRestResponse: _description_
        """
        return self.post(data)
    
    def get_all_call_logs_assigned_to_a_particular_user(self, **kwargs):
        """Returns all call logs assigned to a particular user.

        Returns:
            SparkRestResponse: _description_
        """
        return self.get(**kwargs)
    
    def delete_a_call_log(self, id_call_log):
        """Deletes a call log. If there is an audio recording attached to it, it will also be deleted. The related activity will not be removed by this request. If you want to remove the related activities, please use the endpoint which is specific for activities.

        Args:
            id_call_log (str): (Required) The ID received when you create the call log

        Returns:
            SparkRestResponse: _description_
        """
        return self.delete(*(id_call_log))
    
    def get_details_of_a_call_log(self, id_call_log):
        """Returns details of a specific call log.

        Args:
            id_call_log (str): (Required) The ID received when you create the call log

        Returns:
            SparkRestResponse: _description_
        """
        return self.get(*(id_call_log))
from eleflow.connector.rest_api.rest_base import Restbase
from eleflow.connector.rest_api.spark_rest_response import SparkRestResponse

class PipeDriveGoals(Restbase):
    
    def __init__(self, url_base,api_token_key, api_token_value) -> None:
        super().__init__(url_base+'/goals/',api_token_key, api_token_value)
    
    def update_existing_goal(self, data, id):
        """Updates an existing goal.
        
        Args:
            data (json): The data to add the goal with
            id (int): (Required) The ID of the goal
            
        Returns:
            SparkRestResponse: _description_
        """
        return self.put(data, *(id))

    def delete_existing_goal(self, id):
        """Deletes an existing goal.
        
        Args:
            id (int): (Required) The ID of the goal
            
        Returns:
            SparkRestResponse: _description_
        """
        return self.delete(*(id))

    def get_result_of_a_goal(self, id, **kwargs):
        """Returns the result of a goal.
        
        Args:
            id (int): (Required) The ID of the goal that the results are looked for.
            period.start (int): (Required) The start date of the period for which to find progress of a goal. Date in format of YYYY-MM-DD. This date must be the same or after the goal duration start date.
            poeriod.end(int): (Required) The end date of the period for which to find progress of a goal. Date in format of YYYY-MM-DD. This date must be the same or before the goal duration end date.
            
        Returns:
            SparkRestResponse: _description_
        """
        return self.get(*(id, 'results'), **kwargs)

    def add_a_new_goal(self, data):
        """Adds a new goal.
        
        Args:
            data (json): The data to add the goal with
            
        Returns:
            SparkRestResponse: _description_
        """
        return self.post(data)

    def find_goals(self, **kwargs):
        """Returns all goals.
        
        Args:
            type.name (str): The type of the goal. If provided, everyone's goals will be returned.
            title (str): The title of the goal
            is_active (bool): Whether the goal is active or not
            assignee.id (int): The ID of the user who's goal to fetch. When omitted, only your goals will be returned.
            assignee.type (str): The type of the goal's assignee. If provided, everyone's goals will be returned.
            expected_outcome.target (int): The numeric value of the outcome. If provided, everyone's goals will be returned.
            expected_outcome.tracking_metric (str): The tracking metric of the expected outcome of the goal. If provided, everyone's goals will be returned.
            expected_outcome.currency_id (int):The numeric ID of the goal's currency. Only applicable to goals with expected_outcome.tracking_metric with value sum. If provided, everyone's goals will be returned.
            type.params.pipeline_id (int): The ID of the pipeline or null for all pipelines. If provided, everyone's goals will be returned.
            type.params.stage_id (int): The ID of the stage. Applicable to only deals_progressed type of goals. If provided, everyone's goals will be returned.
            type.params.activity_type_id (int): The ID of the activity type. Applicable to only activities_completed or activities_added types of goals. If provided, everyone's goals will be returned.
            period.start (str): The start date of the period for which to find goals. Date in format of YYYY-MM-DD. When period.start is provided, period.end must be provided too.
            period.end (str): The end date of the period for which to find goals. Date in format of YYYY-MM-DD.
            
        Returns:
            SparkRestResponse: _description_
        """
        return self.get(*('find'), **kwargs)
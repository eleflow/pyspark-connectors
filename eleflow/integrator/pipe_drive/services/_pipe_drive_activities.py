from eleflow.connector.rest_api.rest_base import Restbase
from eleflow.connector.rest_api.spark_rest_response import SparkRestResponse

class PipeDriveActivities(Restbase):
    
    def __init__(self, url_base,api_token_key, api_token_value) -> None:
        super().__init__(url_base+'/activities/',api_token_key, api_token_value)
        
    def get_all_activities_assigned_to_a_particular_user(self, **kwargs) -> SparkRestResponse:
        """Returns all activities assigned to a particular user.
        Query Params:
            user_id <integer>: The ID of the user whose activities will be fetched. If omitted, the user associated with the API token will be used. If 0, activities for all company users will be fetched based on the permission sets.
            filter_id <integer>: The ID of the filter to use (will narrow down results if used together with user_id parameter)
            type <string>: The type of the activity, can be one type or multiple types separated by a comma. This is in correlation with the key_string parameter of ActivityTypes.
            limit <integer>: For pagination, the limit of entries to be returned. If not provided, 100 items will be returned.
            start <integer>: For pagination, the position that represents the first result for the page
            start_date <date>: Use the activity due date where you wish to begin fetching activities from. Insert due date in YYYY-MM-DD format.
            end_date <date>: Use the activity due date where you wish to stop fetching activities from. Insert due date in YYYY-MM-DD format.
            done <number>: Whether the activity is done or not. 0 = Not done, 1 = Done. If omitted returns both done and not done activities.

        Returns:
            SparkRestResponse: _description_
        """
        return self.get(**kwargs)
    
    def delete_multiple_activities_in_bulk(self, ids) -> SparkRestResponse:
        """Marks multiple activities as deleted.
        Body:
            ids <string>: The comma-separated IDs of activities that will be deleted.

        Returns:
            SparkRestResponse: _description_
        """
        return self.delete(**{'ids': ids})
    
    def add_an_activity(self, data):
        """Adds a new activity. Includes more_activities_scheduled_in_context property in response's additional_data which indicates whether there are more undone activities scheduled with the same deal, person or organization (depending on the supplied data). For more information, see the tutorial for adding an activity.
        Args:
            data (json): 
                {
                    "due_date": "<date>",
                    "due_time": "<string>",
                    "duration": "<string>",
                    "deal_id": "<integer>",
                    "person_id": "<integer>",
                    "org_id": "<integer>",
                    "note": "<string>",
                    "location": "<string>",
                    "public_description": "<string>",
                    "subject": "<string>",
                    "type": "<string>",
                    "user_id": "<integer>",
                    "participants": [
                        "<object>",
                        "<object>"
                    ],
                    "busy_flag": "<boolean>",
                    "attendees": [
                        "<object>",
                        "<object>"
                    ],
                    "done": "<number>"
                }

        Returns:
            SparkRestResponse: _description_
        """
        return self.post(data)
    
    def get_details_of_an_activity(self, activity_id):
        """Returns the details of a specific activity.

        Args:
            activity_id (integer): The ID of the activity

        Returns:
            SparkRestResponse: _description_
        """
        return self.get(*(activity_id))
    
    def update_and_activity(self, activity_id, data):
        """Updates an activity.

        Args:
            activity_id (integer): The ID of the activity
            data (dict): The data to update the activity with

        Returns:
            SparkRestResponse: _description_
        """
        return self.put(data, *(activity_id))
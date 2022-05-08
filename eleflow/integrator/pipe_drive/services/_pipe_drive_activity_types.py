from eleflow.connector.rest_api.rest_base import Restbase

class PipeDriveActivityTypes(Restbase):
    
    def __init__(self, url_base,api_token_key, api_token_value) -> None:
        super().__init__(url_base+'/activityTypes/',api_token_key, api_token_value)
    
    def get_all_activity_types(self):
        """Returns all activity types.
        
        Returns:
            SparkRestResponse: _description_
        """
        return self.get()
    
    def add_new_activity_type(self, data):
        """Adds a new activity type.
        
        Args:
            data (dict): The data to add the activity type with
                Body: {
                    name <string>: (Required) The name of the activity type
                    icon_key <string>: (Required) Icon graphic to use for representing this activity type
                    color <string>: A designated color for the activity type in 6-character HEX format (e.g. FFFFFF for white, 000000 for black)
                }
        
        Returns:
            SparkRestResponse: _description_
        """
        return self.post(data)
    
    def delete_multiple_activity_types(self, ids):
        """Deletes multiple activity types.
        
        Args:
            ids (list): The IDs of the activity types to delete
        
        Returns:
            SparkRestResponse: _description_
        """
        return self.delete(**{'ids':ids})
    
    def delete_an_activity_type(self, id):
        """Deletes an activity type.
        
        Args:
            id (int): The ID of the activity type to delete
        
        Returns:
            SparkRestResponse: _description_
        """
        return self.delete(*(id))
    
    def update_an_activity_type(self, data, id):
        """Updates an activity type.

        Args:
            data (json): The data to add the activity type with
            id (_type_): (Required) The ID of the activity type

        Returns:
            SparkRestResponse: _description_
        """
        return self.put(data, *(id))
from eleflow.connector.rest_api.rest_base import Restbase
from eleflow.connector.rest_api.spark_rest_response import SparkRestResponse

class PipeDriveNotes(Restbase):
    
    def __init__(self, url_base,api_token_key, api_token_value) -> None:
        super().__init__(url_base+'/notes/',api_token_key, api_token_value)
    
    def get_one_comment(self, id, comment_id):
        """Gets one comment.
        
        Args:
            id (int): (Required) The ID of the comment.
        
        Returns:
            SparkRestResponse: _description_
        """
        return self.get(*(id, 'comments', comment_id))
    
    def update_a_comment_related_to_a_note(self, id, comment_id, data):
        """Updates a comment related to a note.
        
        Args:
            id (int): (Required) The ID of the note.
            comment_id (int): (Required) The ID of the comment.
            data (dict): (Required) The data to update.
        
        Returns:
            SparkRestResponse: _description_
        """
        return self.patch(data, *(id, 'comments', comment_id))

    def delete_a_comment_related_to_a_note(self, id, comment_id):
        """Deletes a comment related to a note.
        
        Args:
            id (int): (Required) The ID of the note.
            comment_id (int): (Required) The ID of the comment.
        
        Returns:
            SparkRestResponse: _description_
        """
        return self.delete(*(id, 'comments', comment_id))

    def get_all_comments_for_a_note(self, id, **kwargs):
        """Gets all comments for a note.
        
        Args:
            id (int): (Required) The ID of the note.
        
        Returns:
            SparkRestResponse: _description_
        """
        return self.get(*(id, 'comments'), **kwargs)

    def add_a_comment_related_to_a_note(self, id, data):
        """Adds a comment related to a note.
        
        Args:
            id (int): (Required) The ID of the note.
            data (dict): (Required) The data to add.
        
        Returns:
            SparkRestResponse: _description_
        """
        return self.post(data, *(id, 'comments'))

    def delete_a_note(self, id):
        """Deletes a note.
        
        Args:
            id (int): (Required) The ID of the note.
        
        Returns:
            SparkRestResponse: _description_
        """
        return self.delete(*(id))
    
    def get_one_note(self, id):
        """Gets one note.
        
        Args:
            id (int): (Required) The ID of the note.
        
        Returns:
            SparkRestResponse: _description_
        """
        return self.get(*(id))

    def update_a_note(self, id, data):
        """Updates a note.
        
        Args:
            id (int): (Required) The ID of the note.
            data (dict): (Required) The data to update.
        
        Returns:
            SparkRestResponse: _description_
        """
        return self.put(data, *(id))

    def get_all_notes(self, **kwargs):
        """Gets all notes.
        
        Returns:
            SparkRestResponse: _description_
        """
        return self.get(**kwargs)

    def add_a_note(self, data):
        """Adds a note.
        
        Args:
            data (dict): (Required) The data to add.
        
        Returns:
            SparkRestResponse: _description_
        """
        return self.post(data)
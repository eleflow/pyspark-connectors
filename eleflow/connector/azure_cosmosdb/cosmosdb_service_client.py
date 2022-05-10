from azure.cosmos import (CosmosClient, PartitionKey)

from .cosmosdb_document import CosmosDBDocument

class CosmosDBServiceClient:
    
    def __init__(self, endpoint, auth_key, database_name, container_name, partition_key):
        if not endpoint or not auth_key or not database_name or not container_name or not partition_key:
            raise Exception('Missing required parameters')
        self._PARTITION_KEY = partition_key
        self._CONTAINER = (CosmosClient(endpoint, auth_key)
                           .create_database_if_not_exists(id=database_name)
                           .create_container_if_not_exists(id=container_name, partition_key=PartitionKey(path=partition_key)))
           
    def create_item(self, document) -> CosmosDBDocument:
        """Createm item in the container. This method is used to create a new item in the container.
            That's item needs to be a dictionary.
        Args:
            document (Dict): Dictionary with the item to be created.

        Returns:
            Dict[str, str]: Item created.
        """
        return CosmosDBDocument(self._CONTAINER.create_item(document))

    def delete_item(self, document) -> bool:
        """Delete item in the container. This method is used to delete an item in the container.

        Args:
            document (Dict): Dictionary with the item to be deleted.
        """
        self._CONTAINER.delete_item(document, partition_key=self._PARTITION_KEY)
        return True

    def get_item(self, uuid, partition_key='') -> CosmosDBDocument:
        """Get item in the container. This method is used to get an item in the container using uuid of the item.

        Args:
            uuid (str): UUID of the item to be retrieved.

        Returns:
            Dict[str, str]: Item retrieved.
        """
        return CosmosDBDocument(self._CONTAINER.read_item(item=uuid, partition_key=partition_key))

    def query_items(self, query):
        """Query items in the container. This method is used to query items in the container.

        Args:
            query (str): Query to be executed.

        Returns:
            Iterable[Dict[str, str]]: Items retrieved.
        """
        return CosmosDBDocument(self._CONTAINER.query_items(
            query = query,
            enable_cross_partition_query=True
            ))
        
    def get_by_id(self, uuid):
      """Count items in the container. This method is used to count items in the container.

      Returns:
        Iterable[Dict[str, str]]: Items retrieved.
      """
      return CosmosDBDocument(self._CONTAINER.query_items(f"SELECT * FROM c WHERE c.id = '{uuid}'", enable_cross_partition_query=True))
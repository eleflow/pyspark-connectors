import os
from eleflow.__builder__ import EleflowAbstractConnectionBuilder

settings = dict(
  HOST = os.environ.get("COSMOSDB_HOST"),
  KEY = os.environ.get("COSMOSDB_KEY"),
  DATABASE = os.environ.get("COSMOSDB_DATABASE"),
  COLECTION = 'ima_scenarios',
  PARTITION_KEY = '/creation_date'
)

class CosmosDBConnection(EleflowAbstractConnectionBuilder):
    
    def __init__(self, host, key):
        self._HOST = host
        self._KEY = key
    
    @staticmethod
    def build(cls, host, key):
        return cls(host, key)
        
    def get_service_client(self, database, colection, partition_key) -> Any:
        return super().get_service_client()


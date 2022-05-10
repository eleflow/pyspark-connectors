import os
from eleflow.__builder__ import EleflowAbstractConnectionBuilder
from .cosmosdb_service_client import CosmosDBServiceClient

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
    
    @classmethod
    def build(cls, host, key):
        return cls(host, key)
        
    def get_service_client(self, database, colection, partition_key) -> CosmosDBServiceClient:
        return CosmosDBServiceClient(self._HOST, self._KEY, database, colection, partition_key)


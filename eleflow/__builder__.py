from abc import ABC, abstractmethod
from typing import Any

class EleflowAbstractConnectionBuilder(ABC):
    
    @abstractmethod
    def get_service_client(self) -> Any:
        pass
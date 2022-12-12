"""It contains ingestor relevant classes."""


from typing import List
from abc import ABC, abstractmethod

from .QuoteModel import QuoteModel

class IngestorInterface(ABC):
    """Class for a ingestor collections"""
    
    allowed_extensions = []
    
    @classmethod
    def can_ingest(cls, path: str) -> bool:
        """consider whether a file can be ingested."""
        print("here")
        print(path)
        extension = path.split('.')[-1]
        print(extension)
        print(cls.allowed_extensions)
        print(extension in cls.allowed_extensions)
        return extension in cls.allowed_extensions
    
    @classmethod
    @abstractmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """parse the file contents and output it to the quotes."""
        pass
    





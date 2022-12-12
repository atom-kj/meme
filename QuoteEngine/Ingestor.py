"""Select a ingestor for a target file to be ingested."""

from typing import List

from .IngestorInterface import IngestorInterface
from .TextIngestor import TXTIngestor
from .DocxIngestor import DocxIngestor
from .PDFIngestor import PDFIngestor
from .CSVIngestor import CSVIngestor
from .QuoteModel import QuoteModel

class Ingestor(IngestorInterface):
    """Take file path, select ingestor, return quotes."""
    
    ingestors = [TXTIngestor, DocxIngestor, PDFIngestor, CSVIngestor]
    
    @classmethod
    def parse(cls, path:str) -> List[QuoteModel]:
        """select a ingestor."""
        for ingestor in cls.ingestors:
            print(path)
            print(ingestor)
            if ingestor.can_ingest(path):
                print('yes')
                print(ingestor)
                print(path)
                return ingestor.parse(path)

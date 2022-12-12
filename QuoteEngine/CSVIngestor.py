"""csv ingestor."""

from typing import List
import pandas as pd

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel

class CSVIngestor(IngestorInterface):
    """Check the csv file can be parsed. Create a text file. Splits the lines to generate a body and author of quote."""
    allowed_extension = ['csv']
    
    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Take the path and check whether it can be ingested."""
        if not cls.can_ingest(path):
            raise Exception('Cannot ingest.')
        
        quotes = []
        df = pd.read_csv(path,header=0)
        for index, row in df.iterrows():
            quote = QuoteModel(row['body'], row['author'])
            quotes.append(quote)
        
        return quotes
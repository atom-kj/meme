"""Text ingestor"""

from typing import List
from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel


class TXTIngestor(IngestorInterface):
    """Check the txt file can be parsed. Create a text file. Splits the lines to generate a body and author of quote."""
    
    allowed_extensions = ['txt']
    
    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Take the path and check whether it can be ingested."""
        if not cls.can_ingest(path):
            raise Exception('cannot ingest.')
            
        quotes = []
        with open(path) as f:
            ls = f.readlines()
            for l in ls:
                if len(l) > 0:
                    parse = l.split(' - ')
                    quote = QuoteModel(parse[0], parse[1])
                    quotes.append(quote)
        return quotes
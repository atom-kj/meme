"""Docx ingestor."""

from typing import List
import docx

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel

class DocxIngestor(IngestorInterface):
    """Check the docx file can be parsed. Create a text file. Splits the lines to generate a body and author of quote."""
    
    allowed_extensions = ['docx']
    
    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Take the path and check whether it can be ingested."""
        if not cls.can_ingest(path):
            raise Exception('cannot ingest.')
            
        quotes = []
        doc = docx.Document(path)
        for p in doc.paragraphs:
            if p.text != '':
                parse = p.text.split('-')
                quote = QuoteModel(parse[0], parse[1])
                quotes.append(quote)
        return quotes
        

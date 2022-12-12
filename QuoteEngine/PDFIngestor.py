"""PDF Ingestor."""

from typing import List
import subprocess
import os
import random

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel

class PDFIngestor(IngestorInterface):
    """Check the pdf file can be parsed. Create a text file. Splits the lines to generate a body and author of quote."""
    allowed_extensions = ['pdf']
    def parse(cls, path: str) -> List[QuoteModel]:
        """Take the path and check whether it can be ingested."""
        if not cls.can_ingest(path):
            raise Exception('Cannot ingest.')
        tmp = F'./tmp/{random.randint(0, 1000000)}.txt'
        call = subprocess.call(['pdftotext', path, tmp])
        file = open(tmp, 'r')
        quotes = []
        
        for l in file.readlines():
            l = l.strip('/n/r').strip()
            if len(l) > 0:
                parse = l.split(',')
                quote = QuoteModel(parse[0],parse[1])
                quotes.append(quote)
        file.close()
        os.remove(tmp)
        return quotes
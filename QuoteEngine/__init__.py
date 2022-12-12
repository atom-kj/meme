"""This file import all classes.

Each class is used for representian a quote mode with body and author. 
"""

from .QuoteModel import QuoteModel
from .IngestorInterface import IngestorInterface
from .TextIngestor import TXTIngestor
from .DocxIngestor import DocxIngestor
from .PDFIngestor import PDFIngestor
from .CSVIngestor import CSVIngestor
from .Ingestor import Ingestor
"""Quote Mode class."""

class QuoteModel():
    """class that defines a QuoteMode object, which contains text fields for body and author."""
    
    def __init__(self, quote: str, author: str):
        """initialise quote mode."""
        self.quote = quote
        self.author = author
import random
import os
import requests
import urllib.request
from flask import Flask, render_template, abort, request

# Import Ingestor and MemeEngine classes
from QuoteEngine import QuoteModel
from QuoteEngine import IngestorInterface
from QuoteEngine import TXTIngestor
from QuoteEngine import DocxIngestor
from QuoteEngine import PDFIngestor
from QuoteEngine import CSVIngestor
from QuoteEngine import Ingestor
from MemeEngine import MemeEngine


app = Flask(__name__)

meme = MemeEngine('./static')


def setup():
    """ Load all resources """

    quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
                   './_data/DogQuotes/DogQuotesDOCX.docx',
                   './_data/DogQuotes/DogQuotesPDF.pdf',
                   './_data/DogQuotes/DogQuotesCSV.csv']

    quotes = []
    
    for file in quote_files:
        quotes.append(Ingestor.parse(file))

    images_path = "./_data/photos/dog/"


    imgs = [file for file in images_path]

    return quotes, imgs


quotes, imgs = setup()


@app.route('/')
def meme_rand():
    """ Generate a random meme """

    img = random.choice(imgs)
    quote = random.choice(quotes)
    path = meme.make_meme(img, quote.body, quote.author)
    return render_template('meme.html', path=path)


@app.route('/create', methods=['GET'])
def meme_form():
    """ User input for meme information """
    return render_template('meme_form.html')


@app.route('/create', methods=['POST'])
def meme_post():
    """ Create a user defined meme """


    image_url = request.form.get('image_url')
    body = request.form.get('Body')
    author = request.form.get('Author')
    temp = F'{random.randint(0, 1000000)}.png'
    urllib.request.urlretrieve(image_url, temp)
    path = make_meme(temp, body, author)
    os.remove(temp)
    

    return render_template('meme.html', path=path)


if __name__ == "__main__":
    app.run()
# Meme Generator Project

## Overview

This project build a 'meme generator.' This is a multimedia application to dynamically generate memes, including an image with a overlaid quote. A quote consists of body and author. quotes can be loaded multiple file extensions and through a command line and web interface.

## Main Modules

- [QuoteEngine](./QuoteEngine)
- [MemeEngine](./MemeEngine)

## Packages

- [ABC](https://github.com/python/cpython/blob/main/Lib/abc.py)
- [Argparse](https://github.com/python/cpython/blob/main/Lib/argparse.py)
- [Flask](https://github.com/pallets/flask/)
- [Pandas](https://github.com/pandas-dev/pandas)
- [Python-docx](https://github.com/python-openxml/python-docx)
- [Pillow](https://github.com/python-pillow/Pillow)
- [Requests](https://github.com/psf/requests)
- [Subprocess](https://github.com/python/cpython/blob/main/Lib/subprocess.py)
- [Typing](https://github.com/python/typing)

## Usage

### Flask Interface

- Run `python app.py.`
- Access the webpage via [http://localhost:3000](http://localhost:3000).

### Command Line Interface

- Run `python meme.py,` with the optional CLI arguments:
  --body: string quote body
  --author: string quote author
  --path: path to image file

## Submodules
This project consists of main submodules QuoteEngine and MemeEngine, which handle parsing, selecting, and converting data from various files and create memes. The quote engine is to load and parse quotes from files. Meme engine manipulate and draw text onto images. Data directory stores all data for quotes, photos and lines. 
"# meme" 

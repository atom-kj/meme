"""This module takes path, selects image and quote, create a image."""

import random
from PIL import Image, ImageDraw, ImageFont

class MemeEngine:
    """takes path, selects image and quote, and generate quote image"""
    
    def __init__(self, output_path):
        self.output_path = output_path
        
        @staticmethod
        def get_y(value):
            """get a random y."""
            y_min = 10
            y_max = value - 100
            return random.randint(y_min, y_max)
        
        def make_meme(self, path, text, author, width=500) -> str:
            """create meme from text and author."""
            try:
                img = Image.open(path)
            except Exception as e:
                print(F'Exception: {e}')
            else:
                if width is not None:
                    ratio = width/float(img.size[0])
                    height = int(ratio*float(img.size[1]))
                    img = img.resize((width, height), Image.NEAREST)
                if text and author:
                    message = F'{text}\n{author}'
                    draw = ImageDraw.Draw(img)
                    font = ImageFont.load_default()
                    axis = (10, self.get_rand_y(img.size[1]))
                    draw.text(axis, message, font=font, fill='white')
                
                out_path = F'{self.output_path}/{random.randint(0, 1000000)}.jpg'
                
                img.save(out_path)
                print(F'Saved to {self.output_path}')
                return out_path
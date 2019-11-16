from PIL import Image, ImageFilter, ImageFont, ImageDraw
import os, random

draw = ImageDraw

img = Image.open("meme_img/" + random.choice(os.listdir("meme_img")))

font = ImageFont.load("")

print(img)
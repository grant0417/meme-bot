from PIL import Image, ImageFilter
import os, random

img = Image.open("meme_img/" + random.choice(os.listdir("meme_img")))

print(img)
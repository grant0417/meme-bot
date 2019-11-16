from PIL import Image, ImageFilter, ImageFont, ImageDraw
import os, random, json
import textwrap


def print_text(text, x, y, font, color, shadowcolor):
    draw.text((x - 1, y - 1), text, font=font, fill=shadowcolor)
    draw.text((x + 1, y - 1), text, font=font, fill=shadowcolor)
    draw.text((x - 1, y + 1), text, font=font, fill=shadowcolor)
    draw.text((x + 1, y + 1), text, font=font, fill=shadowcolor)
    draw.text((x, y), text, font=font, fill=color)


img = Image.open("meme_img/" + random.choice(os.listdir("meme_img")))

(width, height) = (img.width // 2, img.height // 2)
height = (500 / width) * height
img = img.resize((500, int(height)))

draw = ImageDraw.Draw(img)
font = ImageFont.truetype("impact.ttf", 40)

file = open("training_data_sample.json", "r")
data = json.load(file)
text = random.choice(data)[1].split('|')

print_text(text[0], 5, 5, font, (255, 255, 255, 255), (0, 0, 0, 255))
print_text(text[1], 5, img.height - 55, font, (255, 255, 255, 255), (0, 0, 0, 255))

img.save("meme" + ".png", "PNG")

print(img)

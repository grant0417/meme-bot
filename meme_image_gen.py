import json
import os
import random
import textwrap
import predict_text_generator

from PIL import Image, ImageFont, ImageDraw


def print_text(draw, text, x, y, font, color, shadowcolor):
    for line in text:
        draw.text((x - 1, y - 1), line, font=font, fill=shadowcolor)
        draw.text((x + 1, y - 1), line, font=font, fill=shadowcolor)
        draw.text((x - 1, y + 1), line, font=font, fill=shadowcolor)
        draw.text((x + 1, y + 1), line, font=font, fill=shadowcolor)
        draw.text((x, y), line, font=font, fill=color)
        y += font.getsize(line)[1]


def make_meme():
    img = Image.open("whale_img/" + random.choice(os.listdir("whale_img")))

    (width, height) = (img.width // 2, img.height // 2)
    height = (500 / width) * height
    img = img.resize((500, int(height)))

    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("impact.ttf", 40)

    top, bottom = predict_text_generator.gen_sentence(input())

    top = textwrap.wrap(top.upper(), width=27)
    bottom = textwrap.wrap(bottom.upper().split("\n")[0], width=27)

    print_text(draw, top, 3, 0, font, (255, 255, 255, 255), (0, 0, 0, 255))
    print_text(draw, bottom, 3, img.height - font.getsize(bottom[0])[1] * len(bottom) - 5, font,
               (255, 255, 255, 255), (0, 0, 0, 255))

    img.save("meme" + ".png", "PNG")

    print(img)


if __name__ == "__main__":
    make_meme()

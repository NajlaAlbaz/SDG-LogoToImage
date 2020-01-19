# reference: https://pybit.es/pillow-intro.html

from PIL import Image
import os

current_dir = os.getcwd()
logo_file = 'logo.png'

for f in os.listdir(current_dir):
    if f.endswith(".JPG"):
        img = Image.open(f)
        logo = Image.open(logo_file)
        position = (0, (img.height - logo.height))
        img.paste(logo, position, logo)
        img.save(f'{f[:-4]}_done.jpg')
    else:
        continue
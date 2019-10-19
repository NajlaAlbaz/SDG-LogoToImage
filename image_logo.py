# reference: https://pybit.es/pillow-intro.html

from PIL import Image
import os

current_dir = os.getcwd()
logo_file = 'logo.png'


for f in os.listdir(current_dir):
    if f.endswith(".jpg"):
        img = Image.open(f)
        logo = Image.open(logo_file)
        new_height = img.height // 5
        new_width = new_height * logo.width // logo.height
        new_logo = logo.resize((new_width, new_height), Image.ANTIALIAS)
        position = (0, (img.height - new_logo.height))
        img.paste(new_logo, position, new_logo)
        img.save(f'{f[:-4]}_done.jpg')
    else:
        continue
        

# reference: https://haptik.ai/tech/putting-text-on-image-using-python/

from PIL import Image, ImageDraw, ImageFont
import os

#   Load preferable font
font = ImageFont.truetype('Futura Bold font.ttf', size=180)
#   Size of image
(x, y) = (3508, 2650)
#   Output color
color = 'rgb(232, 73, 67)'
#   List of names
#For female attendees
F_attendees = ["Attendee 1", "Attendee 2"]
#For male attendees
M_attendees = ["Attendee 3", "Attendee 4"]

#   Loop through names and write/save
for i in F_attendees:
    img = Image.open('certificate_F.png')
    draw = ImageDraw.Draw(img)
    #   Size of text
    w, h = draw.textsize(i, font)
    draw.text(((x-w)/2, (y-h)/2), i, fill=color, font=font)
    img.save(f'{i}_certificate.png')

    for i in M_attendees:
        img = Image.open('certificate_M.png')
        draw = ImageDraw.Draw(img)
        #   Size of text
        w, h = draw.textsize(i, font)
        draw.text(((x - w) / 2, (y - h) / 2), i, fill=color, font=font)
        img.save(f'{i}_certificate.png')
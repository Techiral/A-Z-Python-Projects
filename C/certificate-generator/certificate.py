#Sourasish Certificate Generator
import pandas as pd
from PIL import Image, ImageDraw, ImageFont

df = pd.read_excel('names.xlsx')

img = Image.open('certificate_template.png')

nameFont = ImageFont.truetype('fontss.ttf', 110)

color = (0, 0, 0)  # black

for index, row in df.iterrows():
    Name = row['name']
    College = row['college']
    
    cert = Image.new('RGB', img.size, (255, 255, 255))
    
    cert.paste(img, (0, 0))
    
    draw = ImageDraw.Draw(cert)
    name_x, name_y = 1200, 940
    stream_x, stream_y = 900, 1030
    draw.text((name_x, name_y), Name, font=nameFont, fill=color, anchor='mm')
    draw.text((stream_x, stream_y), College, font=nameFont, fill=color, anchor='mm')
    
    cert.save(f'{Name}_certificate.png')
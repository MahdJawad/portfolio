from PIL import Image, ImageDraw, ImageFont
import os

# Créer une image blanche de 32x32 pixels
img = Image.new('RGB', (32, 32), 'white')
draw = ImageDraw.Draw(img)

# Utiliser une police simple pour les initiales
try:
    font = ImageFont.truetype("arial.ttf", 16)
except:
    font = ImageFont.load_default()

# Dessiner les initiales en noir
text = "MJ"
text_bbox = draw.textbbox((0, 0), text, font=font)
text_width = text_bbox[2] - text_bbox[0]
text_height = text_bbox[3] - text_bbox[1]

# Centrer le texte
x = (32 - text_width) // 2
y = (32 - text_height) // 2

draw.text((x, y), text, font=font, fill='black')

# Créer le dossier public s'il n'existe pas
os.makedirs('public', exist_ok=True)

# Sauvegarder l'image en format .ico
img.save('public/favicon.ico', format='ICO', sizes=[(32, 32)]) 
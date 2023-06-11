from PIL import Image

img = Image.open('map1.jpg')
img = img.resize((1920, 1080))
img.save('map1.jpg')
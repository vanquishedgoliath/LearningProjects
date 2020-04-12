from PIL import Image
from PIL import ImageColor

print(ImageColor.getcolor('blue', 'RGBA'))

im = Image.new('RGBA', (100, 100))

im.getpixel((0, 0))

for x in range(100):
    for y in range(50):
        im.putpixel((x, y), (210, 210, 210))

for i in range(100):
    for j in range(50, 100):
        im.putpixel((i, j), ImageColor.getcolor('darkgrey', 'RGBA'))

im.save('putPixel.png')
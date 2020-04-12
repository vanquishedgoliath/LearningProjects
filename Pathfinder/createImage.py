import numpy as np
from PIL import Image


def set_pixel_values_in_map(color_array, image):

    image_array = np.transpose(color_array)

    for index, elevation in np.ndenumerate(image_array):
        pixelcolor = int(elevation)
        image.putpixel(index, (pixelcolor, pixelcolor, pixelcolor))

    return image, image_array


# Create png file
def create_Image(color_array):

    image = Image.new('RGB', (len(color_array), len(color_array)), 'black')
    image, image_array = set_pixel_values_in_map(color_array, image)
    image.save('map.png')
    return image, image_array


# if __name__ == '__main__':

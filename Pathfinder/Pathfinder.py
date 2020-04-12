import numpy as np
from PIL import Image
from PIL import ImageColor
import text2array as text
import createImage as create
import greedywalk as greedy

def main():
    # this imports text elevations into an array
    elevation_array = text.file_to_array()

    # gets minimum and maximum elevation values
    minimum, maximum = text.find_min_and_max_elevation(elevation_array)

    # calculates the range of elevation values in the array
    range_of_elevation, range_increment = text.calculate_elevation_ranges(minimum, maximum)

    # calculates color range values based on elevation range values
    color_ranges = text.calculate_color_ranges(range_of_elevation)

    # creates duplicate array of pixel values to create image with later
    color_array = text.converts_to_array_of_colors(elevation_array, range_increment, color_ranges, minimum)

    # convert pixel values array into an image
    # Image objects in the Pillow library, when converted from an array are read in a transposed manner than made in this program
    image, image_array = create.create_Image(color_array)

    # create transposed elevation array, so it mimics the image array.  The image array is a bunch of pixel values.
    elevation_array = text.file_to_array()
    greedy.find_lowest_starting_elevation(elevation_array)
    greedy.greedy_walk(elevation_array)



if __name__ == '__main__':
    main()
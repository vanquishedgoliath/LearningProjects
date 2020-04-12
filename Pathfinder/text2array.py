import numpy as np


def file_to_array():

    elevation_array = np.loadtxt(fname="elevation_small.txt", dtype=int)

    return elevation_array


# you need to find the min and max elevations:
# then you need to set the highest elevation at ImageColor(255, 255, 255) and lowest elevation at ImageColor(0, 0, 0)

def find_min_and_max_elevation(elevation_array):

    min_elevation = np.min(elevation_array)
    max_elevation = np.max(elevation_array)
    return min_elevation, max_elevation


def calculate_elevation_ranges(min_elevation, max_elevation):

    range_of_elevation = int((max_elevation - min_elevation) / 255)
    range_increment = int((max_elevation - min_elevation) / range_of_elevation)
    return range_of_elevation, range_increment


def calculate_color_ranges(range_of_elevation):

    # max_elevation_pixel = 255
    # min_elevation_pixel = 0
    color_ranges = int(255/range_of_elevation)
    return color_ranges


def converts_to_array_of_colors(elevation_array, range_increment, color_ranges, min_elevation):

    color = 0

    for elevation in np.nditer(elevation_array, op_flags=['readwrite'], op_dtypes=['int'], order='K'):

        color = int(((elevation[...] - min_elevation) / range_increment) * color_ranges)

        # This if statement is to assign pixel values for any range value that is greater than the max elevation
        # This is needed, because not every elevation range will be an even integer, which divides nicely
        if color <= 255:
            elevation[...] = color
        else:
            elevation[...] = 255

    return elevation_array



# if __name__ == "__main__":
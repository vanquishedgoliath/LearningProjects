import numpy as np
from PIL import Image


def find_lowest_starting_elevation(elevation_array):

    # make array in the same layout as image class array
    image_elevation_array = np.transpose(elevation_array)
    starting_pixel = int(image_elevation_array[0][299])
    return elevation_array, starting_pixel


def index_value_of_next_elevation(next_elevation_value, num1, num2, num3):

    if next_elevation_value is num1:
        index = True
        return index
    elif next_elevation_value is num2:
        index = False
        return index
    else:
        index = None
        return index


def least_change_in_elevation(current_elevation, elevation_1, elevation_2, elevation_3):

    num1 = abs(current_elevation - elevation_1)
    num2 = abs(current_elevation - elevation_2)
    num3 = abs(current_elevation - elevation_3)
    next_elevation_value = min(num1, num2, num3)
    next_elevation_value = index_value_of_next_elevation(next_elevation_value, num1, num2, num3)
    return next_elevation_value


def next_three_elevations(elevation_array, i, midpoint):

    try:
        elevation_1 = elevation_array[midpoint - 1][i + 1]
    except IndexError:
        elevation_1 = 0

    try:
        elevation_2 = elevation_array[midpoint][i + 1]
    except IndexError:
        elevation_2 = 0

    try:
        elevation_3 = elevation_array[midpoint + 1][i + 1]
    except IndexError:
        elevation_3 = 0

    return elevation_1, elevation_2, elevation_3


def next_position_in_array(elevation_array, i, midpoint, next_elevation, image):

    try:
        if next_elevation is True:
            next_elevation = elevation_array[midpoint - 1][i + 1]
            midpoint = midpoint - 1
            draw_path(image, i, midpoint)
        elif next_elevation is False:
            next_elevation = elevation_array[midpoint][i + 1]
            draw_path(image, i, midpoint)
        else:
            next_elevation = elevation_array[midpoint + 1][i + 1]
            midpoint = midpoint + 1
            draw_path(image, i, midpoint)
    except IndexError:
        return next_elevation, midpoint

    return next_elevation, midpoint


def draw_path(image, i, midpoint):

    image.putpixel((i, midpoint), (0, 180, 180))
    return


def greedy_walk(elevation_array):

    midpoint = 0
    current_elevation = elevation_array[0][0]
    image = Image.open('map.png')
    # take away the minus 1 otherwise the last pixel won't be drawn to
    for midpoint in range(len(elevation_array)):
        if midpoint == 599:
            break
        for i in range(len(elevation_array)):
            # try statements stop index errors from occurring when checking for elevations outside of the image
            elevation_1, elevation_2, elevation_3 = next_three_elevations(elevation_array, i, midpoint)
            # this calculates the next elevation lowest changed elevation, and returns a flag to determine next elevation index
            next_elevation = least_change_in_elevation(current_elevation, elevation_1, elevation_2, elevation_3)
            # if statement determines the next elevation in the array to check and updates the "midpoint"
            next_elevation, midpoint = next_position_in_array(elevation_array, i, midpoint, next_elevation, image)
            # this updates the loop so you'll keep checking the next pixel
            current_elevation = next_elevation
    # this statement was originally inside the for loop and it was real fun watching the computer open and save a png 600 times
    image.save('map.png')
    return image

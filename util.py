import matplotlib.pyplot as plt
from PIL import Image, ImageOps
import numpy as np

def get_grayscale(image):
    image_copy = image.copy()
    return ImageOps.grayscale(image_copy)


def get_square(image, i, j):
    width, height = image.size

    neighbors = [[(-1, -1), (-1, 0), (-1, 1)], [(0, -1), (0, 0), (0, 1)],
                 [(1, -1), (1, 0), (1, 1)]]

    square = np.zeros((9, 9))

    for i in range(9):
        for j in range(9):
            di, dj = neighbors[i, j]
            square[i, j] = image[(di + i) % height, (dj + j) % width]

    return square


def get_channels(pixels):
    # Arrays for red, green, and blue.
    reds, greens, blues = [], [], []

    for red, green, blue in pixels:
        reds.append(red)
        greens.append(green)
        blues.append(blue)

    return reds, greens, blues

import matplotlib.pyplot as plt
from PIL import Image, ImageOps
import numpy as np
import math


def distance_pixels(pixel_a, pixel_b):
    x1, y1, z1 = pixel_a
    x2, y2, z2 = pixel_b
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)


def get_grayscale(image):
    image_copy = image.copy()
    return ImageOps.grayscale(image_copy)


def get_pixel_patch(image, i, j):
    width, height = image.size

    neighbors = [[(-1, -1), (-1, 0), (-1, 1)], [(0, -1), (0, 0), (0, 1)],
                 [(1, -1), (1, 0), (1, 1)]]

    pixel_patch = np.zeros((3, 3))

    for i in range(3):
        for j in range(3):
            di, dj = neighbors[i, j]
            pixel_patch[i, j] = image[(di + i) % height, (dj + j) % width]

    return pixel_patch


def get_channels(pixels):
    # Arrays for red, green, and blue.
    reds, greens, blues = [], [], []

    for red, green, blue in pixels:
        reds.append(red)
        greens.append(green)
        blues.append(blue)

    return reds, greens, blues

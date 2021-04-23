
import numpy as np
import math
import random
from util import get_channels

# Find min and max of plot of pixels.
def find_min_max(reds, greens, blues):
    max_arr = [max(reds), max(greens), max(blues)]
    min_arr = [min(reds), min(greens), min(blues)]
    return min_arr, max_arr


def distance_pixels(pixel_a, pixel_b):
    # https://slideplayer.com/slide/260326/1/images/13/Distance+Formula+in+Three+Dimensions.jpg
    x1, y1, z1 = pixel_a
    x2, y2, z2 = pixel_b
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)


def find_min_index(pixel, center_points):
    min_dist = math.inf
    min_index = -1

    for i in range(len(center_points)):
        center_point = center_points[i]
        if distance_pixels(center_point, pixel) < min_dist:
            min_dist = distance_pixels(center_point, pixel)
            min_index = i

    return min_index


def k_means(pixels, k=5):
    reds, greens, blues = get_channels(pixels)
    min_arr, max_arr = find_min_max(reds, greens, blues)
    center_points = [
        (
            random.randint(min_arr[0], max_arr[0]),  # Red (x)
            random.randint(min_arr[1], max_arr[1]),  # Green (y)
            random.randint(min_arr[2], max_arr[2])  # Blue (z)
        ) for i in range(k)
    ]

    point_to_cluster = [0] * len(pixels)
    prev_point_to_cluster = None

    while True:
        prev_point_to_cluster = point_to_cluster
        cluster_size = [0] * len(center_points)

        for i in range(len(pixels)):
            min_index = find_min_index(pixels[i], center_points)
            point_to_cluster[i] = min_index
            cluster_size[min_index] += 1

        if prev_point_to_cluster == point_to_cluster:
            break

        center_points = [(0, 0, 0)] * k

        for i in range(len(point_to_cluster)):
            x, y, z = pixels[i]
            cx, cy, cz = center_points[i]

            center_points[i] = (cx + x / cluster_size[i],
                                cy + y / cluster_size[i],
                                cz + z / cluster_size[i])

    return point_to_cluster
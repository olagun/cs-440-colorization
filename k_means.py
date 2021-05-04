
import numpy as np
import math
import random
from util import get_channels, distance_pixels

def find_range(pixels):
  """
  Find min and max of plot of pixels.
  """
  reds, greens, blues = get_channels(pixels)
  max_arr = [max(reds), max(greens), max(blues)]
  min_arr = [min(reds), min(greens), min(blues)]
  return min_arr, max_arr

def find_mean_index(pixel, means):
    """
    Finds the mean index that a specific pixel belongs to.
    """

    min_dist, min_index = math.inf, -1

    for i in range(len(means)):
        if distance_pixels(means[i], pixel) < min_dist:
            min_dist = distance_pixels(means[i], pixel)
            min_index = i

    return min_index


def k_means(pixels, k=5):
    print("Starting K Means")

    min_arr, max_arr = find_range(pixels)
    
    means = np.array([
        [
            random.randint(min_arr[0] + 1, max_arr[0] - 1), # Red
            random.randint(min_arr[1] + 1, max_arr[1] - 1), # Green
            random.randint(min_arr[2] + 1, max_arr[2] - 1) # Blue
         ] for i in range(k)
    ])

    pixel_to_mean = [0] * len(pixels)

    for i in range(3):
        changes = 0
        mean_size = [0] * len(means)

        for i in range(len(pixels)):
            index = find_mean_index(pixels[i], means)

            if index != pixel_to_mean[i]:
              changes += 1

            mean_size[index] += 1
            pixel_to_mean[i] = index

        if changes == 0:
          break

        means = np.zeros((k, 3))

        for i in range(len(pixel_to_mean)):
            m_index = pixel_to_mean[i]
            means[m_index] += np.array(pixels[i]) / mean_size[m_index]

    print("Finished K Means")
    return means, pixel_to_mean
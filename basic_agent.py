from PIL import Image
from k_means import k_means
import math
from util import get_pixel_patch, distance_pixels

class BasicAgent:
    def __init__(self, image):
      self.color_image = image
      self.grayscale_image = self.get_grayscale_image(image)

    def get_grayscale_image(self, image):
      """
      Converts a color image into a gray image.
      """
      grayscale_image = image.copy()
      grayscale_pixels = grayscale_image.load()
      width, height = image.size

      for x in range(width):
        for y in range(height):
          r, g, b = grayscale_pixels[x, y]

          grayscale_pixels[x, y] = (
            math.floor(0.21 * r + 0.72 * g + 0.07 * b),
            math.floor(0.21 * r + 0.72 * g + 0.07 * b),
            math.floor(0.21 * r + 0.72 * g + 0.07 * b)
          )
      
      return grayscale_image

    def get_k_colors(self):
      """
      Gets the 5 representative colors as an array of rgb tuples.

      e.g. [(0, 0, 0), (255, 255, 255), ...]
      """
      pixels = []
      width, height = self.color_image.size
      half_width = width // 2

      for row in range(height):
        for col in range(0, half_width):
          pixels.append(self.color_image[row][col])
      
      return k_means(pixels)

    def get_six_most_similar(self, pixel_patch):
      """
      Returns the indices of the six most similar
      pixel patches to `pixel_patch` inside of
      the left half of `self.grayscale_image`.
      """
      pixels_with_distance = []

      width, height = self.grayscale_image.size
      half_width = width // 2

      # Find the distance for every pixel
      for row in range(height):
        for col in range(half_width):
          pixel = self.grayscale_image[row][col]
          dist = self.compare_pixel_patches(
            get_pixel_patch(self.grayscale_image, row, col),
            pixel_patch,
          )
          pixels_with_distance.append((dist, pixel))

      # Sort by the first tuple item (distance).
      pixels_with_distance.sort(key=lambda x: x[0])

      # Get the six most similar pixels.
      six_most_similar = pixels_with_distance[:6]

      # Return only the first tuple item.
      return list(map(lambda x: x[0], six_most_similar))

    def compare_pixel_patches(self, patch_a, patch_b):
      """
      Finds the number difference between two pixel patches.
      """
      difference = 0

      for row in range(len(patch_a)):
        for col in range(len(patch_a[0])):
          difference += abs(patch_a[row][col] - patch_b[row][col])

      return difference

    def replace_nearest_color(self):
      """
      Replaces each pixel on left half ofimage
      with closest cluster representative.
      """
      """read in real self.image and pit version output
      into self.rep image."""
      color_image = self.color_image.load()
      width, height = self.color_image.size
      half_width = width // 2

      rep_colors, _ = k_means(self.color_image.getdata())


      for x in range(half_width):
        for y in range(height):
          pixel = color_image[x, y]
          
          min_index = 0
          min_value = math.inf
          
          for i in range(len(rep_colors)):
            dist = distance_pixels(pixel, rep_colors[i])

            if dist < min_value:
              min_value = dist
              min_index = i
            
          color_image[x, y] = tuple(rep_colors[min_index].astype(int))

    def run(self):
      # Iterate through the right half of the image
      width, height = self.grayscale_image.size
      half_width = width / 2

      for row in range(height):
        for col in range(half_width):
          col = half_width + col


    
if __name__ == "__main__":
    image = Image.open("color_photo2.jpg")
    basic_agent = BasicAgent(image)

    # Convert image to grayscale.
    basic_agent.grayscale_image.save("gray_photo.png")

    basic_agent.replace_nearest_color()
    basic_agent.color_image.save("rep_photo.png")


    


    
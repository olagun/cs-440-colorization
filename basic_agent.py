from PIL import Image
from k_means import k_means
from util import get_square

class BasicAgent:
    """
    Given a 3x3 patch of grayscale pixels, we try to use these 9 values to reconstruct the original (r, g, b) value of the middle pixel.
    """
    def __init__(self, image):
      self.representative_image = image
      self.grayscale_image = self.get_grayscale_image(image)

    def get_grayscale_image(self, image):
      """
      Converts a color image into gray using the
      following formula: 

      Gray(r, g, b) = 0.21r + 0.72g + 0.07b
      """
      grayscale_image = image.copy()
      width, height = image.size

      for row in range(height):
        for col in range(width):
          r, g, b = self.grayscale_image[row][col]
          image[row][col] = (
            0.21 * r + 0.72 * g + 0.07 * b,
            0.21 * r + 0.72 * g + 0.07 * b,
            0.21 * r + 0.72 * g + 0.07 * b
          )
        
      return grayscale_image

    def get_k_colors(self):
      """
      Gets the 5 representative colors as 
      an array of tuples.

      e.g. [(0, 0, 0), (255, 255, 255), ...]
      """
      pixels = self.image.getdata()
      return k_means(pixels)

    def get_six_most_similar(self, square):
      """
      Returns the coordinates of the six most similar squares
      to `square` in the left side of `self.grayscale_image`.
      """
      return []

    def compare_squares(self, square_a, square_b):
      """
      Finds the number difference between two
      squares.
      """
      return 0

    def replace_nearest_color(self):
      """
      Replaces each pixel on left half ofimage
      with closest cluster representative.
      """
      """read in real self.image and pit version output
      into self.rep image."""
      pass

    def run(self):
      # Iterate through the right half of the image
      width, height = self.grayscale_image.size
      half_width = width / 2

      for row in range(height):
        for col in range(half_width):
          col = half_width + col

    
if __name__ == "__main__":
    image = Image.open("color_photo.jpg")
    basic_agent = BasicAgent(image)
    
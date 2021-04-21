import matplotlib.pyplot as plt
from PIL import Image

def graph_image(image_path):
  figure = plt.figure()
  plot = figure.add_subplot(projection='3d')

  # Opens image.
  image = Image.open(image_path)

  # Returns a flattened list of all pixels.
  pixels = image.getdata()

  # Arrays for red, green, and blue.
  reds, greens, blues = [], [], []

  for red, green, blue in pixels:
    reds.append(red)
    greens.append(green)
    blues.append(blue)

  # Scatter plot of reds, greens, and blues.
  plot.scatter(reds, greens, blue, marker="^", color="blue")

  # Add labels.
  plot.set_xlabel('Red')
  plot.set_ylabel('Green')
  plot.set_zlabel('Blue')

  # Show plot.
  plt.show()

graph_image("color_photo.jpg")
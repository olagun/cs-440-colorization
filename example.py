from PIL import Image
# from graph import graph_k_means

# Opens image
image = Image.open("color_photo.jpg")

# Get image size
width, height = Image.size

# Loads pixels
image.load()

# Iterates through pixels
for i in range(width):
  for j in range(height):
    print(image[i, j])

# Modifies pixels
for i in range(width):
  for j in range(height):
    red, green, blue = 255, 255, 255
    image[i, j] = (red, green, blue)

# Saves image
image.save("photo.png")
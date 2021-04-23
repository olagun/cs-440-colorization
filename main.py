from PIL import Image
from graph import graph_k_means

# Opens image
image = Image.open("color_photo.jpg")

# Pixels
pixels = list(image.getdata())[:50]

# Graph K-Means
graph_k_means(pixels)

# Display Graph
# graph_image("color_photo.jpg")

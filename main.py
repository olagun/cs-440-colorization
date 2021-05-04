from PIL import Image
from graph import graph_k_means

# Opens image
image = Image.open("color_photo2.jpg")

# Pixels
pixels = list(image.getdata())[:600]

# Graph K-Means
graph_k_means(pixels)

# Display Graph
# graph_image("color_photo.jpg")

# import cv2
# import numpy as np
# import matplotlib.pyplot as plt

# img = cv2.imread("color_photo2.jpg")
# img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# pixel_values = img.reshape((-1, 3))
# # convert to float
# pixel_values = np.float32(pixel_values)
# criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 100, 0.2)
# k = 5
# _, labels, (centers) = cv2.c(pixel_values, k, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)

# # convert back to 8 bit values
# centers = np.uint8(centers)

# # flatten the labels array
# labels = labels.flatten()

# segmented_image = centers[labels.flatten()]

# segmented_image = segmented_image.reshape(img.shape)
# # show the image
# plt.imshow(segmented_image)
# plt.show()
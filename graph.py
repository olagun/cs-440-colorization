import matplotlib.pyplot as plt
from util import get_channels
from k_means import k_means

def graph_image(pixels):
    figure = plt.figure()
    plot = figure.add_subplot(projection='3d')

    # Arrays for red, green, and blue.
    reds, greens, blues = get_channels(pixels)

    # Scatter plot of reds, greens, and blues.
    plot.scatter(reds, greens, blues, marker="^", color="blue")

    # Add labels.
    plot.set_xlabel('Red')
    plot.set_ylabel('Green')
    plot.set_zlabel('Blue')

    # Show plot.
    plt.show()


def graph_k_means(pixels):
    _, clusters = k_means(pixels)

    figure = plt.figure()
    plot = figure.add_subplot(projection='3d')

    colors = ["blue", "red", "yellow", "green", "purple"]

    print("Starting Graph")
    for i in range(len(pixels)):
        r, g, b = pixels[i]
        cluster = clusters[i]
        plot.scatter([r], [g], [b], marker="^", color=colors[cluster])
    print("Ending Graph") 
    plot.set_xlabel('Red')
    plot.set_ylabel('Green')
    plot.set_zlabel('Blue')

    plt.show()
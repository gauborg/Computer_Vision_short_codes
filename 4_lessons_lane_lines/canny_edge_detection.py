import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import cv2

image = mpimg.imread('exit-ramp.jpg')

gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)  # grayscale conversion

# this is a gaussian smoothing step
kernel_size = 5
blur_gray = cv2.GaussianBlur(gray, (kernel_size, kernel_size), 0)

# define parameters for Canny and run
low_threshold = 50
high_threshold = 150

edges = cv2.Canny(blur_gray, low_threshold, high_threshold)

# display the image
plt.imshow(edges, cmap = 'Greys_r')
plt.show()
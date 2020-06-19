import os
import numpy as np
import cv2
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

def normalize_img(img):

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    pixel_value_color = img[500][600]
    print(pixel_value_color)
    print(np.sum(pixel_value_color))
    pixel_value_gray = gray[500][600]
    print(pixel_value_gray)

    normalized_img = np.sum((img/3), axis = 3, keepdims = True)

    return normalize_img

image = mpimg.imread("my_test.jpg")
color_img = normalize_img(image)

plt.imshow(color_img, cmap = 'gray')
plt.show()
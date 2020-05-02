import os
import numpy as np
import cv2
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import pickle


def saturation_select(img, thresh = (0,255)):

    hls = cv2.cvtColor(img, cv2.COLOR_RGB2HLS)

    # 2. apply threshold to s channel
    s_channel = hls[:,:,2]

    # 3. create empty array to store the binary output and apply threshold
    binary_image = np.zeros_like(s_channel)
    binary_image[(s_channel > thresh[0]) & (s_channel <= thresh[1])] = 1
    # plt.imshow(binary_image)
    # plt.show()

    return binary_image


def abs_sobel(img, orient = 'x', sobel_kernel = 3, thresh = (0,255)):

    # 1. Applying the Sobel depending on x or y direction and getting the absolute value
    if (orient == 'x'):
        abs_sobel = np.absolute(cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize = sobel_kernel))
    if (orient == 'y'):
        abs_sobel = np.absolute(cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize = sobel_kernel))

    # 2. Scaling to 8-bit and converting to np.uint8
    scaled_sobel = np.uint8(255*abs_sobel/np.max(abs_sobel))

    # 3. Create mask of '1's where the sobel magnitude is > thresh_min and < thresh_max
    binary_image = np.zeros_like(scaled_sobel)
    binary_image[(scaled_sobel > thresh[0]) & (scaled_sobel <= thresh[1])] = 1

    return binary_image



def combined(img):

    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    
    s_binary = saturation_select(img, thresh = (100,255))
    plt.imshow(s_binary)
    plt.show()

    print(s_binary.shape)


    gradex = abs_sobel(gray, orient = 'x', sobel_kernel = 9, thresh = (20,100))
    print(gradex.shape)


    combined = np.zeros_like(s_binary)
    combined[((s_binary == 1) | (gradex == 1))] = 1
    cv2.imwrite('output.jpg', combined)


img = mpimg.imread('test3.jpg')

combined(img)
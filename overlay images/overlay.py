import os
import numpy as np
import cv2
import matplotlib.pyplot as plt
import matplotlib.image as mpimg



img1 = mpimg.imread('test.jpg')
img2 = mpimg.imread('test-thresholded.jpg')

print(img1.shape)
print(img2.shape)


img2_resize = cv2.resize(img2, None, fx = 0.25, fy = 0.25, interpolation = cv2.INTER_LINEAR)



print(img2_resize.shape)

print(img2_resize[10][20])




'''
height, width = (768 , 1024)

blank_image = np.zeros((height, width, 3), np.uint8)
blank_image[:, 0:width] = (255, 0, 0) # (B, G, R)

x_offset = int((width - img.shape[1])/2)
y_offset = int((height - img.shape[0])/2)

blank_image[ y_offset:y_offset+img.shape[0], x_offset:x_offset+img.shape[1]] = img

plt.imshow(cv2.cvtColor(blank_image, cv2.COLOR_BGR2RGB))
plt.show()

'''
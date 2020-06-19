import os
import numpy as np
import cv2

a = np.array([1, 2, 3])

print("a = ", a)

b = np.array([10, 20, 30])

print("b = ", b)

resized = cv2.addWeighted(a, 1, b, 0.1, 0)


print(resized)
print(resized.reshape(1, 3))

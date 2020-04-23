import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

image = mpimg.imread('test.jpg')
print('This image is:', type(image), 'with dimensions:', image.shape)

# Grab the x and y sizes and make a copy of the image
ysize = image.shape[0]
print(ysize)
xsize = image.shape[1]

# Note: always make a copy rather than simply using "="

color_select = np.copy(image)

# define our color selection criteria
red_threshold = 200
blue_threshold = 200
green_threshold = 200

rgb_threshold = [red_threshold, green_threshold, blue_threshold]

# identify pixels below threshold

thresholds = (image[:,:,0]< rgb_threshold[0]) \
            | (image[:,:,1] < rgb_threshold[1]) \
            | (image[:,:,2] < rgb_threshold[2])

color_select[thresholds] = [0, 0, 0]

# Display the image
plt.imshow(color_select)
plt.show()

# Uncomment the following code if you are running the code locally and wish to save the image
mpimg.imsave("test-after.png", color_select)

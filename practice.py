import cv2
import numpy as np

# Load the image
img = cv2.imread('Flower.JPG')

# Convert the image to grayscale
gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Invert the image
inverted_image = 255 - gray_image

blurred_image = cv2.GaussianBlur(inverted_image, (21, 21), 0)

blended_image = cv2.divide(gray_image, 255 - blurred_image, scale=256)

equalized_image = cv2.equalizeHist(blended_image)


kernel = np.array([[-1,-1,-1], [-1,9,-1], [-1,-1,-1]])
sharpened_image = cv2.filter2D(equalized_image, -1, kernel)


# Display the resulting image

cv2.imwrite('pencil_sketch.jpg', blended_image)

import cv2
import numpy as np

# Load an image
image = cv2.imread('input_image.jpg')

# Convert the image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply Gaussian blur to the grayscale image
blurred_image = cv2.GaussianBlur(gray_image, (15, 15), 0)

# Apply edge detection using the Canny algorithm
edges = cv2.Canny(blurred_image, threshold1=30, threshold2=70)

# Display the original, blurred, and edge-detected images
cv2.imshow('Original Image', image)
cv2.imshow('Blurred Image', blurred_image)
cv2.imshow('Edge Detection', edges)

# Exit the program on any key press
cv2.waitKey(0)
cv2.destroyAllWindows()


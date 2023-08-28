import cv2
import numpy as np

# Load the input image and the background image
input_image = cv2.imread('input_image.jpg')
background_image = cv2.imread('background_image.jpg')

# Convert the images to the same size
background_image = cv2.resize(background_image, (input_image.shape[1], input_image.shape[0]))

# Convert the input image to grayscale
gray_image = cv2.cvtColor(input_image, cv2.COLOR_BGR2GRAY)

# Apply thresholding to create a mask of the object
_, mask = cv2.threshold(gray_image, 200, 255, cv2.THRESH_BINARY)

# Invert the mask to select the background
mask_inv = cv2.bitwise_not(mask)

# Extract the object from the input image
object_removed = cv2.bitwise_and(input_image, input_image, mask=mask_inv)

# Extract the background from the background image
background_extracted = cv2.bitwise_and(background_image, background_image, mask=mask)

# Combine the object and background to get the final image
final_image = cv2.add(object_removed, background_extracted)

# Display the original input image and the final image
cv2.imshow('Input Image', input_image)
cv2.imshow('Final Image', final_image)

# Exit the program on any key press
cv2.waitKey(0)
cv2.destroyAllWindows()


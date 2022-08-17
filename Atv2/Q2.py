#MÉTODO DE ROTAÇÃO
# Python program to explain cv2.rotate() method
 
# importing cv2
import cv2
 
# path
path = r'C:\\Users\\Pichau\\Downloads\\lukita.jpg'
 
# Reading an image in default mode
src = cv2.imread(path)
 
# Window name in which image is displayed
window_name = 'Image'
 
# Using cv2.rotate() method
# Using cv2.ROTATE_90_CLOCKWISE rotate
# by 90 degrees clockwise
image = cv2.rotate(src, cv2.ROTATE_90_CLOCKWISE)
 
# Displaying the image
cv2.imshow(window_name, image)
cv2.waitKey(0)
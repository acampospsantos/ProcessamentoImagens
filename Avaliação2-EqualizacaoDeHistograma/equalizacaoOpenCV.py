from __future__ import print_function
import cv2 as cv
import argparse

# Loads an image
parser = argparse.ArgumentParser(description='Code for Histogram Equalization tutorial.')
parser.add_argument('--input', help='Path to input image.', default='mergulhador.jpg')
args = parser.parse_args()

# ...Loads an image
src = cv.imread(cv.samples.findFile(args.input))
if src is None:
    print('Could not open or find the image:', args.input)
    exit(0)

# Convert the original image to grayscale = Converte a imagem original para o tom cinza
src = cv.cvtColor(src, cv.COLOR_BGR2GRAY)
# Equalize the Histogram by using the OpenCV function cv::equalizeHist = Aplica a equalização do histograma com a função cv::equalizeHist 
dst = cv.equalizeHist(src)

# Display the source and equalized images in a window. = Exibe ambas as imagens (original e equalizada):
cv.imshow('Source image', src)
cv.imshow('Equalized Image', dst)

cv.waitKey()
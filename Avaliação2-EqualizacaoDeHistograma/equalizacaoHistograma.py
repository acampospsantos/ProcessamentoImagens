from __future__ import print_function
from __future__ import division
import cv2 as cv
import numpy as np
import argparse

# Função 
def invert(img, name):
    img = abs(255 - img)
    cv.imwrite(name, img)

# Loads an image...
parser = argparse.ArgumentParser(description='Code for Histogram Equalization.')
parser.add_argument('--input', help='Path to input image.', default='fazenda.jpg')
args = parser.parse_args()

# ...Loads an image
src = cv.imread(cv.samples.findFile(args.input))
dst = cv.imread(cv.samples.findFile(args.input))
if src is None:
    print('Could not open or find the image:', args.input)
    exit(0)

# Convert the original image to grayscale = Converte a imagem original para o tom cinza
src = cv.cvtColor(src, cv.COLOR_BGR2GRAY)

# Equalize Histogram = Equalização de Histograma 
img_array = np.asarray(src)
histogram_array = np.bincount(img_array.flatten(), minlength=256)
num_pixels = np.sum(histogram_array)
histogram_array = histogram_array/num_pixels
chistogram_array = np.cumsum(histogram_array)
transform_map = np.floor(255 * chistogram_array).astype(np.uint8)
img_list = list(img_array.flatten())
eq_img_list = [transform_map[p] for p in img_list]
eq_img_array = np.reshape(np.asarray(eq_img_list), img_array.shape)
dst = eq_img_array

# Display the source and equalized images in a window = Exibe ambas as imagens (original e equalizada):
cv.imshow('Source Image', src) #ANTES DA EQUALIZAÇÃO DO HISTORIOGRAMA
cv.imshow('Equalized Image', dst) #DEPOIS DA EQUALIZAÇÃO DO HISTORIOGRAMA

cv.waitKey()
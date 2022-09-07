"""
@file sobel_demo.py
@brief Sample code using Sobel and/or Scharr OpenCV functions to make a simple Edge Detector
"""
import sys
import cv2 as cv
import numpy as np
import argparse

def main(argv):    
    window_name = ('Sobel Demo - Simple Edge Detector')
    scale = 1
    delta = 0
    ddepth = cv.CV_16S

    # Loads an image...
    parser = argparse.ArgumentParser(description='Code for filtro realce.')
    parser.add_argument('--input', help='Path to input image.', default='fruits.png')
    args = parser.parse_args()

    # ... Loads the image
    src = cv.imread(cv.samples.findFile(args.input))
    dst = cv.imread(cv.samples.findFile(args.input))
    # Check if image is loaded fine
    if src is None:
        print ('Error opening image: ' + argv[0])
        return -1
    
    kernelx = np.array([[1,1,1],[0,0,0], [-1,-1,-1]])
    kernely = np.array([[-1,0,1],[-1,0,1], [-1,0,1]])

    src = cv.GaussianBlur(src, (3, 3), 0)
    
    
    gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)
    
    
    grad_x = cv.filter2D(gray, ddepth, kernelx)

    # Gradient-Y
    # grad_y = cv.Scharr(gray,ddepth,0,1)
    grad_y = cv.filter2D(gray, ddepth, kernely)
    
    
    abs_grad_x = cv.convertScaleAbs(grad_x)
    abs_grad_y = cv.convertScaleAbs(grad_y)
    
    
    grad = cv.addWeighted(abs_grad_x, 0.5, abs_grad_y, 0.5, 0)
    
    # Display the source and after effects in a window = Exibe ambas as imagens (original e após efeito do Realce):
    cv.imshow('Source image', dst)
    cv.imshow(window_name, grad)
    cv.waitKey(0)
    
    return 0

if __name__ == "__main__":
    main(sys.argv[1:])
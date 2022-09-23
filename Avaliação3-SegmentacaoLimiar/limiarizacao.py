import sys
import cv2 as cv
import numpy as np
 
def main(argv):
    window_name = ('Treshold Binary Segmentation')
    window_original = ('Original Image')
 
    if len(argv) < 1:
        print('Not enough parameters')
        print('Usage:\nmorph_lines_detection.py < path_to_image >')
        return -1
 
    # load the original image
    original = cv.imread(argv[0])
    # load the image in grayscale
    src = cv.imread(argv[0], cv.IMREAD_GRAYSCALE)
   
 
    # Check if image is loaded fine
    if src is None:
        print('Error opening image: ' + argv[0])
        return -1
 
    width, height = np.shape(src)
 
    threshold = (src.max() + src.min()) / 2
    initialTreshold = threshold
   
    while abs(threshold - initialTreshold) != 0:
        R1 = np.array([])
        R2 = np.array([])
        for i in range(width):
            for y in range(height):
                if src[i, y] >= threshold:
                    R1 = np.append(R1, src[i, y])
                else:
                    R2 = np.append(R2, src[i, y])
       
        threshold = (np.mean(R1) + np.mean(R1)) / 2
 
    for i in range(width):
            for y in range(height):
                if src[i, y] >= threshold:
                    src[i, y] = 255
                else:
                    src[i, y] = 0

    # Display the source and Thresholding images in a window = Exibe ambas as imagens (original e limiarizada):
    cv.imshow(window_original, original) #ANTES DA LIMIARIZAÇÃO
    cv.imshow(window_name, src) #DEPOIS DA LIMIZARIZAÇÃO
    cv.waitKey(0)
    cv.destroyAllWindows()
    return 0
 
if __name__ == "__main__":
    main(sys.argv[1:])

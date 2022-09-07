import sys
import cv2 as cv
import numpy as np
#  Global Variables
DELAY_CAPTION = 1500
DELAY_BLUR = 100
MAX_KERNEL_LENGTH = 31
src = None
dst = None
dst1 = None
dst2 = None 
window_name = 'Smoothing Demo'
def main(argv):
    cv.namedWindow(window_name, cv.WINDOW_AUTOSIZE)
    # Load the source image
    imageName = argv[0] if len(argv) > 0 else 'C:\\Users\\Pichau\\Downloads\\board-saltpep-1.tif'
    global src
    src = cv.imread(cv.samples.findFile(imageName))
    if src is None:
        print ('Error opening image')
        print ('Usage: smoothing.py [image_name -- board-saltpep-1.tif] \n')
        return -1
 

    print("------- MENU -------")
    print("1 - Calcular Mediana")
    print("2 - Calcular Media")
    print("--------------------")
    opcao = int(input('Digite a opção desejada: '))
   
    # Original Image  --> Imprime a Imagem Original (independe da escolha do usuário)
    if display_caption('Original Image') != 0: ##Telinha da Imagem Original
        return 0
    global dst
    dst = np.copy(src)
    if display_dst(DELAY_CAPTION) != 0:
        return 0

    if (opcao == 1): ##Opção da Mediana       
        if display_caption('Median Blur - 3X') != 0: ##Telinha falando que tá calculando a Mediana 3 vezes
            return 0

        ##Código que faz o cálculo da Mediana 3 VEZES
        for i in range(1, MAX_KERNEL_LENGTH, 2):
            dst1 = cv.medianBlur(src, i)
            dst2 = cv.medianBlur(dst1, i)
            dst = cv.medianBlur(dst2, i)   
            if display_dst(DELAY_BLUR) != 0:
                 return 0 
        

    elif (opcao == 2): ##Opção da Média
        if display_caption('Blur - 3X') != 0: ##Telinha falando que tá calculando a Média 3 vezes
            return 0

        ##Código que faz o cálculo da Média 3 VEZES
        for i in range(1, MAX_KERNEL_LENGTH, 2):
            dst1 = cv.blur(src, (i, i))
            dst2 = cv.blur(dst1, (i, i))
            dst = cv.blur(dst2, (i, i))
            if display_dst(DELAY_BLUR) != 0:
                return 0
   
    else :
        print("## OPÇÃO INVÁLIDA!! ##")
         
       
    # Done
    display_caption('Done!') ##Telinha falando que foi concluído
    return 0 

def display_caption(caption):
    global dst
    dst = np.zeros(src.shape, src.dtype)
    rows, cols, _ch = src.shape
    cv.putText(dst, caption,
                (int(cols / 4), int(rows / 2)),
                cv.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255))
    return display_dst(DELAY_CAPTION)
 
def display_dst(delay):
    cv.imshow(window_name, dst)
    c = cv.waitKey(delay)
    if c >= 0 : return -1
    return 0
if __name__ == "__main__":
    main(sys.argv[1:])





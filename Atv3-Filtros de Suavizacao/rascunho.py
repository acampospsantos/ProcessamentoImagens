# Original Image
    if display_caption('Original Image') != 0:
        return 0
    global dst
    dst = np.copy(src)
    if display_dst(DELAY_CAPTION) != 0:
        return 0    

 
    # Applying Median blur (MEDIANA) - 1 VEZ
    if display_caption('Median Blur - 1 VEZ') != 0:
        return 0
   
    for i in range(1, MAX_KERNEL_LENGTH, 2):       
        dst = cv.medianBlur(src, i)             
        if display_dst(DELAY_BLUR) != 0:
            return 0      
   
 
    # Applying Median blur (MEDIANA) - 3 VEZES
    if display_caption('Median Blur - 3 VEZES') != 0:
        return 0
   
    for i in range(1, MAX_KERNEL_LENGTH, 2):       
        dst1 = cv.medianBlur(src, i)
        dst2 = cv.medianBlur(dst1, i)
        dst = cv.medianBlur(dst2, i)       
        if display_dst(DELAY_BLUR) != 0:
            return 0      

            

        # Applying blur (MEDIA) ---> RASCUNHO
            dst = cv.blur(src, (3, 3))
        if display_dst(DELAY_BLUR) != 0:
            return 0
   
    #  Done
    display_caption('Done!')
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

import cv2

def main():   
    windowName = 'Niblack Treshold Binarization'  
    cap = cv2.VideoCapture(0) 
    if cap.isOpened():
        ret, frame = cap.read()
    else:
        ret = False
    while ret:   
        ret, frame = cap.read()       
        th = 178
        max_val = 255
        _src = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	#_dst=cv.ximgproc.niBlackThreshold(_src, maxValue, type, blockSize, k[, _dst[, binarizationMethod]])
        _dst=cv2.ximgproc.niBlackThreshold(_src, max_val, cv2.THRESH_BINARY, 5, 0.1,
            cv2.THRESH_BINARY,
                cv2.ximgproc.BINARIZATION_NIBLACK)
        cv2.imshow(windowName, _dst)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cv2.destroyAllWindows()
    cap.release()

if __name__ == "__main__":
    main()

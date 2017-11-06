import cv2
import numpy as np
def main(argv ):
    src = cv2.imread(argv)
    print(src)
    cv2.namedWindow("Original image", cv2.WINDOW_AUTOSIZE)
    cv2.imshow("Original image", src)
    (B,G,R) = cv2.split(src)
    cv2.imshow("Red", R)
    cv2.imshow("Green", G)
    cv2.imshow("Blue", B)
    print("value in RGB is " + str((R[19][25], G[19][25], B[19][25])))

    ycrcb_image = cv2.cvtColor(src, cv2.COLOR_BGR2YCR_CB)
    (Y, CB, CR) = cv2.split(ycrcb_image)
    cv2.imshow("Y", Y)
    cv2.imshow("Cb", CB)
    cv2.imshow("Cr", CR)
    print("value in YCBCR is " + str((Y[19][25], CB[19][25], CR[19][25])))

    hsv_image = cv2.cvtColor(src, cv2.COLOR_BGR2HSV)
    (Hue, Saturation, Value) = cv2.split(hsv_image)
    cv2.imshow("Hue", Hue)
    cv2.imshow("Saturation", Saturation)
    cv2.imshow("Value", Value)
    print("value in HSV is " + str((Hue[19][25], Saturation[19][25], Value[19][25])))

    cv2.waitKey(0)
    return 0
if __name__ == '__main__':
    main('Test_images/Lenna.png')
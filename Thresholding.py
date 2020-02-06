import cv2

img = cv2.imread('b.jpeg')
# in threshold these argument are use image name, lower bound, higest value of color,keyword(cv2.THRES_Binary,)
# flag, fream = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
# flag, fream = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY_INV)

img2 = cv2.imread('b.jpeg', 0)
flag, frame = cv2.threshold(img2, 10, 255, cv2.THRESH_BINARY)
result = cv2.adaptiveThreshold(img2, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 111, 3)

cv2.imshow("IMAGE", img)
# cv2.imshow("Thresh", img2)
# cv2.imshow("Final", frame)
cv2.imshow("RESULT", result)
cv2.waitKey(0)
cv2.destroyAllWindows()

import cv2


img = cv2.imread('abc.jpg', 1)

box = img[37:111, 108:195]

img[0:74, 0:87] = box # same diffrance hovo joye 111-37, 195-108

cv2.imshow('This is', img)

cv2.waitKey(0)
cv2.destroyAllWindows()



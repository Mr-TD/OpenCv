import cv2
import time
vid = cv2.VideoCapture(0)
while True:
    flag, fream = vid.read()
    cv2.imshow('a', fream)
    i = 3
    while i >= 1:
        flag, fream = vid.read()
        if i != 0:
            cv2.putText(fream, str(i), (250, 250), cv2.FONT_HERSHEY_SIMPLEX, 7, (255, 255, 255), 10, cv2.LINE_AA)
        cv2.imshow('a', fream)
        cv2.waitKey(1)
        time.sleep(0.5)
        i = i - 1
    else:
        flag, fream = vid.read()
        cv2.imshow('a', fream)
        cv2.waitKey(1)
        cv2.imwrite('camera13.jpg',fream)
        break
vid.release()
cv2.destroyAllWindows()

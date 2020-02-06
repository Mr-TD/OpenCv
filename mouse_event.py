import cv2

# print(cv2.EVENT_LBUTTONDOWN)
# print(cv2.EVENT_LBUTTONUP)
#
# print(cv2.EVENT_RBUTTONDOWN)
# print(cv2.EVENT_RBUTTONUP)

def mouse_event(event, x, y, flag, parameter):
    if event == cv2.EVENT_LBUTTONDOWN:
        print("you")
        print(x)
        cv2.putText(img, str(x)+str(" ")+str(y), (x, y), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 255, 0), 2)
       # cv2.putText(img, 'Clicked', (x, y), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 255, 0), 2)
        # image name, event name, position, font tyle, size of font, color of font but bgr format, thickness
        cv2.imshow('Image', img)


img = cv2.imread('abc.jpg', 1)
cv2.imshow('Image', img)
cv2.setMouseCallback('Image',mouse_event)



cv2.waitKey(0)
cv2.destroyAllWindows()


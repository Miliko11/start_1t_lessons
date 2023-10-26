import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    res, img = cap.read()
    cv2.imshow('image', img)

    img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    hue = img_hsv[:, :, 0]
    saturation = img_hsv[:, :, 1]
    value = img_hsv[:, :, 2]
    cv2.imshow('hue', hue)
    cv2.imshow('saturation', saturation)
    cv2.imshow('value', value)


    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

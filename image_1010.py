import cv2

img = cv2.imread("py.png")
grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

face_cascade = cv2.CascadeClassifier(cv2.haarcascades +'haarcascade_frontalfase_default.xml')
faces = face_cascade.detectMultiScale(grey, 1.2, 5)

print("Количество лиц=", len(faces))
for(x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (255,0,0), 2)

cv2.imshow("faces", img)

cv2.waitKey(0)
cv2.destroyAllWindows()
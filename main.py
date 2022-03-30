from HandTracingModule import HandDetector
import cv2


cap = cv2.VideoCapture(0)
detector = HandDetector()
while True:
    succes, img = cap.read()
    img = detector.findHands(img)
    lst = detector.findPosition(img)

    cv2.imshow("Image", img)
    cv2.waitKey(1)
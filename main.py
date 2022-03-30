from HandTracingModule import HandDetector
import cv2
import numpy as np
from sound import Sound


cap = cv2.VideoCapture(0)
detector = HandDetector()

while True:
    succes, img = cap.read()
    img = detector.findHands(img, draw=False)
    lst = detector.findPosition(img, draw=False)
    if len(lst)!=0:
        # Getting the coordinates of the fingers
        id, x1, y1 = lst[4]
        id, x2, y2 = lst[8]
        # Draw pointers
        cv2.line(img, (x1, y1), (x2, y2), (0, 255, 0))
        cv2.circle(img, (x1, y1), 5, (255,0,255), cv2.FILLED)
        cv2.circle(img, (x2, y2), 5, (255, 0, 255), cv2.FILLED)
        # Set the volume depending on the distance between the fingers
        vector = (x2-x1, y2-y1)
        lenghtVector = int((vector[0]**2+vector[1]**2)**0.5)
        vol = int(np.interp(lenghtVector, [20, 140], [0, 100]))
        Sound.volume_set(vol)

    cv2.imshow("Image", img)
    cv2.waitKey(1)

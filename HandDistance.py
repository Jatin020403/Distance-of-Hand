
import cv2 as cv
import numpy as np
import mediapipe as mp
import time
import HandTrackingModule as htm
import math


def dist(l1, l2):
    pt1 = [l1[1], l1[2]]
    pt2 = [l2[1], l2[2]]
    return math.dist(pt1, pt2)


pTime = 0
cap = cv.VideoCapture(0)
detector = htm.handDetector()


dist_list = []                         
Config = True

DISTANCE = 30

while cap.isOpened():
    
    while Config:
        
        print('''Place your hand at a distance of 30 cm
The palm must be parallel to the screen and and right in front of the camera''')
        
        ask = (input("Ready for Config :       [Expecting Yes]\n")).upper()
        
        if ask == 'YES':
            for i in range(5):
                success, img = cap.read()
                img = cv.flip(img, 1)
                img = detector.findHands(img)
                lmList = detector.findPosition(img, draw = False)
                if len(lmList) !=0:
                    d = dist(lmList[0], lmList[9])      # For Wrist to Middle_F_MCP -- [0] to [9]
                    dist_list.append(d)                     # Refer Reference Image for more information
            D_initial = np.mean(dist_list)
            print('D_initial value for you is ', D_initial)
            Config = False
            
        elif ask == 'MINE':
            D_initial = 256             # Hardcoded my D_initial value
            Config = False
            
        else:
            print('...')

    success, img = cap.read()
    img = cv.flip(img, 1)
    img = detector.findHands(img)
    lmList = detector.findPosition(img, draw = False)
    if len(lmList) !=0:

        D_final = dist(lmList[0], lmList[9])
        Expected_Distance = round(D_initial/D_final * DISTANCE, 2)

        print(Expected_Distance, 'cm')
        


    cTime = time.time()
    fps = 1/(cTime - pTime)
    pTime = cTime

    cv.putText(img, 'Fps:'+str(int(fps)), (10, 70),
                cv.FONT_HERSHEY_PLAIN, 3,
               (255, 0, 255), 3)

    cv.imshow('Screen', img)
    cv.waitKey(1)

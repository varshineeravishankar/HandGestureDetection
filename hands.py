import cv2
import mediapipe as mp
from math import hypot
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
import numpy as np
from cvzone.HandTrackingModule import HandDetector
from cvzone.ClassificationModule import Classifier
import numpy as np
import math
import pyaudio
import wave
import volume_control
import test


cap = cv2.VideoCapture(0)
detector = HandDetector(detectionCon=0.8, maxHands=2)
while True:
    succes, img = cap.read()
    hands, img = detector.findHands(img)
    if hands:
        hand1 = hands[0]
        lmList1 = hand1["lmList"]
        bbox1 = hand1["bbox"]
        centerPoint1 = hand1["center"]
        handType1 = hand1["type"]
        #test.fcall()
        volume_control.funcc()

        # print(len(lmList1), lmList1)
        # print(bbox1 )
        # print(centerPoint1)
        fingers1 = detector.fingersUp(hand1)

        if len(hands) == 2:
            hand2 = hands[1]
            lmList2 = hand2["lmList"]
            bbox2 = hand2["bbox"]
            centerPoint2 = hand2["center"]
            handType2 = hand2["type"]
            #volume_control.funcc()
            test.fcall()





            fingers2 = detector.fingersUp(hand2)

            # if hand2["type"] == "left"
            # print(fingers1, fingers2)
            # lenght, info, img = detector.findDistance(centerPoint1, centerPoint2, img)

    cv2.imshow("Image", img)
    cv2.waitKey(1)

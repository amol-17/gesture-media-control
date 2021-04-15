import cv2
import mediapipe as mp

class handDetector():
    def __init__(self, mode=False, maxHands=2, detectionConfi=0.5, trackConfi=0.5):
        self.mode = mode
        self.maxHands = maxHands
        self.detectionConfi = detectionConfi
        self.trackConfi = trackConfi

        self.hand_sol = mp.solutions.hands
        self.hands = self.hand_sol.Hands(self.mode, self.maxHands,
                                        self.detectionConfi, self.trackConfi)
        self.Draw = mp.solutions.drawing_utils

    def findHands(self, img, draw=True):
        img_to_RGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.hands.process(img_to_RGB)

        if self.results.multi_hand_landmarks:
            for handLandmarks in self.results.multi_hand_landmarks:
                if draw:
                    self.Draw.draw_landmarks(img, handLandmarks,
                                               self.hand_sol.HAND_CONNECTIONS)
        return img

    def findHandPosition(self, img, handNumber=0, draw=True):

        LandmarkList = []
        if self.results.multi_hand_landmarks:
            myHand = self.results.multi_hand_landmarks[handNumber]
            for id, Landmark in enumerate(myHand.landmark):
                # print(id, Landmark)
                hei, wei, c = img.shape
                cx, cy = int(Landmark.x * wei), int(Landmark.y * hei)
                LandmarkList.append([id, cx, cy])
                if draw:
                    cv2.circle(img, (cx, cy), 12, (255, 0, 0), cv2.FILLED)

        return LandmarkList

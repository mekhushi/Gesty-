import mediapipe as mp
import cv2

class HandTracker:
    def __init__(self):
        self.hands = mp.solutions.hands.Hands(
            static_image_mode=False,
            max_num_hands=1,
            min_detection_confidence=0.7,
            min_tracking_confidence=0.7
        )
        self.drawer = mp.solutions.drawing_utils

    def get_hand_landmarks(self, frame):
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        result = self.hands.process(rgb)
        if result.multi_hand_landmarks:
            return result.multi_hand_landmarks[0]
        return None

    def draw_hand(self, frame):
        landmarks = self.get_hand_landmarks(frame)
        if landmarks:
            self.drawer.draw_landmarks(frame, landmarks, mp.solutions.hands.HAND_CONNECTIONS)
        return frame

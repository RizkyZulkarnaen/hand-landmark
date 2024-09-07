import mediapipe as mp
import cv2
import numpy as np

hands = hand_landmark.Hands(static_image_mode=False, max_num_hands=1,
                            min_detection_confidence=0.5, min_tracking_confidence=0.5)

hand_draw = mp.solutions.drawing_utils


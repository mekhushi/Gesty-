import cv2
import time
from collections import deque
from hand_tracker import HandTracker
from gesture_detector import detect_gesture
from window_control import perform_action

cap = cv2.VideoCapture(0)
tracker = HandTracker()

gesture_history = deque(maxlen=6)
last_performed = None
last_time = 0
cooldown = 2  # seconds

try:
    while True:
        ret, frame = cap.read()
        if not ret:
            print("⚠️ Camera error")
            break

        landmarks = tracker.get_hand_landmarks(frame)
        gesture = detect_gesture(landmarks)

        # Store gesture history for consistency
        gesture_history.append(gesture)
        most_common = max(set(gesture_history), key=gesture_history.count)

        # Confirm gesture only if stable for 5+ frames
        if gesture_history.count(most_common) >= 5 and most_common:
            now = time.time()
            if most_common != last_performed or (now - last_time > cooldown):
                print(f"✅ Confirmed: {most_common}")
                perform_action(most_common)
                last_performed = most_common
                last_time = now

        # Visual
        frame = tracker.draw_hand(frame)
        if most_common:
            cv2.putText(frame, f"Gesture: {most_common}", (10, 40),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2)

        cv2.imshow("Gesture Controller", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

except Exception as e:
    import traceback
    traceback.print_exc()

cap.release()
cv2.destroyAllWindows()

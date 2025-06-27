from gesture_utils import is_thumb_up

def detect_gesture(landmarks):
    if not landmarks:
        return None

    finger_states = []

    # Thumb detection using angle + height
    if is_thumb_up(landmarks):
        finger_states.append(1)
    else:
        finger_states.append(0)

    # Index, middle, ring, pinky with relaxed margin
    for tip_id in [8, 12, 16, 20]:
        tip = landmarks.landmark[tip_id]
        pip = landmarks.landmark[tip_id - 2]
        finger_states.append(1 if tip.y < pip.y - 0.01 else 0)

    print("🧠 Finger States:", finger_states)

    # Gesture classification
    if finger_states == [1, 0, 0, 0, 0]:
        return "thumbs_up"
    elif finger_states == [0, 0, 0, 0, 0]:
        return "fist"
    elif finger_states == [0, 1, 1, 1, 1]:
        return "open_palm"
    elif finger_states == [0, 1, 0, 0, 0]:
        return "one_finger"
    elif finger_states == [0, 1, 1, 0, 0]:
        return "two_fingers"
    elif finger_states == [1, 1, 1, 1, 1]:
        return "screenshot"

    return None

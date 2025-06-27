import math

def is_thumb_up(landmarks):
    """
    Returns True if thumb is pointing upward based on angle and height.
    """
    wrist = landmarks.landmark[0]
    thumb_tip = landmarks.landmark[4]
    thumb_mcp = landmarks.landmark[2]

    dx = thumb_tip.x - thumb_mcp.x
    dy = thumb_tip.y - thumb_mcp.y
    angle = math.degrees(math.atan2(dy, dx))

    return -100 < angle < -40 and thumb_tip.y < wrist.y - 0.1

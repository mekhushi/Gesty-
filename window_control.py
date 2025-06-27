import pyautogui
import datetime

def perform_action(gesture):
    if gesture == "thumbs_up":
        pyautogui.hotkey('win', 'up')       # ✅ Thumbs Up → Maximize
    elif gesture == "fist":
        pyautogui.hotkey('win', 'down')     # ✅ Fist → Minimize
    elif gesture == "open_palm":
        pyautogui.hotkey('win', 'tab')      # Task View
    elif gesture == "one_finger":
        pyautogui.hotkey('alt', 'f4')       # Close Window
    elif gesture == "two_fingers":
        pyautogui.hotkey('win', 'e')        # Open File Explorer
    elif gesture == "screenshot":
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"screenshot_{timestamp}.png"
        pyautogui.screenshot(filename)
        print(f"📸 Screenshot saved: {filename}")

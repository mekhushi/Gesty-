import pyautogui
import datetime

def perform_action(gesture):
    if gesture == "thumbs_up":
        pyautogui.hotkey('win', 'up')      
    elif gesture == "fist":
        pyautogui.hotkey('win', 'down')    
    elif gesture == "open_palm":
        pyautogui.hotkey('win', 'tab')      
    elif gesture == "one_finger":
        pyautogui.hotkey('alt', 'f4')       
    elif gesture == "two_fingers":
        pyautogui.hotkey('win', 'e')       
    elif gesture == "screenshot":
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"screenshot_{timestamp}.png"
        pyautogui.screenshot(filename)
        print(f"📸 Screenshot saved: {filename}")

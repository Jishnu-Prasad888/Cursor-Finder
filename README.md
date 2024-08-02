# Cursor-Finder



## Circle Drawer with Hotkeys

This project is a Python application that displays a translucent circle at the current mouse position when a specific hotkey is pressed. The circle is drawn using PyQt5 and the display of the circle is controlled using a timer. The application also allows you to exit by pressing another hotkey.

## Features

- Draws a translucent circle at the current mouse position.
- The circle automatically disappears after a specified duration.
- Supports hotkeys to trigger the circle display and to exit the application.

## Requirements

- Python 3.x
- PyQt5
- pyautogui
- keyboard

## Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/yourusername/circle-drawer.git
   ```

2. Navigate to the project directory:

   ```bash
   cd circle-drawer
   ```

3. Install the required Python packages:

   ```bash
   pip install pyqt5 pyautogui keyboard
   ```

## Usage

1. Run the script:

   ```bash
   python main.py
   ```

2. Use the following hotkeys:
   - **Show Circle**: `Ctrl + Shift + Alt + A`
   - **Exit Application**: `Ctrl + Alt + X`

When you press the "Show Circle" hotkey, a translucent circle will be drawn at the current mouse position. The circle will remain visible for 1 second before disappearing. You can adjust the display duration by modifying the `time` parameter in the `Circle` class.

To exit the application, press the "Exit Application" hotkey.

## Code Overview

- **Circle Class**: Inherits from `QWidget` and handles the drawing of the circle with specified transparency and radius. Uses a `QTimer` to close the window after a specified time.
- **run_on_hotkey Function**: Retrieves the current mouse position and creates an instance of the `Circle` class at that position.
- **exit_func Function**: Exits the application.
- **main Function**: Sets up hotkeys and starts listening for them using the `keyboard` library.


## Common Colors and Their RGB Values

#### Red: QColor(255, 0, 0)
#### Green: QColor(0, 255, 0)
#### Blue: QColor(0, 0, 255)
#### Yellow: QColor(255, 255, 0)
#### Cyan: QColor(0, 255, 255)
#### Magenta: QColor(255, 0, 255)
#### White: QColor(255, 255, 255)
#### Black: QColor(0, 0, 0)
#### Gray: QColor(128, 128, 128)
#### Light Gray: QColor(192, 192, 192)
#### Dark Gray: QColor(64, 64, 64)
#### Orange: QColor(255, 165, 0)
#### Pink: QColor(255, 192, 203)
#### Brown: QColor(165, 42, 42)
#### Purple: QColor(128, 0, 128)
#### Lime: QColor(50, 205, 50)
#### Teal: QColor(0, 128, 128)
#### Indigo: QColor(75, 0, 130)
#### Gold: QColor(255, 215, 0)

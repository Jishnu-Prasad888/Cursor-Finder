import sys
import pyautogui
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QPainter, QPen, QColor, QBrush
from PyQt5.QtCore import Qt, QRect, QTimer
import keyboard

class Circle(QWidget):
    def __init__(self, x, y, radius, time=1, transparency_circle=0, transparency_border=255):
        super().__init__()
        self.time = time
        self.transparency_circle = transparency_circle
        self.transparency_border = transparency_border
        self.x = x
        self.y = y
        self.radius = radius
        screen = QApplication.primaryScreen()
        screen_size = screen.size()
        self.setWindowTitle("")
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setGeometry(QRect(0, 0, screen_size.width(), screen_size.height()))
        self.showFullScreen()
        self.timer = QTimer()
        self.timer.timeout.connect(self.closeWindow)
        self.timer.start(time * 1000)
    
    def closeWindow(self):
        self.close()
        
    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        pen = QPen(QColor(255, 0, 0, self.transparency_border), 3)
        painter.setBrush(QBrush(QColor(255, 0, 0, self.transparency_circle)))
        painter.setPen(pen)
        painter.drawEllipse(self.x - self.radius, self.y - self.radius, 2 * self.radius, 2 * self.radius)

def run_on_hotkey():
    app = QApplication([])
    xpos, ypos = pyautogui.position()
    circle_widget = Circle(xpos, ypos, 50)
    circle_widget.show()
    app.exec_()

def exit_func():
    exit()
    # sys.exit

def main():
    # Setup the hotkeys
    stopkey = "ctrl+alt+x"
    hotkey = "ctrl+shift+alt+a"

    keyboard.add_hotkey(hotkey, run_on_hotkey)
    keyboard.add_hotkey(stopkey, exit_func)

    print(f"Hotkeys set: {hotkey} to show circle, {stopkey} to exit.")
    keyboard.wait()  # Wait indefinitely for hotkeys

if __name__ == "__main__":
    main()

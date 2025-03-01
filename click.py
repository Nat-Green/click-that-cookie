import time
import threading
from pynput.mouse import Controller, Button
from pynput.keyboard import Listener, KeyCode

TOGGLE_KEY = KeyCode(char='t')  # Set this to whatever key you want to use as your clicker toggle

clicking = False
mouse = Controller()

def clicker():
    while True:
        if clicking:
            mouse.click(Button.left, 1)
        time.sleep(0.0001)  # Set the wait time between each click (smaller number = faster clicks, but there's a limit to how much the game will actually register)

def toggle_event(key):
    if key == TOGGLE_KEY:
        global clicking
        clicking = not clicking

click_thread = threading.Thread(target=clicker)
click_thread.start()

with Listener(on_press=toggle_event) as listener:
    listener.join()
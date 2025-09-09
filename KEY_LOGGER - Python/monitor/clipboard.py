import time
import logging
import pyperclip

def log_clipboard(running):
    prev_content = ""
    while running.is_set():
        try:
            content = pyperclip.paste()
            if content != prev_content:
                logging.info(f"Clipboard: {content}")
                prev_content = content
        except Exception as e:
            logging.error(f"Clipboard error: {e}")
        time.sleep(1)

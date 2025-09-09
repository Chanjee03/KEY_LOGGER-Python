import time
import logging
import mss

def capture_screenshot(running):
    with mss.mss() as sct:
        while running.is_set():
            try:
                filename = f"screenshot_{int(time.time())}.png"
                sct.shot(output=filename)
                logging.info(f"Screenshot saved: {filename}")
            except Exception as e:
                logging.error(f"Screenshot error: {e}")
            time.sleep(10)

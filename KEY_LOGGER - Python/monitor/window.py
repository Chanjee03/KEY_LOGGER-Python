import sys
import time
import logging

def log_window_title(running):
    if sys.platform.startswith('linux'):
        # Periodically log that this feature is intentionally skipped
        while running.is_set():
            logging.info("Active window logging is skipped on Linux.")
            time.sleep(60)  # Log once every minute
        return

    prev_title = ""
    while running.is_set():
        try:
            import pygetwindow as gw
            active_window = gw.getActiveWindow()
            if active_window:
                title = active_window.title
                if title != prev_title:
                    logging.info(f"Active Window: {title}")
                    prev_title = title
        except Exception as e:
            logging.error(f"Window logging error: {e}")
        time.sleep(1)

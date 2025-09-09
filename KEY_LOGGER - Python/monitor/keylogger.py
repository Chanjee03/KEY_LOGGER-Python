import logging

def log_keystrokes(key):
    try:
        logging.info(f"Key {getattr(key, 'char', key)} pressed")
    except Exception as e:
        logging.error(f"Keystroke logging error: {e}")

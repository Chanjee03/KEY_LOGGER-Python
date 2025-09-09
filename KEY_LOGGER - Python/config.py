import os
from dotenv import load_dotenv

load_dotenv()

DROPBOX_ACCESS_TOKEN = os.getenv("DROPBOX_ACCESS_TOKEN")
EMAIL_USER = os.getenv("EMAIL_USER")
EMAIL_PASS = os.getenv("EMAIL_PASS")
EMAIL_RECEIVER = os.getenv("EMAIL_RECEIVER", "your_destination@example.com")
EMAIL_CHECK_INTERVAL = 60
SELF_DESTRUCT_COMMANDS = {"DEACTIVATE", "SELF_DESTRUCT"}

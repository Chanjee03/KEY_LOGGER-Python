import time
import logging
import imaplib
import email
from email.header import decode_header

def check_emails(running, email_user, email_pass, self_destruct_commands, initiate_self_destruct, interval):
    while running.is_set():
        try:
            mail = imaplib.IMAP4_SSL("imap.gmail.com")
            mail.login(email_user, email_pass)
            mail.select("inbox")
            _, data = mail.search(None, '(UNSEEN)')
            for num in data[0].split():
                _, msg_data = mail.fetch(num, '(RFC822)')
                msg = email.message_from_bytes(msg_data[0][1])
                subject = decode_header(msg["Subject"])[0][0]
                if isinstance(subject, bytes):
                    subject = subject.decode()
                if subject.strip().upper() in self_destruct_commands:
                    mail.store(num, '+FLAGS', '\\Seen')
                    initiate_self_destruct()
                    return
        except Exception as e:
            logging.error(f"Email check failed: {e}")
        finally:
            try: mail.close()
            except: pass
            try: mail.logout()
            except: pass
        time.sleep(interval)

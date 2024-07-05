import os
import platform
import subprocess


def get_desktop_environment():
    return os.environ.get('XDG_CURRENT_DESKTOP')


def is_screen_locked():
    os_name = platform.system()

    if os_name == 'Linux':
        desktop_env = get_desktop_environment()
        if desktop_env == 'KDE':
            # KDE specific command
            output = subprocess.check_output("qdbus org.kde.screensaver /ScreenSaver org.freedesktop.ScreenSaver.GetActive", shell=True)
            return "true" in output.decode('utf-8').lower()

        elif desktop_env in ['GNOME', 'MATE', 'Cinnamon', 'X-Cinnamon']:
            # GNOME, MATE, Cinnamon specific command
            output = subprocess.check_output("gnome-screensaver-command -q", shell=True)
            return "is active" in output.decode('utf-8').lower()

        elif desktop_env == 'XFCE':
            # XFCE specific command
            output = subprocess.check_output("xfce4-screensaver-command -q", shell=True)
            return "is active" in output.decode('utf-8').lower()

        else:
            raise NotImplementedError(f"Unsupported desktop environment: {desktop_env}")

    elif os_name == 'Darwin':
        # For MacOS
        output = subprocess.check_output("/usr/bin/python -c 'import Quartz; print Quartz.CGSessionCopyCurrentDictionary()'", shell=True)
        return "CGSSessionScreenIsLocked = 1" in output.decode('utf-8').lower()

    elif os_name == 'Windows':
        # For Windows
        import ctypes
        user32 = ctypes.windll.User32
        return user32.GetForegroundWindow() == 0

    else:
        raise NotImplementedError(f"Unsupported platform: {os_name}")

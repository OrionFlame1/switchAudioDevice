import os
import sys
import pystray
from datetime import datetime
from PIL import Image
from pystray import MenuItem as item
from audioUtil import audioSwitch

global devices

def debug():
    if __name__ == "__main__" or getattr(sys, 'frozen', False):
        return True
    return False

def now():
    return "[" + datetime.now().strftime("%H:%M:%S") + "]"

def set_device(device_name):
    global devices
    device_name = str(device_name)
    id = str(devices[device_name])
    print(f"{now()} SETTING DEVICE TO {device_name} - {id}")
    audioSwitch.switchOutput(id, 1) # 1 = eMultimedia
    audioSwitch.switchOutput(id, 2) # 2 = eCommunications

def on_exit(icon):
    icon.stop()
    print(f"{now()} EXITING")

def load_icon():
    if debug():
        icon_folder = os.path.join(os.path.dirname(__file__), 'static')
    else:
        icon_folder = os.path.join(sys._MEIPASS, 'static')
    return Image.open(icon_folder + "\icon.ico")

def setup_tray():
    global devices
    devices = audioSwitch.MyAudioUtilities.getAllDevices("Output")
    
    menu = []

    for device in devices:
        print(f"{now()} DEVICE: {device} ID: {devices[device]}")
        menu.append(item(str(device), lambda _, id=str(device): set_device(id)))

    menu.append(item('Exit', on_exit))

    icon = pystray.Icon("test_icon", load_icon(), "switchAudioDevice", menu)
    icon.run()

setup_tray()
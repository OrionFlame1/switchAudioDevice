import os
import sys
from comtypes import CLSCTX_ALL
import pystray
from pystray import MenuItem
from PIL import Image, ImageDraw
from pystray import MenuItem as item
from pycaw.pycaw import AudioUtilities
from audioUtil import audioSwitch
from pycaw.constants import ERole

global devices

def set_device(device_name):
    global devices
    device_name = str(device_name)
    print(f"SETTING DEVICE TO {device_name} - {str(devices[device_name])}")
    audioSwitch.switchOutput(str(devices[device_name]), 2)

def on_exit(icon):
    icon.stop() 

def load_icon():
    icon_folder = os.path.join(sys._MEIPASS, 'static')
    return Image.open(icon_folder + "\icon.ico")

def setup_tray():
    global devices
    devices = audioSwitch.MyAudioUtilities.getAllDevices("Output")
    
    menu = []

    for device in devices:
        print("DEVICE: " + device + " ID: " + devices[device])
        menu.append(item(str(device), lambda _, id=str(device): set_device(id)))

    menu.append(item('Exit', on_exit))

    icon = pystray.Icon("test_icon", load_icon(), "switchAudioDevice", menu)
    icon.run()

setup_tray()
import sys
import ctypes
from comtypes import CLSCTX_ALL
import pystray
from PIL import Image, ImageDraw
from pystray import MenuItem as item
from pycaw.pycaw import IAudioEndpointVolume, AudioUtilities, IMMDeviceEnumerator
import sounddevice as sd


def get_devices():
    # Get all audio devices
    devices = AudioUtilities.GetAllDevices()

    output_devices = {}
    device_count = 0

    # Print the list of output devices
    for idx, device in enumerate(devices):
        if str(getattr(device, "state")) == "AudioDeviceState.Active" and "0.0.0" in str(getattr(device, "id")):
            # for attr in device.__dict__:
            #     print(attr + "->" + str(getattr(device, attr)))

            output_devices[device_count] = {"index": device_count, "id" : device.id, "name" : device.properties["{A45C254E-DF1C-4EFD-8020-67D146A850E0} 14"]}
            device_count += 1

    return output_devices

    # {A45C254E-DF1C-4EFD-8020-67D146A850E0} 2
    # simple name

    # {B3F8FA53-0004-438E-9003-51A46E139BFC} 6
    # more detailed name

    # {A45C254E-DF1C-4EFD-8020-67D146A850E0} 14
    # complete name

def set_device(device_id):
    print("Setting device to: " + str(device_id))
    pass

def on_exit(icon, item):
    icon.stop()  # Stop the tray icon, effectively exiting the app

# Function to generate an icon
def create_image(width, height, color1, color2):
    image = Image.new('RGB', (width, height), color1)
    dc = ImageDraw.Draw(image)
    dc.rectangle(
        (width // 2, 0, width, height // 2),
        fill=color2)
    dc.rectangle(
        (0, height // 2, width // 2, height),
        fill=color2)
    return image

# Define the system tray icon
def setup_tray():
    # Create an image for the icon
    icon_image = create_image(64, 64, 'blue', 'white')

    items = get_devices()

    menu = []

    # menu = (item(name, lambda item, id=index: set_device(id)) for index, name in enumerate(items))
    for index, name in items.items():
        menu.append(item(name["name"], lambda item, id=name["index"]: set_device(id)))
    # Create the icon object
    icon = pystray.Icon("test_icon", icon_image, "System Tray Icon", menu)

    # Run the icon loop in the background
    icon.run()

# Start the tray icon
if __name__ == "__main__":
    setup_tray()

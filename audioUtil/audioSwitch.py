from __future__ import print_function
import os
import ctypes
import comtypes
from pycaw.constants import CLSID_MMDeviceEnumerator
from pycaw.pycaw import (DEVICE_STATE, AudioUtilities, EDataFlow,
                         IMMDeviceEnumerator)

from . import policyconfig as pc

cwd = os.getcwd()
audioDll = ctypes.CDLL(cwd + "/AudioDLL.dll")

class MyAudioUtilities(AudioUtilities):
    @staticmethod
    def getAllDevices(direction, State = DEVICE_STATE.ACTIVE.value):
        devices = {}
        if direction.lower() == "input":
            Flow = EDataFlow.eCapture.value     # 1
        else:
            # Output
            Flow = EDataFlow.eRender.value      # 0
        comtypes.CoInitialize()
        deviceEnumerator = comtypes.CoCreateInstance(
            CLSID_MMDeviceEnumerator,
            IMMDeviceEnumerator,
            comtypes.CLSCTX_INPROC_SERVER)
        if deviceEnumerator is None:
            return devices
        

        collection = deviceEnumerator.EnumAudioEndpoints(Flow, State)
        if collection is None:
            return devices

        count = collection.GetCount()
        for i in range(count):
            dev = collection.Item(i)
            if dev is not None:
                createDev = AudioUtilities.CreateDevice(dev)
                if not ": None" in str(createDev):
                    # devices.append({
                    #                 "name" : createDev.FriendlyName,
                    #                 "id" : createDev.id
                    #               })
                    devices[createDev.FriendlyName] = createDev.id
                createDev._dev.Release()
                
        comtypes.CoUninitialize()
        return devices

def switchOutput(deviceId, role):
    try:
        policy_config = comtypes.CoCreateInstance(
            pc.CLSID_PolicyConfigClient,
            pc.IPolicyConfig,
            comtypes.CLSCTX_ALL
        )
        policy_config.SetDefaultEndpoint(deviceId, role)
        policy_config.Release()
    except Exception as e:
        print(e)

SetApplicationEndpoint = audioDll.SetApplicationEndpoint




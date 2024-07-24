# SteelSeries Sonar Device Switcher
A way to switch sound devices on SteelSeries Sonar

## How do I set it up?
You'll need to acquire the device ID for the devices you want - these change if you update their drivers so you may need to re-do this step once a month or how frequently you update drivers. 

Simply go to Sonar and set the device you want to be known as speaker then run DeviceID/deviceIdUpdateSpeaker.py, and then set the device to headset and run DeviceID/deviceIdUpdateHeadset.py

![UpdateDeviceFlow](https://github.com/user-attachments/assets/717fae45-f29f-4518-9f43-6a380501ff39)

This will update the text files within DeviceID which can be used by the python files to change devices.

Run each python file and you should be able to see that the devices are switching between each other.

I've had to make it so that the python files run without popping a cmd window up, and to also use the icons that I have provided which I have pinned to my taskbar as seen below.

![WindowsTaskbar](https://github.com/zencane/SteelSeries-Sonar-Device-Switcher/assets/141449041/b3ef520d-0631-477b-9186-2806ab05ef9e)

To do this you can right click on the python file and add it as a shortcut to the taskbar. Then right click on the shortcut you have created and edit the properties - change the icon from there and you can also tinker with other settings.

## Why did I make this?
I've had this sound switch solution for a while but when I switched to SteelSeries Sonar for my sound management, I needed to revamp it and make it compatible with the SteelSeries Sonar API.

## How does it work?
The script makes use of the local Sonar API and curl commands!

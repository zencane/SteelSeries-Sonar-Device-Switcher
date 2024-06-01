# SteelSeries Sonar Device Switcher
A way to switch sound devices on SteelSeries Sonar

## How do I set it up?
You'll need to acquire the device ID for the devices you want - these change if you update their drivers so you may need to re-do this step once a month or how frequently you update drivers. 
You can do this by using the Wireshark - Choose the "Adapter for loopback traffic capture" and start monitoring. Open the Mixer tab in Sonar (streamer mode enabled) and toggle between the two devices a couple times.
![image](https://github.com/zencane/SteelSeries-Sonar-Device-Switcher/assets/141449041/d52839d1-3e6f-49bc-a0ec-7123faf3473a)

Stop the wireshark capture and scroll until you find a line that resembles this ![image](https://github.com/zencane/SteelSeries-Sonar-Device-Switcher/assets/141449041/c0f4b54f-25d8-4bbb-8a69-fe07d3154d4e)
The text after "deviceID/" until " HTTP/1.1" is what you're looking for. Type this into codeHeadset.txt. Find another similar line and type the deviceID you find into codeSpeaker.txt.

Run each python file and you should be able to see that the devices are switching between each other.

I've had to make it so that the python files run without popping a cmd window up, and to also use the icons that I have provided which I have pinned to my taskbar as seen below.

![image](https://github.com/zencane/SteelSeries-Sonar-Device-Switcher/assets/141449041/b3ef520d-0631-477b-9186-2806ab05ef9e)

To do this you can right click on the python file and add it as a shortcut to the taskbar. Then right click on the shortcut you have created and edit the properties - change the icon from there and you can also tinker with other settings.

## Why did I make this?
I've had this sound switch solution for a while but when I switched to SteelSeries Sonar for my sound management, I needed to revamp it and make it compatible with the SteelSeries Sonar API.

## How does it work?
By using buttons on your taskbar you can quickly switch between two audio devices. The script makes use of the local Sonar API. 

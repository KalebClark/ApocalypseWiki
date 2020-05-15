# Apocpi
Apocalypse Wiki! This is a standard build of Kiwix Hotspot (which is NOT included in this repository), with some hardware additions that I have made. 

## Hardware Additions
- Raspberry Pi Touchscreen Display
- Temp Sensor & Fan
- Pi Supply Power Switch & Buttons
- Rugged Case

## Software Additions
- Kiosk Mode using Matchbox window manager
- Virtual Keyboard - Matchbox
- Software for power switch
- Custom script for temp sensor

## Installation
First do a basic install of Kiwix Hotspot. Add a 'ssh' file to the /boot partition and then login with normal raspi default credentials.

- Update APT
	- `sudo apt-get update`
- Install minimal xwindows
	- `sudo apt-get install --no-install-recommends xserver-xorg x11-xserver-utils xinit matchbox-window-manager`
- Install Chromium Browser
	- `sudo apt-get install --no-install-recommends chromium-browser`
- Install Matchbox virtual keyboard
	- `sudo apt-get install --no-install-recommends matchbox-keyboard`

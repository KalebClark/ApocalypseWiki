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

- Configure System
	- `sudo raspi-config`
	- Boot Options -> Desktop/CLI -> Console Autologin
	- Interfacing Options -> 1-Wire
- Update APT
	- `sudo apt-get update`
- Install minimal xwindows
	- `sudo apt-get install --no-install-recommends xserver-xorg x11-xserver-utils xinit matchbox-window-manager`
- Install Chromium Browser
	- `sudo apt-get install --no-install-recommends chromium-browser`
- Install Matchbox virtual keyboard
	- `sudo apt-get install --no-install-recommends matchbox-keyboard`
	
That should take care of the software installs. Now copy the .xsession file from this repository to the home directory of the user 'pi'

`cp .xsession ~`

Edit the .bashrc file in the home directory and add the following to the bottom

`startx -- -nocursor`

Now install the service.
- `sudo cp apocpi.service /etc/systemd/system/`
- `sudo systemctl enable apocpi.service`
- `sudo systemctl start apocpi.service`




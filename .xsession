#!/bin/bash
xset -dpms
xset s off
xset s noblank


# Remove exit errors from the config files that could trigger a warning
  
sed -i 's/"exited_cleanly":false/"exited_cleanly":true/' ~/.config/chromium/'Local State'
  
sed -i 's/"exited_cleanly":false/"exited_cleanly":true/; s/"exit_type":"[^"]\+"/"exit_type":"Normal"/' ~/.config/chromium/Default/Preferences

while true; do
	chromium-browser --noerrdialogs --disable-infobars --kiosk http://goto.kiwix.hotspot &

	# Hide the mouse cursor
	xinit -root -warp $( cat /sys/module/*fb*/parameters/fbwidth ) $( cat /sys/module/*fb*/parameters/fbheight )
	exec matchbox-window-manager -use_titlebar no -use_cursor no
	sleep 2
done


#!/bin/bash

PID=`pidof matchbox-keyboard`
DISPLAY=:0

if [ ! -e $PID ]; then
	kill $PID
else
	matchbox-keyboard &
fi


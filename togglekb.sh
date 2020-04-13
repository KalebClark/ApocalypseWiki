#!/bin/bash

PID=`pidof matchbox-keyboard`
echo $PID

if [ ! -e $PID ]; then
	kill $PID
else
	matchbox-keyboard &
fi


if [ -n "$SSH_CLIENT" ] || [ -n "$SSH_TTY" ]; then
	echo "SSH SESSION"
else
	export DISPLAY=:0
	startx -- -nocursor
fi

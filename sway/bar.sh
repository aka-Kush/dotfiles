#!/bin/bash
while true
do
	date=$(date +'%A, %b %d')
	time=$(date +'%I:%M %p')
	volume=$(pamixer --get-volume)
	brightness=$(( 100 * $(brightnessctl get) / $(brightnessctl max) ))
    battery_info=$(upower -i $(upower -e | grep BAT) | grep -oP 'percentage:\s*\K[0-9]+')
	echo "$brightness% | $volume% | $battery_info% | $date | $time  "
done 

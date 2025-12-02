#!/bin/bash

# Brightness step (adjust as needed)
STEP="5%"

# Function to get current brightness as a percentage
get_brightness() {
    brightnessctl get | awk -v max=$(brightnessctl max) '{ printf "%.0f", ($1 / max) * 100 }'
}

# Function to pick icon based on brightness
get_icon() {
    BRIGHT=$1
    if [ "$BRIGHT" -le 30 ]; then
        echo "display-brightness-low-symbolic"
    elif [ "$BRIGHT" -le 70 ]; then
        echo "display-brightness-medium-symbolic"
    else
        echo "display-brightness-high-symbolic"
    fi
}

# Handle arguments
case "$1" in
    up)
        brightnessctl set +$STEP
        ;;
    down)
        brightnessctl set $STEP-
        ;;
    *)
        echo "Usage: $0 {up|down}"
        exit 1
        ;;
esac

# Wait a bit to let brightness update
sleep 0.05

# Get updated brightness and icon
BRIGHTNESS=$(get_brightness)
ICON=$(get_icon $BRIGHTNESS)

# Send notification
dunstify -i "$ICON" -r 9994 -t 1500 "Brightness: $BRIGHTNESS%"

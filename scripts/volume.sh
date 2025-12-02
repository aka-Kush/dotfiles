#!/bin/bash

# Volume step
STEP="5%"

# Get current sink
SINK="@DEFAULT_AUDIO_SINK@"

# Function to get current volume as a percentage
get_volume() {
    wpctl get-volume $SINK | awk '{ printf "%.0f", $2 * 100 }'
}

# Function to get mute status (true/false)
is_muted() {
    wpctl get-volume $SINK | grep -q MUTED
}

# Function to pick icon based on volume
get_icon() {
    VOL=$1
    if is_muted; then
        echo "audio-volume-muted-symbolic"
    elif [ "$VOL" -eq 0 ]; then
        echo "audio-volume-muted-symbolic"
    elif [ "$VOL" -le 30 ]; then
        echo "audio-volume-low-symbolic"
    elif [ "$VOL" -le 70 ]; then
        echo "audio-volume-medium-symbolic"
    else
        echo "audio-volume-high-symbolic"
    fi
}

# Handle arguments
case "$1" in
    up)
        wpctl set-volume $SINK $STEP+
        ;;
    down)
        wpctl set-volume $SINK $STEP-
        ;;
    mute)
        wpctl set-mute $SINK toggle
        ;;
    *)
        echo "Usage: $0 {up|down|mute}"
        exit 1
        ;;
esac

# Wait a bit to let volume update
sleep 0.05

# Get updated volume and icon
VOLUME=$(get_volume)
ICON=$(get_icon $VOLUME)

# Send notification
dunstify -i "$ICON" -r 9993 -t 1500 "Volume: $VOLUME%"

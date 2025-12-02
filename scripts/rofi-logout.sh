#!/bin/bash

# Rofi appearance (you can adjust this)
ROFI_CMD="rofi -dmenu -p Power"

# Options
options="e: Logout\ns: Shutdown\nr: Reboot\nl: Lock"

# Show rofi menu and get selection
choice=$(echo -e "$options" | $ROFI_CMD)

case "$choice" in
    e*) hyprctl dispatch exit ;;
    s*) systemctl poweroff ;;
    r*) systemctl reboot ;;
    l*) hyprlock;; 
    *) exit 1 ;;
esac

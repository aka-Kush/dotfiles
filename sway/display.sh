#!/bin/bash

if swaymsg -t get_outputs | grep -q "HDMI-A-1"; then
    # External monitor connected - disable laptop screen, use external
    swaymsg output eDP-1 disable
    swaymsg output HDMI-A-1 enable
    
    # Set workspaces 1-8 on external monitor
    for i in {1..8}; do
        swaymsg workspace $i output HDMI-A-1
    done
else
    # No external monitor - use laptop screen only
    swaymsg output eDP-1 enable
    
    # Set workspaces 1-8 on laptop screen
    for i in {1..8}; do
        swaymsg workspace $i output eDP-1
    done
fi

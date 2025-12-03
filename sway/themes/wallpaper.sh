#!/usr/bin/env bash

WALL_DIR="$HOME/.config/themes/current/walls"

# Get random file, safely
wallpaper="$(find -L "$WALL_DIR" -type f | shuf -n 1)"
echo $wallpaper

if [[ -z "$wallpaper" ]]; then
    echo "Error: No wallpapers found in $WALL_DIR" >&2
    exit 1
fi

swaybg -m fill -i "$wallpaper" &
cp "$wallpaper" "$HOME/.config/sway/current_wall"

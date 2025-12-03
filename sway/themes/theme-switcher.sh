#!/usr/bin/env bash

THEME_DIR="$HOME/.config/themes"
CURRENT="$THEME_DIR/current"
LIST="$THEME_DIR/theme-list"

# Read list and show with tofi
choice=$(cat "$LIST" | tofi --prompt-text "Select theme:")

# Exit if no selection
[ -z "$choice" ] && exit 0

# Validate theme directory
if [ ! -d "$THEME_DIR/$choice" ]; then
    notify-send "Theme Switcher" "Theme '$choice' not found!"
    exit 1
fi

# Create current folder if needed
mkdir -p "$CURRENT"

# Clear current theme folder
rm -rf "$CURRENT"/*

# Copy new theme files
cp -r "$THEME_DIR/$choice/"* "$CURRENT/"

# Run launch.sh if exists
if [ -f "$CURRENT/launch.sh" ]; then
    chmod +x "$CURRENT/launch.sh"
    "$CURRENT/launch.sh"
else
    notify-send "Theme Switcher" "launch.sh not found in theme '$choice'"
    exit 1
fi

# dunst 
killall swaync; swaync & disown

# Notify success
notify-send "Theme Switcher" "Theme '$choice' applied successfully"

# apply wallpaper
$THEME_DIR/wallpaper.sh


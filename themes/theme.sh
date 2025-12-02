#!/usr/bin/env bash

# Directory containing all themes
THEMES_DIR="$HOME/.config/themes"
CURRENT_DIR="$THEMES_DIR/current"

# List all theme directories except 'current'
themes=($(find "$THEMES_DIR" -maxdepth 1 -mindepth 1 -type d -printf "%f\n" | grep -v "^current$"))
if [ ${#themes[@]} -eq 0 ]; then
    notify-send "Theme Switcher" "⚠️ No themes found in $THEMES_DIR."
    exit 1
fi

# Use rofi to pick a theme
chosen_theme=$(printf "%s\n" "${themes[@]}" | rofi -dmenu -p "Select theme:")

# Exit if no theme is selected
if [ -z "$chosen_theme" ]; then
    notify-send "Theme Switcher" "❌ No theme selected."
    exit 0
fi

# Remove old current theme folder
rm -rf "$CURRENT_DIR"

# Copy new theme to 'current'
cp -r "$THEMES_DIR/$chosen_theme" "$CURRENT_DIR"

# Launch new theme
bash "$CURRENT_DIR/launch.sh"

# Send final notification
notify-send "Theme Switcher" "✅ Theme '$chosen_theme' applied successfully!"

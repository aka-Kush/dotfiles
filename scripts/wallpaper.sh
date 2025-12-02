#!/usr/bin/env bash

# Wallpaper directory
WALLPAPER_DIR="$HOME/Pictures/walls"

# Build the menu with image previews
menu=""
declare -A wallpaper_map

while IFS= read -r wallpaper; do
    if [[ -f "$wallpaper" ]]; then
        filename=$(basename "$wallpaper")
        menu+="${filename}\0icon\x1f${wallpaper}\n"
        wallpaper_map["$filename"]="$wallpaper"
    fi
done < <(find "$WALLPAPER_DIR" -maxdepth 1 -type f \( -iname "*.jpg" -o -iname "*.jpeg" -o -iname "*.png" -o -iname "*.webp" -o -iname "*.bmp" \) | sort)

# Show rofi menu with image previews
selected=$(echo -e "$menu" | rofi -dmenu -i \
    -theme-str 'window {width: 70%;}' \
    -theme-str 'listview {columns: 5; lines: 4;}' \
    -theme-str 'element {orientation: vertical; padding: 10px;}' \
    -theme-str 'element-icon {size: 8em;}' \
    -theme-str 'element-text {horizontal-align: 0.5;}' \
    -p "Select Wallpaper")

# Set the selected wallpaper with swww
if [[ -n "$selected" ]]; then
    wallpaper_path="${wallpaper_map[$selected]}"
    if [[ -n "$wallpaper_path" ]]; then
        cp $wallpaper_path ~/.config/hypr/current_wallpaper
        swww img "$wallpaper_path" --transition-duration 1 --transition-type grow --transition-fps 144
        matugen image $wallpaper_path -m "dark"
        notify-send -u normal -i "$wallpaper_path" "Wallpaper Set" "Colors generated!"
    fi
fi

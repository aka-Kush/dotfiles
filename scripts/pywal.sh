#!/usr/bin/env bash

# --- CONFIGURATION ---
WALLPAPER="$1"
SOURCE_FILE="$HOME/.cache/wal/colors-waybar.css"
DEST_FILE="$HOME/.config/waybar/colors-waybar.css"
WALLPAPER_START="$HOME/.config/wall.jpg"

# --- CHECK ---
if [[ -z "$WALLPAPER" || ! -f "$WALLPAPER" ]]; then
  echo "Usage: $0 /path/to/image"
  exit 1
fi

# use wpgtk instead
wpg -n -s "$WALLPAPER" 
swww img "$WALLPAPER" --transition-type grow --transition-duration 1 --transition-fps 144

# Wait until wal has generated the required file
for i in {1..10}; do
  if [[ -f "$SOURCE_FILE" ]]; then
    break
  fi
  sleep 0.2
done

if [[ ! -f "$SOURCE_FILE" ]]; then
  echo "Error: $SOURCE_FILE not found after wal execution."
  exit 1
fi

# --- COPY COLOR FILE ---
cp "$SOURCE_FILE" "$DEST_FILE"
cp "$WALLPAPER" "$WALLPAPER_START"
# --- PARSE HEX COLOR ---
HEX_BG=$(grep -oP '@define-color background #\K[0-9a-fA-F]{6}' "$DEST_FILE")
if [[ -z "$HEX_BG" ]]; then
  echo "Error: Could not extract background color from $DEST_FILE"
  exit 1
fi

# --- CONVERT TO RGBA ---
R=$((16#${HEX_BG:0:2}))
G=$((16#${HEX_BG:2:2}))
B=$((16#${HEX_BG:4:2}))
ALPHA=0.75
RGBA_BG="rgba($R,$G,$B,$ALPHA)"

# --- MODIFY WAYBAR COLOR FILE ---
if grep -q "@define-color background-rgba" "$DEST_FILE"; then
  sed -i "s|@define-color background-rgba .*|@define-color background-rgba $RGBA_BG;|" "$DEST_FILE"
else
  sed -i "/@define-color background /a @define-color background-rgba $RGBA_BG;" "$DEST_FILE"
fi

# --- SPOTIFY ---
if pgrep -x "spotify" > /dev/null
then
    # Spotify is running
    cp ~/.cache/wal/colors.spicetify.ini ~/.config/spicetify/Themes/Pywal/color.ini
    pkill -SIGUSR1 spotify
    /home/kush/.spicetify/spicetify apply
    flatpak run com.spotify.Client &
else
    # Spotify is not running
    cp ~/.cache/wal/colors.spicetify.ini ~/.config/spicetify/Themes/Pywal/color.ini
    spicetify apply -n
fi

# --- DISCORD ---
if pgrep -x "Discord" > /dev/null; then
    pkill -SIGUSR1 "Discord"
    discord &
fi

# --- RESTART WAYBAR ---
killall -q waybar
waybar &



#!/bin/bash

# Kitty theme
kitten theme Catppuccin-Mocha
pkill -SIGUSR1 kitty

# waybar reload
bash /home/kush/.config/waybar/launch.sh &

# hyprland reload
hyprctl reload

# wallpaper logic
ln -sf ~/Pictures/Cat-walls ~/.config/themes/current/walls 
swww img /home/kush/Pictures/Cat-walls/astronaut.png --transition-duration 1 --transition-type grow --transition-fps 144 
cp /home/kush/Pictures/Cat-walls/astronaut.png ~/.config/hypr/current_wallpaper

# gtk themeing
gsettings set org.gnome.desktop.interface gtk-theme "catppuccin-mocha-mauve-standard+default"

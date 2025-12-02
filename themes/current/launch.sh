#!/bin/bash

# Kitty theme
kitten theme gruvbox\ dark 
pkill -SIGUSR1 kitty

# waybar reload
bash /home/kush/.config/waybar/launch.sh &

# hyprland reload
hyprctl reload

# wallpaper logic
ln -sf ~/Pictures/Gruv-walls ~/.config/themes/current/walls
swww img /home/kush/Pictures/Gruv-walls/skull.jpg --transition-duration 1 --transition-type grow --transition-fps 144 
cp ~/Pictures/Gruv-walls/skull.jpg ~/.config/hypr/current_wallpaper

# gtk theme
gsettings set org.gnome.desktop.interface gtk-theme "Gruvbox-Material-Dark"

#!/bin/bash

# Kitty theme
kitten theme Rosé Pine
pkill -SIGUSR1 kitty

# gtk theme
gsettings set org.gnome.desktop.interface gtk-theme "rose-pine-gtk"

# neovim
echo "return 'rose-pine'" > ~/.config/nvim/lua/theme.lua

# sway reload 
swaymsg reload

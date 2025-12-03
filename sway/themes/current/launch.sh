#!/bin/bash

# Kitty theme
kitten theme gruvbox\ dark 
pkill -SIGUSR1 kitty

# gtk theme
gsettings set org.gnome.desktop.interface gtk-theme "Gruvbox-Material-Dark"

# neovim
echo "return 'gruvbox'" > ~/.config/nvim/lua/theme.lua

# sway reload 
swaymsg reload

#! /bin/bash

killall waybar
waybar -c ./config -s ./styles.css &

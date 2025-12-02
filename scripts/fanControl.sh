#!/bin/bash

BOOST_PATH="/sys/devices/platform/hp-wmi/hwmon/hwmon6/pwm1_enable"

current_state=$(cat "$BOOST_PATH")

case "$current_state" in
    0)
        echo 2 | sudo tee "$BOOST_PATH" > /dev/null
        notify-send -i fan "Fan Mode" "💤 Boost mode OFF"
        ;;
    2)
        echo 0 | sudo tee "$BOOST_PATH" > /dev/null
        notify-send -i fan "Fan Mode" "🌀 Boost mode ON"
        ;;
    *)
        notify-send -i dialog-warning "Fan Mode" "Unknown fan mode: $current_state"
        ;;
esac

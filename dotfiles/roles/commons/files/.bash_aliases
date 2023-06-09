#!/usr/bin/env bash

alias gpg='gpg2'
alias getBattery='upower -i /org/freedesktop/UPower/devices/battery_BAT0'
alias getclip='xclip -selection c -o'
alias setclip='xclip -selection c'
alias t_get='gsettings get org.gnome.desktop.peripherals.touchpad send-events'
alias cookieFortune='cowsay -f $(cowsay -l | tail -n +2 | xargs | tr " " "\n" | shuf -n 1) $(fortune)'
alias urldecode='python3 -c "import sys, urllib.parse as ul;print(ul.unquote_plus(sys.argv[1]))"'

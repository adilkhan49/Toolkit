#!/usr/bin/env bash

cd ~/Downloads
youtube-dl -U
youtube-dl `pbpaste` -f 140 --no-check-certificate
open "$(youtube-dl `pbpaste` -f 140 --no-check-certificate --get-filename)"
rm "$(youtube-dl `pbpaste` -f 140 --no-check-certificate --get-filename)"
osascript -e 'tell application "iTunes" to pause'

#!/usr/bin/env bash

random_url() {
    wget --quiet "http://hub.local/api/wallpapers/random/" -O - \
	| jq -r '.image'
}

download_new_image() {
    wget --quiet "$(random_url)" -O /tmp/wallpaper
}

is_raspbian() {
    [[ "$(grep -c "ID=raspbian" /etc/os-release)" != "0" ]]
}

set_wallpaper() {
    if is_raspbian; then
	pcmanfm --set-wallpaper "/tmp/wallpaper"
    else
	gsettings set org.gnome.desktop.background picture-uri "file://tmp/wallpaper"
    fi
}

download_new_image
set_wallpaper

#!/usr/bin/env bash

sudo dnf install -y git vim stow
#TODO Prompt custom

# FIXME Does not work
#stow gitconfig

# https://dbeley.ovh/post/2021/01/09/g%C3%A9rer-ses-fichiers-de-configuration-sous-linux-avec-stow/
# https://www.gnu.org/software/stow/manual/html_node/Invoking-Stow.html#Invoking-Stow

stow .

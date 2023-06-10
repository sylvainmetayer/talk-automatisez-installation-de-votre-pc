#!/usr/bin/env bash


pip3 install --user psutil
python3 -m pip install --user -r "requirements.txt"
ansible-galaxy role install -r "requirements.yml"
ansible-galaxy collection install -r "requirements.yml"

# ansible vault password
echo "sylvain" > ~/.ansible_vault.txt

#!/usr/bin/env bash


pip3 install --user psutil
python3 -m pip install --user -r "requirements.txt"
ansible-galaxy role install -r "requirements.yml"
ansible-galaxy collection install -r "requirements.yml"

# ansible vault password
echo "sylvain" > ~/.ansible_vault.txt

# For demo purpose, do not ever store your sudo password in plaintext !!
EXTRA_ARGS="--extra-vars 'ansible_become_password=sylvain'"
ANSIBLE_VAULT_PASSWORD_FILE=~/.ansible_vault.txt ansible-playbook playbooks/demo/main.yaml $EXTRA_ARGS

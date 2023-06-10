# Démo dotfiles

## Initial Setup

- `dnf install git python3-pip`
- `git clone https://github.com/sylvainmetayer/talk-automatisez-installation-de-votre-pc`
- `./scripts/install-ansible-deps.sh`

## Usage

### Demo

Demo on a VM

- `ANSIBLE_VAULT_PASSWORD_FILE=~/.ansible_vault.txt ansible-playbook playbooks/demo/main.yaml -K`
- `systemctl status --user ssh-agent` to get the `SSH_AUTH_SOCK` value
  - Configure KeepassXC to use this socket

- view file : `ANSIBLE_VAULT_PASSWORD_FILE=~/.ansible_vault.txt ansible-vault view secret_data.txt`
- edit file : `ANSIBLE_VAULT_PASSWORD_FILE=~/.ansible_vault.txt ansible-vault edit secret_data.txt`
- encrypt file : `ANSIBLE_VAULT_PASSWORD_FILE=~/.ansible_vault.txt ansible-vault encrypt secret_data.txt`
- decrypt file: `ANSIBLE_VAULT_PASSWORD_FILE=~/.ansible_vault.txt ansible-vault decrypt secret_data.txt`

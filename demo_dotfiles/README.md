# Démo dotfiles

## Initial Setup

- `dnf install git keepassxc python3-pip`
- `git clone https://github.com/sylvainmetayer/dotfiles.git $HOME/dotfiles`
- `./scripts/install-ansible-deps.sh`

## Usage

### Demo

Demo on a VM

- `ansible-playbook playbooks/demo/main.yaml -K`
- `systemctl status --user ssh-agent` to get the `SSH_AUTH_SOCK` value
  - Configure KeepassXC to use this socket

- `FILE=$HOME/dotfiles/roles/gop/templates/aws_config.j2`
- `FILE=$HOME/dotfiles/roles/gop/templates/ssh_hosts.j2`
- `FILE=$HOME/dotfiles/playbooks/gop/locals.yml`

- view file : `ANSIBLE_VAULT_PASSWORD_FILE=~/.ansible_vault.txt ansible-vault view $FILE`
- edit file : `ANSIBLE_VAULT_PASSWORD_FILE=~/.ansible_vault.txt ansible-vault edit $FILE`
- encrypt file : `ANSIBLE_VAULT_PASSWORD_FILE=~/.ansible_vault.txt ansible-vault encrypt $FILE`
- decrypt file: `ANSIBLE_VAULT_PASSWORD_FILE=~/.ansible_vault.txt ansible-vault decrypt $FILE`

Use the following command : `ANSIBLE_VAULT_PASSWORD_FILE=~/.ansible_vault.txt ansible-playbook playbooks/gop/main.yml -K` to run the playbook and decrypt the files.

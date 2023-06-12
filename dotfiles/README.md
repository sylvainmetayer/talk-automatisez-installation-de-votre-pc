# Démo dotfiles

## Initial Setup

- `dnf install git python3-pip`
- `git clone https://github.com/sylvainmetayer/talk-automatisez-installation-de-votre-pc`
- `./scripts/bootstrap.sh` Will install dependencies and start demo playbook with the sudo password on the demo VM

## Usage

- `ANSIBLE_VAULT_PASSWORD_FILE=~/.ansible_vault.txt ansible-playbook playbooks/demo/main.yaml -K`

- view file : `ANSIBLE_VAULT_PASSWORD_FILE=~/.ansible_vault.txt ansible-vault view secret_data.txt`
- edit file : `ANSIBLE_VAULT_PASSWORD_FILE=~/.ansible_vault.txt ansible-vault edit secret_data.txt`
- encrypt file : `ANSIBLE_VAULT_PASSWORD_FILE=~/.ansible_vault.txt ansible-vault encrypt secret_data.txt`
- decrypt file: `ANSIBLE_VAULT_PASSWORD_FILE=~/.ansible_vault.txt ansible-vault decrypt secret_data.txt`

## demo

```shell
git clone https://github.com/sylvainmetayer/talk-automatisez-installation-de-votre-pc.git
./scripts/bootstrap.sh

source ~/.bashrc # montrer
newgrp docker
docker container run hello-world
# ouvrir jetbrain + spotify + vscode
ls -ail $HOME
cat $HOME/.gitconfig
cat $HOME/.vimrc
cat $HOME/secret_data.txt
```

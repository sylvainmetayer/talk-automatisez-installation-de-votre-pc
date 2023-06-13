# Ansible

---

## Avantages / Inconvénients

| Objectif                                | État |
|-----------------------------------------|------|
| Gérer mes fichiers de configuration     | ✅    |
| Gérer les logiciels installés           | ✅    |
| Versionnable                            | ✅    |
| Facilement maintenable                  | ✅    |
| Gérer mon poste de travail pro et perso | ✅    |
| Gestion de secrets                      | ✅    |

speaker:

- Peu de prérequis
- Vous utilisez déjà ansible pour votre configuration de machines ?
- Roles / Playbooks (séparer PC pro/perso)
- Syntaxe YAML

Cependant, si pas d'usage d'ansible autre que pour un seul poste, peu être "lourd" à mettre en place

---

## Concrètement, comment fait-on ?

<img src="assets/img/tell_me_more.gif"  height="300" width="600" alt="Tell me more">

speaker:

- Structure
- Usage
- Symlink
- Gestion des secrets
- Plusieurs machines

Structure : 

roles, tasks, playbook, variables

Ansible galaxy fournit plein de roles déjà prêt (exemple : Guerrlinguy docker) pour setup votre pc

Usage : 

montrer script bootstrap rapidement

Installation de packages : 

dotfiles/roles/fedora_dependencies/tasks/main.yaml

Symlink : 

dotfiles/roles/commons/tasks/symlink.yml + fonction gitignore à présenter

Templating : Dire que possible si besoin de boucles à partir de variables, mais ne pas présenter et renvoyer vers la documentation

Montrer résultat de gitconfig

Gestion des secrets : secret_data.txt + bootstrap.sh

Plusieurs machines : playbooks demo + work avec variables différentes

---

### Et comment on fait...

<https://docs.ansible.com/>

<https://galaxy.ansible.com/>

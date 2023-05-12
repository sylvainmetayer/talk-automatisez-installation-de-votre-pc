# Notes

Question en amont : Combien dans la salle ont changé de poste récemment ? Combien de temps pour réinstaller tous les outils + la config ? Et si on faisait qqch qui va vous suivre au long de votre carrière et qui lors de votre prochain changement de PC vous fera gagner du temps ?

## Dotfiles

Les fichiers de configurations de notre poste.

Ces fichiers contiennent souvent les préférences utilisateurs, tel quel configuration git / vim / extension vscode...

Chacun a ses propres préférences et sa propre façon de gérer ses dotfiles, et ces derniers représentent souvent la majorité de la "customisation" de notre poste.

Les dotfiles ne sont pas uniquement les composants nécessaire à l'automatisation de son poste, mais représente une grande partie.

avantages : les versionnner !

Réinstaller un logiciel, c'est rapide, mais réinstaller sa config, ça peut être plus long. Avoir la config sous forme de dotfiles, c'est l'assurance de pouvoir repartir de la même base sur son editeur / application.

un dotfiles par utilisateur, et environ une méthode de dotfiles par utilisateur.

=====

exemples ansible :

<https://github.com/geerlingguy/ansible-role-dotfiles> pour install de config simple.

## copier coller

facile, on copie colle dans un dépôt git nos fichier de config, et quand on réinstaller son pc, on a juste à cloner le dépôt et à les remettre au bon endroit.

Facile, sauf quand on met à jour ses fichiers régulièrement ou que la configuration est différente entre plusieurs PC (pro/perso, identité git, clé SSH différente)... Et puis, on m'a promis une installation de mon pc, comment ça va installer mes logiciels ça ?

Démo vraiment nécessaire ?

## script

démo shell d'installation de vim / git + symlink d'un fichier de config git et d'un bashrc de démo

## Stow

On m'a promis un outil pour gérer mon installation, je vais pas non plus tout coder !

Avantage

Simple à mettre en place

Fais une chose bien, mais ne fait que ça, pour du templating par poste ou des installations spécifiques, va falloir rester sur du custom..

secret: (je le mets ou le contenu de mon docker.cfg pour me logguer sur dockerhub ?)

Démo : stow de quelques fichiers avec arborescence. Stow d'un fichier dans un dossier network manager voir <https://dbeley.ovh/post/2021/01/09/g%C3%A9rer-ses-fichiers-de-configuration-sous-linux-avec-stow/>

## Ansible

- Syntaxe YAML qui peut être capricieuse (indentation / chaine de caractères...)

- Démo 1 : Lancer l'exemple dotfiles de [geerlingguy](https://github.com/geerlingguy/ansible-role-dotfiles). Faire le pont avec stow
- Démo 2 : Installation paquet : on installe vim / git / vscode. + paquet flatpak (depuis mon poste.)
-

et comment on fait... ? Docs ansible avec roles / modules multiples pour répondre à quasi tous les besoins. Galaxy avec des rôles déjà pré-établis.

## Conclusion

Chaque PC est unique, chaque utilisateur est unique. Il existe plein de façon de gérer ses fichiers et la gestion de son PC.

Au cours de cette présentation, plusieurs méthodes ont tentés de répondre au besoin de pouvoir réinstaller son PC sans être trop embêté, mais au final, c'est à vous de choisir la solution qui vous convient.

Exemple de mon dotfiles perso.

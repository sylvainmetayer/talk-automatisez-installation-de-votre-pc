## Dotfiles, c'est quoi ?

<blockquote cite="<https://wiki.archlinux.org/title/Dotfiles>">
&ldquo;User-specific application configuration is traditionally
stored in so called dotfiles (files whose filename starts with a dot).&rdquo;
</blockquote>

<small><a href='https://wiki.archlinux.org/title/Dotfiles'>https://wiki.archlinux.org/title/Dotfiles</a></small>

---

## Exemple

```shell
$ ❯ cat ~/.bashrc
#!/usr/bin/env bash

if [ -f /etc/bashrc ]; then
 . /etc/bashrc
fi

export SSH_AUTH_SOCK=/run/user/1000/ssh-agent.socket
# ...
```

> Et d'autres : vimrc, gitconfig, ...

---

[//]: # (## Avantages)
[//]: # ()
[//]: # (<img src="assets/img/git.jpeg"  height="400" width="400" alt="Git">)
[//]: # ()
[//]: # (---)

## Comment fait-on ?

<img src="assets/img/do-it.gif"  height="300" width="600" alt="Do ti">

<https://dotfiles.github.io/>

<https://github.com/webpro/awesome-dotfiles>


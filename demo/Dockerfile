FROM fedora
RUN dnf install sudo util-linux flatpak -y
RUN adduser demo
RUN usermod -aG wheel demo
RUN echo "%wheel ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers
USER demo
WORKDIR /home/demo

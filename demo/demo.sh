#!/usr/bin/env bash

build() {
    docker build -t demo .
}

demo1() {
    docker run --cap-add CAP_SYS_ADMIN -it --rm -v $(pwd)/../dotfiles/:/home/demo/dotfiles test bash
}

$1


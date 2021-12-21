FROM ubuntu:21.04@sha256:93a94c12448f393522f44d8a1b34936b7f76890adea34b80b87a245524d1d574 AS build-stage

RUN apt-get update && \
    yes | unminimize

ENV DEBIAN_FRONTEND=noninteractive
ENV TZ=Etc/UTC
RUN apt install -y man zsh curl git wget python-is-python3 python3-pip \
                   net-tools iproute2 arping arp-scan dsniff \
                   inetutils-tools inetutils-ping inetutils-traceroute

RUN pip install ipython ipdb

RUN sh -c "$(curl -fsSL https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"

WORKDIR /root
RUN sed -r "s/ZSH_THEME=\"\w+\"/ZSH_THEME=\"bureau\"/" .zshrc | tee ./.zshrc

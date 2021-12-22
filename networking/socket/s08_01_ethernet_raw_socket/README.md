# Raw Ethernet sockets

## Purpose

Attempt to send a binary message from one machine to another using nothing else but **raw Ethernet sockets**.

## Pre-requisites

**i_python_exploration_dev_ubuntu** must be built with the `00_dev_utils/01_dev_docker_container/generate_image.sh` script.

## Steps to setup

1. Run `generate_image.sh` which will build a special tailored image from **i_python_exploration_dev_ubuntu**
2. Run `docker compose up -d`
3. Open two terminals
  * in first terminal run `docker compose exec machine_a /bin/zsh`
  * in second termina run `docker compose exec machine_b /bin/zsh`

## How to use

1. In **machine_b** run `python -B process_b.py`. This will start the receiver and will wait for Ethernet frames.
2. In **machine_b** run `python -B process_a.py`. This will send one Ethernet frame to **machine_a**.

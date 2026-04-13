# PocketBook SSH

This CLI application allows you to transfer files to/from your e-reader using SFTP (SSH files transfer protocol).

## Requirements

1. PocketBook device with installed KOReader. Installation instructions: https://github.com/koreader/koreader/wiki/Installation-on-PocketBook-devices.
2. Python version 3.11 or later.

## Usage

1. Clone the project.
2. Run `./main.sh` in a terminal:
   1. If you're running the application for the first time, start with generating SSH keys and config setup.
   2. Follow friendly interface with instructions.

## Application features

- Generate SSH keys using `ssh-keygen` for secure files transfer.
- Setup config entering device's home path, SSH Server IP and PORT.
- Download or upload files using `sftp`.

## Troubleshooting

Common issues and how to resolve them.

#### SSH server's IP address has been changed

1. Select `Setup device config` in the main menu and set new IP address.
2. Replace an old IP address in the `~/.ssh/known_hosts` file with the new one.

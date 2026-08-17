# PocketBook SSH

This CLI application allows you to transfer files to/from your e-reader using SFTP (SSH File Transfer Protocol).

## Requirements

1. PocketBook device with KOReader installed. Installation instructions: https://github.com/koreader/koreader/wiki/Installation-on-PocketBook-devices.
2. Python version 3.11 or later.
3. `uv` (or install `prompt-toolkit` manually with pip).

## Usage

1. Clone the project and go to its folder.
2. Install dependencies: `uv sync`
3. Run `./main.sh` in a terminal:
   1. If you're running the application for the first time, start with generating SSH keys and config setup.
   2. Follow the user-friendly on-screen instructions.

## Application features

- Generate SSH keys using `ssh-keygen` for secure file transfer.
- Set up config by entering the device's home path, SSH server IP, and port.
- Transfer files using `sftp`.
- Check connection with the device using `ssh`.

## Troubleshooting

Common issues and how to resolve them.

#### SSH server's IP address has been changed

1. Select `Set up device config` in the main menu and set the new IP address.
2. Replace (or delete) an old IP address in the `~/.ssh/known_hosts` file.

#### SSH connection failed

1. Make sure `...koreader/settings/SSH/authorized_keys` has the contents of the `.keys/ecdsa.pub` file.
2. Delete a device's IP address from the `~/.ssh/known_hosts` file and run `Check connection` command from the main menu.

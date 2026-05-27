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
- Download or upload files using `sftp`.

## Troubleshooting

Common issues and how to resolve them.

#### SSH server's IP address has been changed

1. Select `Setup device config` in the main menu and set the new IP address.
2. Replace the old IP address in the `~/.ssh/known_hosts` file with the new one.

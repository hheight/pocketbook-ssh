# PocketBook SSH

This CLI application allows you to transfer files to/from your e-reader using SFTP (SSH File Transfer Protocol).

## Requirements

1. PocketBook device with KOReader installed. Installation instructions: https://github.com/koreader/koreader/wiki/Installation-on-PocketBook-devices.
2. Python version 3.11 or later.
3. `uv`.
4. OpenSSH client tools (`ssh`, `sftp`, and `ssh-keygen`) available on your `PATH`.

## Usage

1. Clone the project and go to its folder.
2. Run `./main.sh` in a terminal. The script uses `uv` to create or update the project environment and install dependencies.
3. On first use, select **Generate a new SSH key pair** and follow the instructions to add `.keys/ecdsa.pub` to the device's `authorized_keys` file.
4. Select **Set up device config** and enter the device's home path, SSH server IP, and port. Make sure the SSH server is enabled in KOReader.
5. Select **Check connection** to verify the setup, then use **Transfer files** to upload or download.

## Application features

- Generate SSH keys using `ssh-keygen` for secure file transfer.
- Set up config by entering the device's home path, SSH server IP, and port.
- Transfer files using `sftp`.
- Check connection with the device using `ssh`.

## Troubleshooting

Common issues and how to resolve them.

#### SSH server's IP address has been changed

1. Select `Set up device config` in the main menu and set the new IP address.
2. Remove the old host entry from `~/.ssh/known_hosts`. For a non-default SSH port, the entry may be written as `[IP]:port`.

#### SSH connection failed

1. Make sure `...koreader/settings/SSH/authorized_keys` contains the public key from `.keys/ecdsa.pub` and that KOReader's SSH server is enabled.
2. If the error reports a changed host key, remove the old entry with `ssh-keygen -R <IP>`; for a non-default port, use `ssh-keygen -R '[<IP>]:<PORT>'`.
3. Run **Check connection** from the main menu again.

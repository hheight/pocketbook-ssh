import os
import subprocess

from style_text import style_text

ssh_keys_dirname = "ssh_keys"
ssh_keys_path = f"{os.path.abspath(os.getcwd())}/{ssh_keys_dirname}"

def generate_keys():
    if not os.path.isdir(ssh_keys_path):
        os.mkdir(ssh_keys_dirname);

    subprocess.run([
        "ssh-keygen",
        "-t", "ecdsa",
        "-f", f"{ssh_keys_path}/ecdsa",
        "-N", ""
    ])

    print_next_steps()

def print_next_steps():
    print("\n")
    print(style_text(style_text("Next steps:", "bold"), "green"))
    print(f"     1. On your device access the main koreader directory. Inside it you will find the directory `{style_text('settings/SSH', 'yellow')}`")
    print(f"     2. If a `{style_text('authorized_keys', 'yellow')}` file doesn't exist then create it. Paste the single line from your `{style_text('.pub', 'yellow')}` key pair to this file.")
    print(f"     3. Note, the `{style_text('authorized_keys', 'yellow')}` file doesn't have an extension. If you want to add other public keys to it you can add each one on a new line.")
    print("\n")


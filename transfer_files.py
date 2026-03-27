import os
import subprocess
from prompt_toolkit.shortcuts import prompt

from style_text import style_text

pocketbook_home_folder_path = "/mnt/ext1/"

def transfer_files(action, keys_path):
    """
    Transfers files between devices using SFTP.
    SFTP (SSH File Transfer Protocol) is a secure file protocol for accessing, managing, and transferring files over an encrypted SSH connection.
    """

    if action == "download":
        device_files_path = prompt("Enter the path to a file or folder from the device's home folder: /")
        download_from_path = os.path.join(pocketbook_home_folder_path, device_files_path)

        save_to_path = prompt("Enter the absolute path where to save files: ")

        # TODO: write commands with paths to sftp_commands.txt
        print(download_from_path)
        print(save_to_path)
    elif action == "upload":
        print("Uploading")

    try:
        print("Connecting to the device...")
        connect_to_device(keys_path)
    except Exception:
        print(f"{style_text('Failed to connect.', 'red')} Please check that SSH server is started on the device.")
        return

def connect_to_device(keys_path):
    subprocess.run([
        "sftp",
        "-b", "sftp_commands.txt",
        "-i", f"{keys_path}/ecdsa",
        "-P", "2222",
        "reader@192.168.1.11"
        ], 
        timeout=7
    )

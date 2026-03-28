import json
import os
import subprocess

from prompt_toolkit.shortcuts import prompt
from constants import CONFIG_FILE, COMMANDS_FILE
from style_text import style_text
from pathlib import Path


def transfer_files(action, keys_path):
    """
    Transfers files between devices using SFTP.
    SFTP (SSH File Transfer Protocol) is a secure file protocol for accessing, managing, and transferring files over an encrypted SSH connection.
    """

    try:
        config = get_config()
    except Exception as e:
        print(e)
        return

    if action == "download":
        device_files_path = prompt("Enter the path to a file or folder from the device's home folder: ")
        download_from_path = os.path.join("/", config["homepath"], device_files_path)
        save_to_path = os.path.join("/", prompt("Enter the path where to save files: "))

        with open(COMMANDS_FILE, "w") as f:
            f.write(f"get -r {download_from_path} {save_to_path}\nbye")

    elif action == "upload":
        print("Uploading")

    try:
        print("Connecting to the device...")
        connect_to_device(keys_path, str(config["port"]), config["ip"])
        print(style_text("Files transfered successfully!", "green"))
    except Exception as e:
        print(e)
        return

def connect_to_device(keys_path, port, ip):
    process = subprocess.Popen(
        [
            "sftp",
            "-b", COMMANDS_FILE,
            "-i", f"{keys_path}/ecdsa",
            "-P", str(port),
            f"reader@{ip}"
        ],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True
    )

    output_lines = []

    if process.stdout:
        for line in process.stdout:
            print(line, end="")
            output_lines.append(line)

    process.wait()

    if process.returncode != 0:
        raise Exception(
            f"{style_text('SFTP failed', 'red')} (code {process.returncode})\n"
            f"{''.join(output_lines)}"
        )

def get_config():
    config_path = Path(CONFIG_FILE)

    if not config_path.exists() or not config_path.read_text():
        raise Exception(f"{style_text('Missing config file.', 'red')} Please setup device config from the main menu.")

    config = json.loads(config_path.read_text())

    if not config.get("homepath") or not config.get("ip") or not config.get("port"):
        raise Exception(f"{style_text('Missing config elements.', 'red')} Please fill device config.")

    return config

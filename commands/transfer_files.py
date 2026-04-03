import json
import subprocess
from pathlib import Path

from prompt_toolkit.shortcuts import prompt
from prompt_toolkit.styles import Style

from constants import COMMANDS_FILE, CONFIG_FILE
from utils.style_text import style_text

ROOT_PATH = Path("/")

style = Style.from_dict(
    {
        # User input (default text).
        "": "ansicyan",
        # Prompt.
        "title": "ansiyellow",
        "path": "ansicyan",
    }
)


def transfer_files(action, keys_path):
    """
    Transfers files between devices using SFTP.
    SFTP (SSH File Transfer Protocol) is a secure file protocol for accessing, managing, and transferring files over an encrypted SSH connection.
    """

    config = get_config()

    device_homepath = config.get("homepath")
    device_ip = config.get("ip")
    device_port = config.get("port")

    if action == "download":
        download_from = prompt(
            [("class:title", "FROM: ")], default=device_homepath, style=style
        )
        download_from_path = ROOT_PATH / device_homepath / download_from

        save_to = prompt([("class:title", "TO: ")], default=str(ROOT_PATH), style=style)
        save_to_path = ROOT_PATH / save_to

        with open(COMMANDS_FILE, "w") as f:
            f.write(f"get -r {download_from_path} {save_to_path}\nbye")

    elif action == "upload":
        upload_from = prompt(
            [("class:title", "FROM: ")], default=str(ROOT_PATH), style=style
        )
        upload_from_path = ROOT_PATH / upload_from

        upload_to = prompt(
            [("class:title", "TO: ")], default=device_homepath, style=style
        )
        upload_to_path = ROOT_PATH / device_homepath / upload_to

        with open(COMMANDS_FILE, "w") as f:
            f.write(f"put -r {upload_from_path} {upload_to_path}\nbye")

    print("Connecting to the device...")
    run_commands(keys_path, str(device_port), device_ip)
    print(style_text("Files transfered successfully!", "green"))


def run_commands(keys_path, port, ip):
    process = subprocess.Popen(
        [
            "sftp",
            "-b",
            COMMANDS_FILE,
            "-i",
            f"{keys_path}/ecdsa",
            "-P",
            str(port),
            f"reader@{ip}",
        ],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
    )

    if process.stdout:
        for line in process.stdout:
            print(line, end="")

    process.wait()

    if process.returncode != 0:
        raise Exception(
            f"{style_text('SFTP failed', 'red')} (code {process.returncode})"
        )


def get_config():
    config_path = Path(CONFIG_FILE)

    if not config_path.exists() or not config_path.read_text():
        raise Exception(
            f"{style_text('Missing config file.', 'red')} Please setup device config from the main menu."
        )

    config = json.loads(config_path.read_text())

    if not config.get("homepath") or not config.get("ip") or not config.get("port"):
        raise Exception(
            f"{style_text('Missing config elements.', 'red')} Please fill device config."
        )

    return config

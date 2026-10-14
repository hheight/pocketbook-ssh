import subprocess
from pathlib import Path
from typing import Literal

from prompt_toolkit.completion import PathCompleter
from prompt_toolkit.shortcuts import prompt
from prompt_toolkit.styles import Style

from commands import config
from constants import COMMANDS_FILE
from utils import text

ROOT_PATH = Path("/")
path_completer = PathCompleter(only_directories=False, expanduser=True)

style = Style.from_dict(
    {
        # User input (default text).
        "": "ansicyan",
        # Prompt.
        "title": "ansiyellow",
        "path": "ansicyan",
        # Autocomplete menu
        "completion-menu": "bg:ansicyan #ffffff",
        "completion-menu.completion": "bg:ansicyan #ffffff",
        "completion-menu.completion.current": "bg:ansicyan #ffffff",
    }
)


def transfer(action: Literal["download", "upload"], keys_path: Path) -> None:
    """
    Transfer files between devices using SFTP.

    SFTP (SSH File Transfer Protocol) is a secure file protocol for accessing, managing, and transferring files over an encrypted SSH connection.
    """

    cfg_obj = config.get()

    device_homepath = cfg_obj["homepath"]
    device_ip = cfg_obj["ip"]
    device_port = cfg_obj["port"]

    if action == "download":
        download_from = prompt(
            [("class:title", "FROM: ")], default=device_homepath, style=style
        )
        download_from_path = ROOT_PATH / device_homepath / download_from

        save_to = prompt(
            [("class:title", "TO: ")],
            default=str(ROOT_PATH),
            completer=path_completer,
            style=style,
        )
        save_to_path = ROOT_PATH / save_to

        _write_to_commands_file("get", download_from_path, save_to_path)

    if action == "upload":
        upload_from = prompt(
            [("class:title", "FROM: ")],
            default=str(ROOT_PATH),
            completer=path_completer,
            style=style,
        )
        upload_from_path = ROOT_PATH / upload_from

        upload_to = prompt(
            [("class:title", "TO: ")], default=device_homepath, style=style
        )
        upload_to_path = ROOT_PATH / device_homepath / upload_to

        _write_to_commands_file("put", upload_from_path, upload_to_path)

    print("Connecting to the device...")
    _run_commands(keys_path, str(device_port), device_ip)
    print(text.style("Files transferred successfully!", "green"))


def _write_to_commands_file(
    command: Literal["put", "get"], from_path: Path, to_path: Path
) -> None:
    """Write commands to a file."""

    with open(COMMANDS_FILE, "w") as f:
        f.write(f'progress\n{command} -r "{from_path}" "{to_path}"\nbye')


def _run_commands(keys_path: Path, port: str, ip: str) -> None:
    """Run commands from a file using subprocess."""

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
        ]
    )

    if process.wait() != 0:
        raise Exception(
            f"{text.style('SFTP failed', 'red')} (code {process.returncode})"
        )

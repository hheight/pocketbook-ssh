import subprocess
import sys
import threading
from itertools import cycle
from pathlib import Path

from commands import config
from utils import text


def _communicate_with_spinner(
    process: subprocess.Popen, message: str
) -> str:
    """Wait for the SSH check while showing activity in an interactive terminal."""

    if not sys.stdout.isatty():
        output, _ = process.communicate()
        return output or ""

    stop_spinner = threading.Event()

    def animate() -> None:
        for frame in cycle("|/-\\"):
            if stop_spinner.is_set():
                break
            print(f"\r{message} {frame}", end="", flush=True)
            if stop_spinner.wait(0.12):
                break

    spinner = threading.Thread(target=animate, daemon=True)
    spinner.start()
    try:
        output, _ = process.communicate()
        return output or ""
    finally:
        stop_spinner.set()
        spinner.join()
        print("\r\033[K", end="", flush=True)


def ensure_connection(
    keys_path: Path,
    port: str,
    ip: str,
    message: str = "Checking connection to PocketBook",
) -> None:
    """Run an SSH connection check, showing activity while it is pending."""
    process = subprocess.Popen(
        [
            "ssh",
            "-T",
            "-i",
            f"{keys_path}/ecdsa",
            "-p",
            str(port),
            f"reader@{ip}",
            "exit",
        ],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
    )

    output = _communicate_with_spinner(process, message)
    if output:
        print(output, end="" if output.endswith("\n") else "\n")

    if process.wait() != 0:
        raise Exception(
            f"{text.style('Connection failed', 'red')} (code {process.returncode})"
        )


def check(keys_path: Path) -> None:
    """Check SSH connection with the device."""

    cfg_obj = config.get()
    ensure_connection(keys_path, cfg_obj["port"], cfg_obj["ip"])
    print(text.style("Connection successful.", "green"))

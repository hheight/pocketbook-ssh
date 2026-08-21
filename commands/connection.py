import subprocess

from commands import config
from utils import text


def check(keys_path):
    """
    Checks SSH connection with the device.
    """
    cfg_obj = config.get()

    process = subprocess.Popen(
        [
            "ssh",
            "-T",
            "-i",
            f"{keys_path}/ecdsa",
            "-p",
            str(cfg_obj.get("port")),
            f"reader@{cfg_obj.get('ip')}",
            "exit",
        ],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
    )

    if process.stdout:
        for line in process.stdout:
            print(line)

    if process.wait() != 0:
        raise Exception(
            f"{text.style('Connection failed', 'red')} (code {process.returncode})"
        )
    else:
        print(text.style("Successful connection", "green"))

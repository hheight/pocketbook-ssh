import subprocess

from commands.setup_config import get_config
from utils.style_text import style_text


def check_connection(keys_path):
    """
    Checks SSH connection with the device.
    """
    config = get_config()

    device_ip = config.get("ip")
    device_port = config.get("port")

    process = subprocess.Popen(
        [
            "ssh",
            "-T",
            "-i",
            f"{keys_path}/ecdsa",
            "-p",
            str(device_port),
            f"reader@{device_ip}",
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
            f"{style_text('Connection failed', 'red')} (code {process.returncode})"
        )
    else:
        print(style_text("Successful connection", "green"))

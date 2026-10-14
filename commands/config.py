import json
from pathlib import Path
from typing import Literal

from constants import CONFIG_FILE
from utils import text


def write_to_file(homepath: str, port: str, ip: str) -> None:
    """
    Write config data to a file.
    """

    with open(CONFIG_FILE, "w") as f:
        f.write(json.dumps({"homepath": homepath, "port": port, "ip": ip}))

    print(text.style("Config saved successfully.", "green"))


def get() -> dict[Literal["homepath", "ip", "port"], str]:
    """
    Get config dictionary from a file with `homepath`, `port` and `ip` values.
    """

    cfg_path = Path(CONFIG_FILE)

    if not cfg_path.exists() or not cfg_path.read_text():
        raise Exception(
            f"{text.style('Missing config file.', 'red')} Please setup device config from the main menu."
        )

    cfg_obj = json.loads(cfg_path.read_text())

    if not cfg_obj.get("homepath") or not cfg_obj.get("ip") or not cfg_obj.get("port"):
        raise Exception(
            f"{text.style('Missing config elements.', 'red')} Please fill device config."
        )

    return cfg_obj


def get_default_values() -> tuple[
    str | Literal["/"], str | Literal[""], str | Literal[""]
]:
    """
    Get default config values.

    Reads config file and returns tuple with `homepath`, `port` and `ip` values.
    """

    homepath, ip, port = ("/", "", "")
    config_path = Path(CONFIG_FILE)

    if config_path.exists() and config_path.read_text():
        config = json.loads(config_path.read_text())
        homepath = config.get("homepath")
        ip = config.get("ip")
        port = config.get("port")

    return homepath, ip, port

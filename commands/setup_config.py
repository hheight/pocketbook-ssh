import json
from pathlib import Path

from constants import CONFIG_FILE
from utils.style_text import style_text


def setup_config(homepath, port, ip):
    with open(CONFIG_FILE, "w") as f:
        f.write(json.dumps({"homepath": homepath, "port": port, "ip": ip}))

    print(style_text("Config saved successfully!", "green"))


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


def get_default_config_values():
    homepath, ip, port = ("/", "", "")
    config_path = Path(CONFIG_FILE)

    if config_path.exists() and config_path.read_text():
        config = json.loads(config_path.read_text())
        homepath = config.get("homepath")
        ip = config.get("ip")
        port = config.get("port")

    return homepath, ip, port

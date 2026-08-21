import json
from pathlib import Path

from constants import CONFIG_FILE
from utils import text


def write_to_file(homepath, port, ip):
    with open(CONFIG_FILE, "w") as f:
        f.write(json.dumps({"homepath": homepath, "port": port, "ip": ip}))

    print(text.style("Config saved successfully!", "green"))


def get():
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


def get_default_values():
    homepath, ip, port = ("/", "", "")
    config_path = Path(CONFIG_FILE)

    if config_path.exists() and config_path.read_text():
        config = json.loads(config_path.read_text())
        homepath = config.get("homepath")
        ip = config.get("ip")
        port = config.get("port")

    return homepath, ip, port

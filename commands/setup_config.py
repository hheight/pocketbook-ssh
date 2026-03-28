import json

from utils.style_text import style_text
from constants import CONFIG_FILE

def setup_config(homepath, port, ip):
    with open(CONFIG_FILE, "w") as f:
        f.write(json.dumps({ "homepath": homepath, "port": port, "ip": ip }))

    print(style_text("Config saved successfully!", "green"))

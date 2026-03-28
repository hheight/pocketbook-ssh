import json

from style_text import style_text
from constants import CONFIG_FILE

def config_setup(homepath, port, ip):
    with open(CONFIG_FILE, "w") as f:
        f.write(json.dumps({ "homepath": homepath, "port": port, "ip": ip }))

    print(style_text("Config saved successfully!", "green"))

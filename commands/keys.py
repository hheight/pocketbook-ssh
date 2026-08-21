import subprocess
from pathlib import Path


def generate(path: Path) -> bool:
    """
    Generates SSH key pair with `ssh-keygen`.

    ECDSA key format is used.
    """

    result = subprocess.run(
        ["ssh-keygen", "-t", "ecdsa", "-f", f"{path}/ecdsa", "-N", ""],
    )
    return result.returncode == 0

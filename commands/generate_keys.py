import subprocess

def generate_keys(path):
    """
    Generates SSH key pair with `ssh-keygen`.
    ECDSA key format is used.
    """

    subprocess.run([
        "ssh-keygen",
        "-t", "ecdsa",
        "-f", f"{path}/ecdsa",
        "-N", ""
    ])

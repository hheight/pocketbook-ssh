import os
import subprocess

from prompt_toolkit.shortcuts import choice, prompt

ssh_keys_dirname = "ssh_keys"
ssh_keys_path = f"{os.path.abspath(os.getcwd())}/{ssh_keys_dirname}"

def style_text(text, style):
    match(style):
        case "red":
            return f"\033[31m{text}\033[0m"
        case "green":
            return f"\033[32m{text}\033[0m"
        case "yellow":
            return f"\033[33m{text}\033[0m"
        case "blue":
            return f"\033[34m{text}\033[0m"
        case "bold":
            return f"\033[1m{text}\033[0m"
        case _:
            return text

def main():
    main_menu_choice = choice(
        message="Please select an option:",
        options=[
            ("transfer", "Transfer files to/from your PocketBook"),
            ("generate", "Generate a new key pair"),
        ],
    )

    match(main_menu_choice):
        case "generate":
            if not os.path.isdir(ssh_keys_path):
                os.mkdir(ssh_keys_dirname);

            subprocess.run([
                "ssh-keygen",
                "-t", "ecdsa",
                "-f", f"{ssh_keys_path}/ecdsa",
                "-N", ""
            ])

            print("\n")
            print(style_text(style_text("Next steps:", "bold"), "green"))
            print(f"     1. On your device access the main koreader directory. Inside it you will find the directory `{style_text('settings/SSH', 'yellow')}`")
            print(f"     2. If a `{style_text('authorized_keys', 'yellow')}` file doesn't exist then create it. Paste the single line from your `{style_text('.pub', 'yellow')}` key pair to this file.")
            print(f"     3. Note, the `{style_text('authorized_keys', 'yellow')}` file doesn't have an extension. If you want to add other public keys to it you can add each one on a new line.")
            print("\n")

            text = prompt(f"Type 'done' once you have completed the steps: ")
            if (text == "done"):
                return




if __name__ == "__main__":
    main()

from prompt_toolkit.shortcuts import choice, prompt
from prompt_toolkit.styles import Style

from pathlib import Path

from constants import KEYS_DIRNAME
from commands.generate_keys import generate_keys
from commands.transfer_files import transfer_files
from commands.setup_config import setup_config
from utils.instructions import print_config_instructions, print_keys_instructions
from utils.style_text import style_text

prompt_style = Style.from_dict({
    "key": "ansiyellow",
})

def main():
    base_dir = Path(__file__).resolve().parent
    keys_path = base_dir / KEYS_DIRNAME

    while True:
        main_menu_choice = choice(
            message="Main menu",
            options=[
                ("transfer", "Transfer files to/from your PocketBook"),
                ("generate", "Generate a new ssh key pair"),
                ("config", "Setup device config"),
                ("exit", "Exit"),
            ],
        )

        match(main_menu_choice):
            case "generate":

                if not keys_path.exists():
                    keys_path.mkdir(parents=True, exist_ok=True)

                try:
                    generate_keys(keys_path)
                    print_keys_instructions()
                except Exception:
                    print(f"{style_text('Error:', 'red')} Failed to generate ssh keys.")

            case "transfer":
                try:
                    transfer_choice = choice(
                        message="Choose an option:",
                        options=[
                            ("download", "Download files from the device"),
                            ("upload", "Upload files to the device"),
                        ],
                    )

                    transfer_files(transfer_choice, keys_path)
                except KeyboardInterrupt:
                    print("\n")
                    print("Operation canceled.")
                except Exception as e:
                    print(e)

            case "config":
                print_config_instructions()

                try:
                    homepath = prompt([
                        ("class:key", "Home path: "),
                    ], default="/", style=prompt_style)

                    port = prompt([
                        ("class:key", "PORT: "),
                    ], style=prompt_style)

                    ip = prompt([
                        ("class:key", "IP: "),
                    ], style=prompt_style)

                    setup_config(homepath, port, ip)
                except KeyboardInterrupt:
                    print("\n")
                    print("Operation canceled.")
                except Exception as e:
                    print(e)

            case "exit":
                print(style_text("See you!", "green"))
                break

        prompt([
            ("", "Press "),
            ("class:key", "Enter"),
            ("", " to return to main menu...")
        ], style=prompt_style)


if __name__ == "__main__":
    main()

from prompt_toolkit.shortcuts import choice, prompt
from prompt_toolkit.styles import Style

from pathlib import Path

from constants import KEYS_DIRNAME
from generate_keys import generate_keys, print_next_steps
from style_text import style_text
from transfer_files import transfer_files


def main():
    base_dir = Path(__file__).resolve().parent
    keys_path = base_dir / KEYS_DIRNAME

    while True:
        main_menu_choice = choice(
            message="Please choose an option:",
            options=[
                ("transfer", "Transfer files to/from your PocketBook"),
                ("generate", "Generate a new ssh key pair"),
                ("exit", "Exit"),
            ],
        )

        match(main_menu_choice):
            case "generate":

                if not keys_path.exists():
                    keys_path.mkdir(parents=True, exist_ok=True)

                try:
                    generate_keys(keys_path)
                    print_next_steps()
                except Exception:
                    print(f"{style_text('Error:', 'red')} Failed to generate ssh keys.")

            case "transfer":
                transfer_choice = choice(
                    message="What do you want to do with file(s)?",
                    options=[
                        ("download", "Download from the device"),
                        ("upload", "Upload to the device"),
                    ],
                )

                transfer_files(transfer_choice, keys_path)
            case "exit":
                print(style_text("See you!", "yellow"))
                break

        style = Style.from_dict({
            "key": "ansiyellow",
        })

        prompt([
            ("", "Press "),
            ("class:key", "Enter"),
            ("", " to return to the main menu...")
        ], style=style)


if __name__ == "__main__":
    main()

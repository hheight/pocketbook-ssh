from pathlib import Path

from prompt_toolkit.formatted_text import HTML
from prompt_toolkit.shortcuts import choice, prompt
from prompt_toolkit.styles import Style

from commands import config, connection, files, keys
from constants import KEYS_DIRNAME
from utils import instructions, text

prompt_style = Style.from_dict(
    {
        "key": "ansiyellow",
    }
)
menu_style = Style.from_dict(
    {
        "frame.border": "ansicyan",
        "bottom-toolbar": "fg:ansiwhite bg:ansiblack noreverse",
    }
)


def main():
    base_dir = Path(__file__).resolve().parent
    keys_path = base_dir / KEYS_DIRNAME

    while True:
        try:
            main_menu_choice = choice(
                message=HTML("<b><ansiyellow>Main menu</ansiyellow></b>"),
                options=[
                    ("transfer", "Transfer files"),
                    ("connect", "Check connection"),
                    ("generate", "Generate a new SSH key pair"),
                    ("config", "Set up device config"),
                    ("exit", "Exit"),
                ],
                style=menu_style,
                show_frame=True,
            )

            print()

            match main_menu_choice:
                case "generate":
                    if not keys_path.exists():
                        keys_path.mkdir(parents=True, exist_ok=True)

                    try:
                        if keys.generate(keys_path):
                            instructions.show("keys")
                        else:
                            text.print_error(
                                "No key pair was created.",
                                red_text="SSH key generation failed:",
                            )
                    except Exception:
                        text.print_error("Failed to generate SSH keys.")

                case "transfer":
                    try:
                        transfer_choice = choice(
                            message=HTML("<b>File transfer</b>"),
                            options=[
                                ("upload", "Upload"),
                                ("download", "Download"),
                            ],
                            style=menu_style,
                            show_frame=True,
                        )

                        print()
                        files.transfer(transfer_choice, keys_path)
                    except KeyboardInterrupt:
                        print("Operation canceled.")
                    except Exception as e:
                        text.print_error(str(e))

                case "config":
                    instructions.show("config")
                    print()

                    try:
                        default_homepath, default_ip, default_port = (
                            config.get_default_values()
                        )

                        homepath = prompt(
                            [
                                ("class:key", "Home path: "),
                            ],
                            default=default_homepath,
                            style=prompt_style,
                        )

                        port = prompt(
                            [
                                ("class:key", "PORT: "),
                            ],
                            default=default_port,
                            style=prompt_style,
                        )

                        ip = prompt(
                            [
                                ("class:key", "IP: "),
                            ],
                            default=default_ip,
                            style=prompt_style,
                        )

                        config.write_to_file(homepath, port, ip)
                    except KeyboardInterrupt:
                        print("Operation canceled.")
                    except Exception as e:
                        text.print_error(str(e))

                case "connect":
                    try:
                        connection.check(keys_path)
                    except KeyboardInterrupt:
                        print("Operation canceled.")
                    except Exception as e:
                        text.print_error(str(e))

                case "exit":
                    text.print_success("See you!", blank_line=False)
                    break

            print()
            prompt(
                [
                    ("", "Press "),
                    ("class:key", "Enter"),
                    ("", " to return to main menu..."),
                ],
                style=prompt_style,
            )
            print()
        except KeyboardInterrupt:
            try:
                prompt(
                    [
                        ("", "Press "),
                        ("class:key", "Ctrl+C"),
                        ("", " again to exit..."),
                    ],
                    style=prompt_style,
                )
            except KeyboardInterrupt:
                text.print_success("See you!")
                break


if __name__ == "__main__":
    main()

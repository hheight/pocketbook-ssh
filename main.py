import os
from prompt_toolkit.shortcuts import choice, prompt
from generate_keys import generate_keys, print_next_steps
from style_text import style_text
from transfer_files import transfer_files

keys_dirname = ".keys"
keys_path = os.path.join(os.path.abspath(os.getcwd()), keys_dirname)

def main():
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

                if not os.path.isdir(keys_path):
                    os.mkdir(keys_dirname);

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
                print(style_text(style_text("See you!", "blue"), "bold"))
                break

        prompt("Press Enter to return to the main menu...")


if __name__ == "__main__":
    main()

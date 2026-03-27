from prompt_toolkit.shortcuts import choice, prompt
from generate_keys import generate_keys
from style_text import style_text
from transfer_files import transfer_files


def main():
    while True:
        main_menu_choice = choice(
            message="Please choose an option:",
            options=[
                ("transfer", "Transfer files to/from your PocketBook"),
                ("generate", "Generate a new key pair"),
                ("exit", "Exit"),
            ],
        )

        match(main_menu_choice):
            case "generate":
                generate_keys()
            case "transfer":
                transfer_files()
            case "exit":
                print(style_text(style_text("See you!", "blue"), "bold"))
                break

        prompt("Press Enter to return to menu...")


if __name__ == "__main__":
    main()

from utils import text


def show(content):
    match content:
        case "keys":
            print(text.style(text.style("Next steps:", "bold"), "green"))
            print(
                f" 1. On your device, access the main KOReader directory. Inside it you will find the directory `{text.style('settings/SSH', 'yellow')}`"
            )
            print(
                f" 2. If an `{text.style('authorized_keys', 'yellow')}` file doesn't exist, then create it. Paste the single line from your `{text.style('.pub', 'yellow')}` key pair into this file."
            )
            print(
                f" 3. Note: the `{text.style('authorized_keys', 'yellow')}` file doesn't have an extension. If you want to add other public keys to it, you can add each one on a new line."
            )
        case "config":
            print(text.style(text.style("Instructions:", "bold"), "green"))
            print(" 1. Run KOReader")
            print(" 2. Open the main menu")
            print(
                f" 3. Go to {text.style('Gear', 'yellow')} -> {text.style('Network', 'yellow')} -> {text.style('SSH server', 'yellow')}"
            )
            print(" 4. Enter the information about the device")
        case _:
            print("Unknown content")

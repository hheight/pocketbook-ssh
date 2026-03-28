from utils.style_text import style_text

def print_keys_instructions():
    print(style_text(style_text("Next steps:", "bold"), "green"))
    print(f" 1. On your device access the main koreader directory. Inside it you will find the directory `{style_text('settings/SSH', 'yellow')}`")
    print(f" 2. If a `{style_text('authorized_keys', 'yellow')}` file doesn't exist then create it. Paste the single line from your `{style_text('.pub', 'yellow')}` key pair to this file.")
    print(f" 3. Note, the `{style_text('authorized_keys', 'yellow')}` file doesn't have an extension. If you want to add other public keys to it you can add each one on a new line.")

def print_config_instructions():
    print(style_text(style_text("Instructions:", "bold"), "green"))
    print(" 1. Run KOReader")
    print(" 2. Open the main menu")
    print(f" 3. Go to {style_text('Gear', 'yellow')} -> {style_text('Network', 'yellow')} -> {style_text('SSH server', 'yellow')}")
    print(" 4. Enter the information about the device")

def style(text: str, style: str) -> str:
    """Format text with a given style"""

    match style:
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

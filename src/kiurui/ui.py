# SPDX-FileCopyrightText: 2026 Julian Malinowski
# SPDX-License-Identifier: Apache-2.0

from pathlib import Path

from src.kiurui import password_generation

# Default lengths
DEFAULT_ALPHANUMERIC_LENGTH: int = 16
DEFAULT_PASSPHRASE_LENGTH: int = 6
MIN_PASSWORD_LENGTH: int = 3

# Default file location
DEFAULT_FILE_LOCATION: Path = Path("src/kiurui/eff_large_wordlist.txt")


def menu() -> None:
    """Main menu"""
    try:
        print(
            """Menu:
            1. Generate an alphanumeric password.
            2. Generate a passphrase.
            3. Exit from the script.\n"""
        )
        menu_option = int(input("Enter the number: "))
        match menu_option:
            case 1:
                ui_alphanumeric_password()
                continue_or_exit()
            case 2:
                ui_passphrase_password()
                continue_or_exit()
            case 3:
                raise SystemExit
            case _:
                print("\nEnter a valid number.\n")
                menu()
    except ValueError:
        print("\nEnter a valid number.\n")
        menu()


def continue_or_exit() -> None:
    """Asks users if wants to continue or exit kiurui"""
    question = (
        input("\nDo you want to continue using kiurui? Y(es)/N(o): ")
        .capitalize()
        .strip()
    )
    match question:
        case "Y":
            print("\n")
            menu()
        case "N":
            raise SystemExit
        case _:
            print("Enter Y or N")
            continue_or_exit()


def ui_alphanumeric_password() -> None:
    """Menu for alphanumeric password"""
    password_length = (input("""Enter a password length (default is 16): """)).strip()
    if not password_length.isdigit():
        password_length = DEFAULT_ALPHANUMERIC_LENGTH
    else:
        password_length = int(password_length)
        if password_length < MIN_PASSWORD_LENGTH:
            password_length = DEFAULT_ALPHANUMERIC_LENGTH
    alph_pass = password_generation.alphanumeric_password(password_length)
    print(f"""Your alphanumeric password is: {alph_pass}""")


def ui_passphrase_password() -> None:
    """Menu for passphrase password"""
    # Initial values
    file_location = DEFAULT_FILE_LOCATION
    passphrase_length = DEFAULT_PASSPHRASE_LENGTH

    print("\nIf empty it will default to src/kiurui/eff_large_wordlist.txt")
    file_location = Path(input("Enter a file location for passphrase generation: "))

    # Check if file_location exists and isn't folder
    if file_location.exists() and not file_location.is_dir():
        pass
    else:
        file_location = DEFAULT_FILE_LOCATION

    try:
        passphrase_length = int(input("Enter a passphrase length (default is 6): "))
        wordlist = password_generation.passphrase_password(
            file_location, passphrase_length
        )
        print(f"Your passphrase password is: {wordlist}.")
    except ValueError:
        wordlist = password_generation.passphrase_password(
            file_location, DEFAULT_PASSPHRASE_LENGTH
        )
        print(f"Your passphrase password is: {wordlist}.")

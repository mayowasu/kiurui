# SPDX-FileCopyrightText: 2026 Julian Malinowski
# SPDX-License-Identifier: Apache-2.0

import re
import secrets
import string
from pathlib import Path


def alphanumeric_password(password_length: int) -> str:
    """Generate alphanumeric password"""
    alphabet = string.ascii_letters + string.digits
    while True:
        alph_pass = "".join(secrets.choice(alphabet) for i in range(password_length))
        if (
            any(ch.islower() for ch in alph_pass)
            and any(ch.isupper() for ch in alph_pass)
            and any(ch.isdigit() for ch in alph_pass)
        ):
            break
    return alph_pass


def passphrase_password(file_location: Path, passphrase_length: int) -> str:
    """Generate a passphrase"""
    with open(file_location, encoding="utf-8") as f:
        file_content = f.read()
        find_words = re.findall(r"[A-Za-z]+", file_content)
        return " ".join(secrets.choice(find_words) for i in range(passphrase_length))

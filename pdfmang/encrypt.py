# pdfmang/encrypt.py
from pypdf import PdfReader, PdfWriter
import os

def encrypt_pdf(input_path, output_path, password):
    """
    Encrypt a PDF file with a password.
    Requires password >= 6 chars, containing upper, lower, and number.
    """
    if not os.path.exists(input_path):
        raise FileNotFoundError(f"File not found: {input_path}")

    if not validate_password(password):
        raise ValueError(
            "Password must be at least 6 characters long and contain uppercase, lowercase, and a number."
        )

    reader = PdfReader(input_path)
    writer = PdfWriter()

    for page in reader.pages:
        writer.add_page(page)

    writer.encrypt(user_password=password, owner_password=password)

    with open(output_path, "wb") as f:
        writer.write(f)

    return output_path


def validate_password(password):
    """Check password rules."""
    if len(password) < 6:
        return False
    has_upper = any(ch.isupper() for ch in password)
    has_lower = any(ch.islower() for ch in password)
    has_digit = any(ch.isdigit() for ch in password)
    return has_upper and has_lower and has_digit

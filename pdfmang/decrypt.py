# pdfmang/decrypt.py
from pypdf import PdfReader, PdfWriter
import os

def decrypt_pdf(input_path, output_path, password):
    """Decrypt a password-protected PDF using the provided password."""
    if not os.path.exists(input_path):
        raise FileNotFoundError(f"File not found: {input_path}")

    reader = PdfReader(input_path)

    if reader.is_encrypted:
        try:
            reader.decrypt(password)
        except Exception:
            raise ValueError("Incorrect password or decryption failed.")

    writer = PdfWriter()
    for page in reader.pages:
        writer.add_page(page)

    with open(output_path, "wb") as f:
        writer.write(f)

    return output_path

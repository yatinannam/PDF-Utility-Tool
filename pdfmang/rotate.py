# pdfmang/rotate.py
from pypdf import PdfReader, PdfWriter
import os


def rotate_pdf(input_path, output_path, degree, pages=None):
    """
    Rotate selected pages or all pages in a PDF.
    :param input_path: path to input PDF
    :param output_path: path to save rotated PDF
    :param degree: rotation angle (90, 180, 270)
    :param pages: list of 1-based page numbers to rotate; if None, rotate all
    """
    if not os.path.exists(input_path):
        raise FileNotFoundError(f"File not found: {input_path}")

    reader = PdfReader(input_path)
    writer = PdfWriter()

    total_pages = len(reader.pages)
    pages_to_rotate = pages or list(range(1, total_pages + 1))

    for i, page in enumerate(reader.pages, start=1):
        if i in pages_to_rotate:
            page.rotate(degree)
        writer.add_page(page)

    with open(output_path, "wb") as out_file:
        writer.write(out_file)

    return output_path

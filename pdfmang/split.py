# pdfmang/split.py
from pypdf import PdfReader, PdfWriter
import os

def split_pdf(input_path, output_dir, start_page=None, end_page=None):
    """
    Split a PDF by page range or into separate pages.
    Pages are 1-indexed (1 = first page).
    """
    if not os.path.exists(input_path):
        raise FileNotFoundError(f"File not found: {input_path}")

    os.makedirs(output_dir, exist_ok=True)
    reader = PdfReader(input_path)

    if start_page and end_page:
        # Split a specific range
        writer = PdfWriter()
        for i in range(start_page - 1, end_page):
            writer.add_page(reader.pages[i])

        output_path = os.path.join(output_dir, f"split_{start_page}_to_{end_page}.pdf")
        with open(output_path, "wb") as out_file:
            writer.write(out_file)
        return [output_path]
    else:
        # Split every page into separate files
        output_files = []
        for i, page in enumerate(reader.pages, start=1):
            writer = PdfWriter()
            writer.add_page(page)
            output_path = os.path.join(output_dir, f"page_{i}.pdf")
            with open(output_path, "wb") as out_file:
                writer.write(out_file)
            output_files.append(output_path)
        return output_files

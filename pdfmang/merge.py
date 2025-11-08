# pdfmang/merge.py
from pypdf import PdfWriter
import os

def merge_pdfs(input_files, output_path):
    """Merge multiple PDF files into one output file."""
    if not input_files:
        raise ValueError("No input PDF files provided.")

    merger = PdfWriter()

    for file_path in input_files:
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File not found: {file_path}")
        merger.append(file_path)

    # Write the merged PDF
    with open(output_path, "wb") as out_file:
        merger.write(out_file)

    merger.close()
    return output_path

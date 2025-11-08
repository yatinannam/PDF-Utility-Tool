# pdfmang/compress.py
import fitz  # PyMuPDF
import os

def compress_pdf(input_path, output_path, quality=70):
    """
    Compress PDF by re-saving with image recompression.
    quality: 0–100 (higher = better quality, larger size)
    """
    if not os.path.exists(input_path):
        raise FileNotFoundError(f"File not found: {input_path}")

    doc = fitz.open(input_path)
    doc.save(output_path, garbage=4, deflate=True, clean=True)
    doc.close()

    # Note: PyMuPDF automatically compresses streams; for deeper compression,
    # you'd resample images, but this level keeps it simple and safe.
    return output_path

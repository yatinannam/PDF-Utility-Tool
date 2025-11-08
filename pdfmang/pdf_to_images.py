# pdfmang/pdf_to_images.py
import fitz  # PyMuPDF
import os

def pdf_to_images(input_path, output_dir, fmt="jpg"):
    """
    Convert all pages in a PDF to images.
    :param input_path: Path to input PDF file
    :param output_dir: Directory to save images
    :param fmt: 'jpg' or 'png'
    """
    if not os.path.exists(input_path):
        raise FileNotFoundError(f"File not found: {input_path}")

    os.makedirs(output_dir, exist_ok=True)
    doc = fitz.open(input_path)

    image_paths = []
    for page_num in range(len(doc)):
        page = doc.load_page(page_num)
        pix = page.get_pixmap(matrix=fitz.Matrix(2, 2))  # high quality
        image_path = os.path.join(output_dir, f"page_{page_num + 1}.{fmt}")
        pix.save(image_path)
        image_paths.append(image_path)

    doc.close()
    return image_paths

# gui/main_gui.py
import os
import sys
import tkinter as tk
from tkinter import filedialog, messagebox
import ttkbootstrap as ttk  # modern universal import
from ttkbootstrap import Style  # for applying dark theme

# --- Ensure pdfmang package is importable ---
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

from pdfmang.merge import merge_pdfs
from pdfmang.split import split_pdf
from pdfmang.rotate import rotate_pdf
from pdfmang.encrypt import encrypt_pdf
from pdfmang.decrypt import decrypt_pdf
from pdfmang.compress import compress_pdf
from pdfmang.pdf_to_images import pdf_to_images

def main():
    # Initialize themed root window
    style = Style(theme="darkly")  # <- choose any: darkly, cyborg, solar, etc.
    root = style.master
    root.iconbitmap(os.path.join(os.path.dirname(__file__), "icon.ico"))
    root.title("PDF Utility Tool")
    root.geometry("750x500")
    root.resizable(False, False)

     # --- Top Menu Bar ---
    menubar = tk.Menu(root)

    # File Menu
    file_menu = tk.Menu(menubar, tearoff=0)
    file_menu.add_command(label="Exit", command=root.quit)
    menubar.add_cascade(label="File", menu=file_menu)

    # Help Menu
    help_menu = tk.Menu(menubar, tearoff=0)

    def show_about():
        messagebox.showinfo(
            "About PDF Utility Tool",
            "PDF Utility Tool v1.0\n\nDeveloped by Yatin Annam\nCompletely free and offline tool for PDF operations."
        )

    def show_help():
        messagebox.showinfo(
            "Help",
            "This tool allows you to merge, split, rotate, compress, encrypt/decrypt, and convert PDFs to images.\n\nAll processing is done locally."
        )

    help_menu.add_command(label="Help", command=show_help)
    help_menu.add_command(label="About", command=show_about)
    menubar.add_cascade(label="Help", menu=help_menu)

    root.config(menu=menubar)


    notebook = ttk.Notebook(root)
    notebook.pack(fill="both", expand=True, padx=10, pady=10)

    # -------- Create Tabs --------
    tab_merge = ttk.Frame(notebook)
    tab_split = ttk.Frame(notebook)
    tab_rotate = ttk.Frame(notebook)
    tab_encrypt = ttk.Frame(notebook)
    tab_decrypt = ttk.Frame(notebook)
    tab_compress = ttk.Frame(notebook)
    tab_pdf_to_img = ttk.Frame(notebook)

    notebook.add(tab_merge, text="Merge")
    notebook.add(tab_split, text="Split")
    notebook.add(tab_rotate, text="Rotate")
    notebook.add(tab_encrypt, text="Encrypt")
    notebook.add(tab_decrypt, text="Decrypt")
    notebook.add(tab_compress, text="Compress")
    notebook.add(tab_pdf_to_img, text="PDF → Image")

    # ========== MERGE TAB ==========
    merge_files = []

    def select_merge_files():
        nonlocal merge_files
        merge_files = filedialog.askopenfilenames(
            title="Select PDF Files", filetypes=[("PDF files", "*.pdf")]
        )
        if merge_files:
            merge_label.config(
                text="\n".join([os.path.basename(f) for f in merge_files]),
                foreground="gray"
            )

    ttk.Button(tab_merge, text="Browse PDFs", command=select_merge_files).pack(pady=5)
    merge_label = ttk.Label(tab_merge, text="No files selected", foreground="gray")
    merge_label.pack(pady=5)

    def merge_action():
        if not merge_files:
            messagebox.showerror("Error", "Please select at least two PDF files.")
            return
        output_path = filedialog.asksaveasfilename(
            defaultextension=".pdf",
            filetypes=[("PDF files", "*.pdf")],
            title="Save merged PDF as",
        )
        if not output_path:
            return
        try:
            merge_pdfs(merge_files, output_path)
            messagebox.showinfo("Success", f"Merged PDF saved as:\n{output_path}")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    ttk.Button(tab_merge, text="Merge PDFs", command=merge_action).pack(pady=10)

    # ========== SPLIT TAB ==========
    split_file = tk.StringVar(value="No file selected")

    def select_split_file():
        file_path = filedialog.askopenfilename(
            title="Select PDF to split", filetypes=[("PDF files", "*.pdf")]
        )
        if file_path:
            split_file.set(file_path)
            split_label.config(text=os.path.basename(file_path))

    ttk.Button(tab_split, text="Browse PDF", command=select_split_file).pack(pady=5)
    split_label = ttk.Label(tab_split, textvariable=split_file, foreground="gray")
    split_label.pack(pady=5)

    ttk.Label(tab_split, text="Page Range (e.g. 1-3) or leave blank to split all:").pack(pady=5)
    range_entry = ttk.Entry(tab_split, width=15)
    range_entry.pack(pady=5)

    def split_action():
        file_path = split_file.get()
        if not os.path.exists(file_path):
            messagebox.showerror("Error", "Please select a PDF file first.")
            return
        output_path = filedialog.asksaveasfilename(
            defaultextension=".pdf",
            filetypes=[("PDF files", "*.pdf")],
            title="Save split PDF as",
        )
        if not output_path:
            return
        try:
            range_text = range_entry.get().strip()
            if range_text:
                start, end = map(int, range_text.split("-"))
                split_pdf(file_path, os.path.dirname(output_path), start, end)
            else:
                split_pdf(file_path, os.path.dirname(output_path))
            messagebox.showinfo("Success", f"Split completed!\nFiles saved near:\n{output_path}")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    ttk.Button(tab_split, text="Split PDF", command=split_action).pack(pady=10)

    # ========== ROTATE TAB ==========
    rotate_file = tk.StringVar(value="No file selected")

    def select_rotate_file():
        file_path = filedialog.askopenfilename(
            title="Select PDF to rotate", filetypes=[("PDF files", "*.pdf")]
        )
        if file_path:
            rotate_file.set(file_path)
            rotate_label.config(text=os.path.basename(file_path))

    ttk.Button(tab_rotate, text="Browse PDF", command=select_rotate_file).pack(pady=5)
    rotate_label = ttk.Label(tab_rotate, textvariable=rotate_file, foreground="gray")
    rotate_label.pack(pady=5)

    ttk.Label(tab_rotate, text="Rotation (degrees):").pack(pady=5)
    degree_var = tk.StringVar(value="90")
    ttk.Combobox(
        tab_rotate,
        textvariable=degree_var,
        values=["90", "180", "270"],
        width=10,
        state="readonly"
    ).pack(pady=5)

    ttk.Label(tab_rotate, text="Pages (e.g. 1,3,5 or leave blank for all):").pack(pady=5)
    page_entry = ttk.Entry(tab_rotate, width=20)
    page_entry.pack(pady=5)

    def rotate_action():
        file_path = rotate_file.get()
        if not os.path.exists(file_path):
            messagebox.showerror("Error", "Please select a PDF file first.")
            return
        output_path = filedialog.asksaveasfilename(
            defaultextension=".pdf",
            filetypes=[("PDF files", "*.pdf")],
            title="Save rotated PDF as",
        )
        if not output_path:
            return

        try:
            degree = int(degree_var.get())
            pages = [int(p.strip()) for p in page_entry.get().split(",")] if page_entry.get() else None
            rotate_pdf(file_path, output_path, degree, pages)
            messagebox.showinfo("Success", f"Rotated PDF saved as:\n{output_path}")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    ttk.Button(tab_rotate, text="Rotate PDF", command=rotate_action).pack(pady=10)

    # ========== ENCRYPT TAB ==========
    enc_file = tk.StringVar(value="No file selected")

    def select_encrypt_file():
        file_path = filedialog.askopenfilename(title="Select PDF", filetypes=[("PDF files", "*.pdf")])
        if file_path:
            enc_file.set(file_path)
            enc_label.config(text=os.path.basename(file_path))

    ttk.Button(tab_encrypt, text="Browse PDF", command=select_encrypt_file).pack(pady=5)
    enc_label = ttk.Label(tab_encrypt, textvariable=enc_file, foreground="gray")
    enc_label.pack(pady=5)

    ttk.Label(tab_encrypt, text="Enter Password:").pack(pady=5)
    enc_pass = ttk.Entry(tab_encrypt, show="*", width=20)
    enc_pass.pack(pady=5)

    def encrypt_action():
        file_path = enc_file.get()
        password = enc_pass.get()
        if not os.path.exists(file_path) or not password:
            messagebox.showerror("Error", "Select a file and enter password.")
            return
        output_path = filedialog.asksaveasfilename(
            defaultextension=".pdf",
            filetypes=[("PDF files", "*.pdf")],
            title="Save encrypted PDF"
        )
        if not output_path:
            return
        try:
            encrypt_pdf(file_path, output_path, password)
            messagebox.showinfo("Success", f"Encrypted PDF saved as:\n{output_path}")
            
            # Clear password and file label after success
            enc_pass.delete(0, tk.END)
            enc_file.set("No file selected")
            enc_label.config(text="No file selected", foreground="gray")

        except Exception as e:
            messagebox.showerror("Error", str(e))

    ttk.Button(tab_encrypt, text="Encrypt PDF", command=encrypt_action).pack(pady=10)

    # ========== DECRYPT TAB ==========
    dec_file = tk.StringVar(value="No file selected")

    def select_decrypt_file():
        file_path = filedialog.askopenfilename(title="Select PDF", filetypes=[("PDF files", "*.pdf")])
        if file_path:
            dec_file.set(file_path)
            dec_label.config(text=os.path.basename(file_path))

    ttk.Button(tab_decrypt, text="Browse PDF", command=select_decrypt_file).pack(pady=5)
    dec_label = ttk.Label(tab_decrypt, textvariable=dec_file, foreground="gray")
    dec_label.pack(pady=5)

    ttk.Label(tab_decrypt, text="Enter Password:").pack(pady=5)
    dec_pass = ttk.Entry(tab_decrypt, show="*", width=20)
    dec_pass.pack(pady=5)

    def decrypt_action():
        file_path = dec_file.get()
        password = dec_pass.get()
        if not os.path.exists(file_path) or not password:
            messagebox.showerror("Error", "Select a file and enter password.")
            return
        output_path = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF files", "*.pdf")], title="Save decrypted PDF")
        if not output_path:
            return
        try:
            decrypt_pdf(file_path, output_path, password)
            messagebox.showinfo("Success", f"Decrypted PDF saved as:\n{output_path}")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    ttk.Button(tab_decrypt, text="Decrypt PDF", command=decrypt_action).pack(pady=10)

    # ========== COMPRESS TAB ==========
    comp_file = tk.StringVar(value="No file selected")

    def select_comp_file():
        file_path = filedialog.askopenfilename(title="Select PDF", filetypes=[("PDF files", "*.pdf")])
        if file_path:
            comp_file.set(file_path)
            comp_label.config(text=os.path.basename(file_path))

    ttk.Button(tab_compress, text="Browse PDF", command=select_comp_file).pack(pady=5)
    comp_label = ttk.Label(tab_compress, textvariable=comp_file, foreground="gray")
    comp_label.pack(pady=5)

    ttk.Label(tab_compress, text="Compression Level:").pack(pady=5)
    comp_level = tk.StringVar(value="Medium")
    ttk.Combobox(
        tab_compress,
        textvariable=comp_level,
        values=["Low", "Medium", "High"],
        width=15,
        state="readonly"
    ).pack(pady=5)

    def compress_action():
        file_path = comp_file.get()
        if not os.path.exists(file_path):
            messagebox.showerror("Error", "Please select a PDF first.")
            return
        output_path = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF files", "*.pdf")], title="Save compressed PDF as")
        if not output_path:
            return

        quality_map = {"Low": 40, "Medium": 70, "High": 90}
        quality = quality_map.get(comp_level.get(), 70)

        try:
            compress_pdf(file_path, output_path, quality)
            messagebox.showinfo("Success", f"Compressed PDF saved as:\n{output_path}")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    ttk.Button(tab_compress, text="Compress PDF", command=compress_action).pack(pady=10)

    # ========== PDF → IMAGES TAB ==========
    pdf_img_file = tk.StringVar(value="No file selected")

    def select_pdf_img_file():
        file_path = filedialog.askopenfilename(title="Select PDF", filetypes=[("PDF files", "*.pdf")])
        if file_path:
            pdf_img_file.set(file_path)
            pdf_img_label.config(text=os.path.basename(file_path))

    ttk.Button(tab_pdf_to_img, text="Browse PDF", command=select_pdf_img_file).pack(pady=5)
    pdf_img_label = ttk.Label(tab_pdf_to_img, textvariable=pdf_img_file, foreground="gray")
    pdf_img_label.pack(pady=5)

    ttk.Label(tab_pdf_to_img, text="Select Image Format:").pack(pady=5)
    fmt_var = tk.StringVar(value="jpg")
    ttk.Combobox(
        tab_pdf_to_img,
        textvariable=fmt_var,
        values=["jpg", "png"],
        width=10,
        state="readonly"
    ).pack(pady=5)

    def convert_to_images():
        file_path = pdf_img_file.get()
        if not os.path.exists(file_path):
            messagebox.showerror("Error", "Please select a PDF first.")
            return

        # Ask for base output path (save as)
        output_base = filedialog.asksaveasfilename(
            defaultextension="",
            filetypes=[("All files", "*.*")],
            title="Choose output name (folder will be created automatically)"
        )
        if not output_base:
            return

        # Create output folder based on chosen path
        output_dir = os.path.splitext(output_base)[0] + "_pages"
        os.makedirs(output_dir, exist_ok=True)

        try:
            images = pdf_to_images(file_path, output_dir, fmt_var.get())
            messagebox.showinfo(
                "Success",
                f"Converted {len(images)} pages to images.\nSaved in folder:\n{output_dir}",
            )
        except Exception as e:
            messagebox.showerror("Error", str(e))

    ttk.Button(tab_pdf_to_img, text="Convert to Images", command=convert_to_images).pack(pady=10)


    root.mainloop()


if __name__ == "__main__":
    main()

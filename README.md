# PDF Utility Tool

PDF Utility Tool is a free, offline, and open-source desktop application designed to simplify PDF management.
Built with Python, Tkinter, and ttkbootstrap, it provides essential PDF editing and conversion features in a clean, dark-themed interface — no internet connection required.

---

## Table of Contents

1. [Introduction](#introduction)
2. [Features](#features)
3. [Tech Stack](#tech-stack)
4. [Prerequisites](#prerequisites)
5. [Project Structure](#project-structure)
6. [Setup & Usage](#setup--usage)
7. [Privacy & Security](#privacy--security)

---

## Introduction

Managing PDFs shouldn’t require paid tools or internet access.
This project offers a lightweight, secure, and beginner-friendly solution for everyday PDF operations such as merging, splitting, rotating, compressing, and protecting documents — all handled completely offline.

Whether you’re a student, professional, or developer, this tool makes working with PDFs fast, private, and simple.

---

## Features

| Category              | Description                                                            |
| --------------------- | ---------------------------------------------------------------------- |
| **Merge PDFs**        | Combine multiple PDF files into one.                                   |
| **Split PDFs**        | Extract specific pages or divide entire documents.                     |
| **Rotate Pages**      | Rotate selected pages (90°, 180°, or 270°).                            |
| **Encrypt / Decrypt** | Add or remove password protection easily.                              |
| **Compress PDFs**     | Reduce file size with adjustable quality settings (Low, Medium, High). |
| **PDF → Images**      | Convert every page into JPG or PNG images.                             |
| **Modern Interface**  | Clean dark mode design powered by ttkbootstrap.                        |
| **Offline & Secure**  | All processing is done locally — no uploads, no tracking.              |

---

## Tech Stack

-Language: Python 3.x
-GUI Framework: Tkinter + ttkbootstrap
-PDF Libraries: PyMuPDF (fitz), pypdf
-Design: Tab-based interface for clear module separation
-License: MIT License

---

## Prerequisites

Before running the tool, ensure the following are installed:
-Python 3.8+ (recommended 3.10 or above)
-pip (Python package manager)

Install the required Python packages:

```bash
pip install pypdf pymupdf ttkbootstrap
```

---

## Project Structure

```bash
PDF-Utility-Tool/
│
├── gui/
│   ├── main_gui.py
│   ├── icon.ico
│
├── pdfmang/
│   ├── __init__.py
│   ├── merge.py
│   ├── split.py
│   ├── rotate.py
│   ├── encrypt.py
│   ├── decrypt.py
│   ├── compress.py
│   ├── pdf_to_images.py
│
├── requirements.txt
└── README.md
```

---

## Setup & Usage

1. Clone the Repository

```bash
git clone https://github.com/yatinannam/PDF-Utility-Tool.git
cd PDF-Utility-Tool
```

2. Run the Application

```bash
python gui/main_gui.py
```

The app will launch in a dark-themed window with individual tabs for:
Merge, Split, Rotate, Encrypt/Decrypt, Compress, and PDF → Images.

---

## Privacy & Security

All operations are performed locally on your machine.
No data is uploaded, stored, or shared — your files remain 100% private and secure.

---

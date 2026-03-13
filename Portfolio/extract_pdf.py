import fitz  # PyMuPDF
import sys
import os

pdf_files = [
    "pdf/Dhivahar N CV.pdf",
    "pdf/Dhivahar N resume (1).pdf"
]

for pdf_path in pdf_files:
    if os.path.exists(pdf_path):
        print(f"--- Extracting text from: {pdf_path} ---")
        try:
            doc = fitz.open(pdf_path)
            for page in doc:
                text = page.get_text()
                print(text)
                print("\n")
            doc.close()
        except Exception as e:
            print(f"Error processing {pdf_path}: {e}")
    else:
        print(f"File not found: {pdf_path}")

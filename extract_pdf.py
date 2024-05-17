import fitz  # PyMuPDF !pip install --upgrade pymupdf


def extract_all_pdf_to_text(pdf_paths):
    combined_text = ""
    for pdf_path in pdf_paths:
        with fitz.open(pdf_path) as doc:
            for page in doc:
                combined_text += page.get_text() + "\n\n"
    return combined_text


combined_text = extract_all_pdf_to_text(pdf_files)
print(combined_text)

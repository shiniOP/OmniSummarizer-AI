from pathlib import Path
from docx import Document
from pypdf import PdfReader

#Extract text from a PDF file.
def extract_pdf(file) -> str:
    reader = PdfReader(file)
    text = ""
    for page in reader.pages:
        page_text = page.extract_text()
        if page_text:
            text += page_text + "\n"

    return text

#Extract text from a DOCX file.
def extract_docx(file) -> str:
    document = Document(file)
    text = ""
    for paragraph in document.paragraphs:
        text += paragraph.text + "\n"
    return text

#Extract text from a TXT file.
def extract_txt(file) -> str:
    return file.read().decode("utf-8")

#Detect the uploaded file type and extract its text.
def extract_text(uploaded_file) -> str:
    extension = Path(uploaded_file.name).suffix.lower()

    if extension == ".pdf":
        return extract_pdf(uploaded_file)

    elif extension == ".docx":
        return extract_docx(uploaded_file)

    elif extension == ".txt":
        return extract_txt(uploaded_file)

    else:
        raise ValueError(
            "Unsupported file format. Please upload a PDF, DOCX, or TXT file."
        )
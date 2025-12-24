import os
import re
import uuid
from pathlib import Path
from typing import Optional
import fitz
import docx

BASE_DIR = Path(__file__).resolve().parent
UPLOAD_DIR = BASE_DIR / "uploads"
UPLOAD_DIR.mkdir(parents=True,exist_ok=True)



# ------------------------------------------------
# Saving the document
# ------------------------------------------------

def save_uploaded_file(uploaded_file) -> Path:
    ext = Path(uploaded_file.name).suffix.lower()
    unique_name = f"{uuid.uuid4().hex}{ext}"
    file_path = UPLOAD_DIR / unique_name

    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    return file_path

# ------------------------------------------------
# Extracting text from PDF
# ------------------------------------------------

def extract_text_from_pdf(file_path: Path) -> str:
    text = []
    try:
        with fitz.open(file_path) as doc:
            for page in doc:
                page_text = page.get_text("text")
                if page_text:
                    text.append(page_text)
    
    except Exception:
        return ""
    
    return "\n".join(text)

# ------------------------------------------------
# Extracting text from DOCX
# ------------------------------------------------

def extract_text_from_docx(file_path: Path) -> str:
    try:
        document = docx.Document(file_path)
        return "\n".join(p.text for p in document.paragraphs if p.text)
    except Exception:
        return ""

# ------------------------------------------------
# Extracting text
# ------------------------------------------------

def extract_text(file_path: Path) -> str:
    suffix = file_path.suffix.lower()

    if suffix == ".pdf":
        return extract_text_from_pdf(file_path)
    
    if suffix == ".docx":
        return extract_text_from_docx(file_path)
    
    return ""

# ------------------------------------------------
# OCR DETECTION
# ------------------------------------------------

def needs_ocr(extracted_text: str, min_length: int = 200) -> bool:
    if not extracted_text:
        return True

    return len(extracted_text.strip()) < min_length



# ------------------------------------------------
# Text Cleaning
# ------------------------------------------------

def clean_text(text: str) -> str:

    if not text:
        return ""
    
    text = text.lower()
    text = re.sub(r"\s+", " ", text)
    text = re.sub(r"[^\x00-\x7F]+", " ", text)

    return text.strip()
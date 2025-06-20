import fitz  # PyMuPDF
import docx
import re

def extract_text_from_pdf(path):
    """Extract text from a PDF resume"""
    text = ""
    with fitz.open(path) as doc:
        for page in doc:
            text += page.get_text()
    return text

def extract_text_from_docx(path):
    """Extract text from a DOCX resume or job description"""
    doc = docx.Document(path)
    return "\n".join([para.text for para in doc.paragraphs])


def extract_candidate_info(text):
    info = {}

    # Name (first non-empty line that's not email or skills — a heuristic)
    lines = text.strip().split('\n')
    for line in lines:
        if line.strip() and not re.search(r'@', line) and len(line.split()) <= 5:
            info['name'] = line.strip()
            break

    # Email
    email_match = re.search(r'[\w\.-]+@[\w\.-]+', text)
    info['email'] = email_match.group(0) if email_match else None

    # Phone
    phone_match = re.search(r'\b\d{10}\b|\b\d{3}[-.\s]\d{3}[-.\s]\d{4}\b', text)
    info['phone'] = phone_match.group(0) if phone_match else None

    # Experience (look for keywords like 'Intern', 'Experience', 'years')
    exp_keywords = ['experience', 'intern', 'worked at', 'years', 'role']
    exp_lines = [line.strip() for line in lines if any(word in line.lower() for word in exp_keywords)]
    info['experience_summary'] = exp_lines[:2]  # first 2 relevant lines

    return info
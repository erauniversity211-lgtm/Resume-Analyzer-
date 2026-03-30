import PyPDF2
import docx
import spacy

nlp = spacy.load("en_core_web_sm")

def extract_text(file_path):
    text = ""

    if file_path.endswith(".pdf"):
        with open(file_path, "rb") as f:
            reader = PyPDF2.PdfReader(f)
            for page in reader.pages:
                text += page.extract_text()

    elif file_path.endswith(".docx"):
        doc = docx.Document(file_path)
        for para in doc.paragraphs:
            text += para.text

    return text


def analyze_resume(text, job_desc):
    doc1 = nlp(text.lower())
    doc2 = nlp(job_desc.lower())

    keywords_resume = set([token.text for token in doc1 if token.is_alpha])
    keywords_job = set([token.text for token in doc2 if token.is_alpha])

    match = keywords_resume.intersection(keywords_job)

    score = (len(match) / len(keywords_job)) * 100 if keywords_job else 0

    return round(score, 2), list(match)

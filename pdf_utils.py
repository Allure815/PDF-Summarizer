from pypdf import PdfReader

def extract_text_from_pdf(uploaded_pdf):
    try:
        reader = PdfReader(uploaded_pdf)
    except Exception as e:
        raise ValueError("Unable to read PDF file.") from e

    full_text = []
    for page_number, page in enumerate(reader.pages, start=1):
        try:
            text = page.extract_text()
            if text:
                full_text.append(text)
        except Exception:
            continue

    if not full_text:
        raise ValueError("No readable text found in the PDF.")

    return "\n".join(full_text)

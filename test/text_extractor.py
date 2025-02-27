import PyPDF2

def extract_text_from_pdf(pdf_path):
    text = ""
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        for page in reader.pages:
            text += page.extract_text()
    return text


if __name__ == "__main__":
    print(extract_text_from_pdf("test\\slp upadhyay (1).pdf"))
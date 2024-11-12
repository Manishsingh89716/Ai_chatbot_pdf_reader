from PyPDF2 import PdfReader
from io import BytesIO

class DocumentLoader:
    def load_pdfs(self, files: list):
        documents = []
        for file in files:
            content = file.read()
            pdf_reader = PdfReader(BytesIO(content))
            text = ""
            for page in pdf_reader.pages:
                text += page.extract_text()
            documents.append(text)
        return documents

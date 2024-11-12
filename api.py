from fastapi import FastAPI, UploadFile, File
from pydantic import BaseModel
from document_loader import DocumentLoader
from retriever import DocumentRetriever
from llm_interface import LLMInterface

app = FastAPI()

# Initialize components
pdf_loader = DocumentLoader()
retriever = DocumentRetriever()
llm_interface = LLMInterface(api_key="Your Api key")

# Upload PDFs and index them
@app.post("/upload/")
async def upload_files(files: list[UploadFile]):
    documents = await pdf_loader.load_pdfs(files)
    retriever.add_documents(documents)
    return {"message": "Files uploaded and indexed successfully"}

# Model for query endpoint
class QueryModel(BaseModel):
    question: str

# Handle queries based on uploaded PDFs
@app.post("/query/")
async def query_endpoint(query: QueryModel):
    document = retriever.retrieve(query.question)
    response = llm_interface.ask_question(query.question, document)
    return {"response": response}
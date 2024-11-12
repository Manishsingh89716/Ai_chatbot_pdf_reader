import streamlit as st
from document_loader import DocumentLoader
import openai

# Initialize document loader and set up OpenAI API key
pdf_loader = DocumentLoader()
openai.api_key = "You Api key"

def ask_question(question, documents):
    combined_text = " ".join(documents)  # Combine documents for LLM input
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": question}]
    )
    answer = response.choices[0].message.content
    return answer

# Streamlit UI
st.title("AI Chat with PDF Knowledge Base")
st.write("Upload PDF files to create a knowledge base and ask questions.")

uploaded_files = st.file_uploader("Choose PDF files", type="pdf", accept_multiple_files=True)

if uploaded_files:
    documents = pdf_loader.load_pdfs(uploaded_files)  # Synchronous call
    st.write("PDFs successfully loaded!")

    question = st.text_input("Ask a question:")
    if question:
        answer = ask_question(question, documents)
        st.write("Answer:", answer)

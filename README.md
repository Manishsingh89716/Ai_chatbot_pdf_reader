**`********* **_AI Chat with PDF Knowledge Base
* This is a small AI-powered chat application that allows users to upload multiple PDF files as a knowledge base and ask questions based on their content. The app integrates a large language model (LLM) from OpenAI to provide contextually relevant answers to user queries.
* 
* Features
* PDF Knowledge Base: Upload multiple PDFs to create a searchable knowledge base.
* Question-Answering Interface: Ask questions about the uploaded PDFs.
* Streamlit UI: Simple and interactive user interface built with Streamlit.
* Tech Stack
* Backend: Python, OpenAI API, PyPDF2
* Frontend: Streamlit
* LLM Integration: OpenAI GPT-3.5-turbo
* Requirements
* Python 3.7+
* OpenAI API key (for GPT-3.5-turbo or a compatible model)
* Streamlit
* PyPDF2 (for PDF parsing)
* Installation
* Clone the repository.
* 
* bash
* Copy code
* git clone https://github.com/manishsingh89716/AI_Chatbot.git
* cd AI_Chatbot
* Install the required Python packages.
* 
* bash
* Copy code
* pip install -r requirements.txt
* Set up your OpenAI API key by adding it directly in main.py or setting it as an environment variable.
* 
* python
* Copy code
* openai.api_key = "your_openai_api_key"
* File Structure
* main.py: Contains the Streamlit application and question-answering functionality.
* document_loader.py: Parses PDF content and loads it as plain text for the model.
* README.md: Project overview and setup instructions.
* Usage
* Run the Streamlit application.
* 
* bash
* Copy code
* streamlit run main.py
* Open your browser to the URL provided by Streamlit, typically http://localhost:8501.
* 
* Upload one or more PDF files through the interface.
* 
* Enter a question in the input field. The app will respond based on the content of the uploaded PDFs.
* 
* Example Usage
* Upload a PDF or multiple PDFs containing information on a specific topic.
* Type in a question related to the PDF content, such as "What is the main point of Chapter 3?" or "Summarize the key takeaways on page 5."
* View the AI's response directly in the app.
* Troubleshooting
* OpenAI API Errors: Make sure your API key is valid and has sufficient quota.
* Compatibility Issues: If you encounter issues with multiple OpenMP libraries, consider the workarounds suggested in the Threadpoolctl documentation.
* Dependencies
* plaintext
* Copy code
* streamlit
* openai
* PyPDF2
* Install dependencies with:
* 
* bash
* Copy code
* pip install streamlit openai PyPDF2
* License
* **This project is licensed under the MIT License.**_**********`**
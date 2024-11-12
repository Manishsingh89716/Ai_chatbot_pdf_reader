import openai

class LLMInterface:
    """Class to interface with the OpenAI Language Model."""

    def __init__(self, api_key: str):
        openai.api_key = api_key

    def ask_question(self, question: str, context: str):
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": f"Context: {context}\nQuestion: {question}"}
            ],
            max_tokens=100,
            temperature=0.5
        )
        return response.choices[0].message["content"]

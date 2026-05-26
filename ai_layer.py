import os
from openai import OpenAI
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=OPENAI_API_KEY)

def ask_ai(question: str) -> str:
    if OPENAI_API_KEY is None:
        return "No API key found"
    else:
        response = client.responses.create(
            model="gpt-4.1-mini",
            input=question
        )
        return response.output_text





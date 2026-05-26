import os
from openai import OpenAI
DEEPSEEK_API_KEY = os.getenv("DEEPSEEK_API_KEY")
client = OpenAI(api_key=DEEPSEEK_API_KEY, base_url="https://openrouter.ai/api/v1")

def ask_ai(question: str) -> str:
    if DEEPSEEK_API_KEY is None:
        return "No API key found"
    else:
        response = client.chat.completions.create(
            model="deepseek/deepseek-v4-flash",
            messages=[
                {"role": "system", "content": "You are Gandiv, a helpful Discord AI assistant. Keep answers clear, short, and beginner-friendly."},
                {"role": "user", "content": question}
            ]
        )
        return response.choices[0].message.content.strip()





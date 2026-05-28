import os
from openai import OpenAI
DEEPSEEK_API_KEY = os.getenv("DEEPSEEK_API_KEY")
client = OpenAI(api_key=DEEPSEEK_API_KEY, base_url="https://openrouter.ai/api/v1")

conversation_memory = {}

def ask_ai(user_id:str , question: str) -> str:
    if DEEPSEEK_API_KEY is None:
        return "No API key found"
    else:
        if user_id not in conversation_memory:
            conversation_memory[user_id] = []
        conversation_memory[user_id].append({"role": "user", "content": question})
        response = client.chat.completions.create(
            model="deepseek/deepseek-v4-flash",
            messages=[
                {"role": "system", "content": "You are Gandiv, a helpful Discord AI assistant. Keep answers clear, short, and beginner-friendly."}
            ]+ conversation_memory[user_id][-10:]
        )
        answer= response.choices[0].message.content.strip()
        conversation_memory[user_id].append({"role": "assistant", "content": answer})
        return answer





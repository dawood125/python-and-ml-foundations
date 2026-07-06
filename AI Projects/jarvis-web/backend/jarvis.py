from groq import Groq
from dotenv import load_dotenv
from prompt import JARVIS_SYSTEM_PROMPT
import os

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))


def get_system_prompt():
    return {
        "role": "system",
        "content": JARVIS_SYSTEM_PROMPT
    }


def chat_stream(messages: list):
  
    full_messages = [get_system_prompt()] + messages

    stream = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=full_messages,
        max_tokens=1000,
        stream=True
    )

    for chunk in stream:
        text_piece = chunk.choices[0].delta.content
        if text_piece is not None:
            yield text_piece


def manage_history(messages: list, max_messages: int = 20) -> list:

    if len(messages) > max_messages:
        return messages[-max_messages:]
    return messages
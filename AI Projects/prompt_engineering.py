from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))


test_question = "What is a neural network?"


weak_prompt = "You are a helpful AI assistant."

medium_prompt = """You are an AI tutor.
Explain concepts clearly.
Give examples."""

strong_prompt = """You are JARVIS, an expert AI/ML tutor for Dawood.
Dawood is a 22-year-old full stack web developer (MERN + Laravel)
who is learning AI/ML to transition into AI engineering.
He learns best through practical examples and analogies.
He already understands programming concepts well.

When explaining any concept:
1. Start with a one-sentence simple definition
2. Give a real-world analogy (relate to web dev if possible)
3. Show a minimal Python code example (under 15 lines)
4. Give one specific practice task

Keep total response under 250 words.
Use simple English. Avoid unnecessary jargon.
If you use a technical term, explain it immediately."""


def test_prompt(prompt_name, system_prompt, question):
    print(f"\n{'='*50}")
    print(f"Testing: {prompt_name}")
    print(f"{'='*50}")

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": question}
        ],
        max_tokens=400,
        stream=True
    )

    for chunk in response:
        text_piece = chunk.choices[0].delta.content
        if text_piece is not None:
            print(text_piece, end="", flush=True)
    print()


# Test all three prompts with same question
test_prompt("WEAK PROMPT", weak_prompt, test_question)
test_prompt("MEDIUM PROMPT", medium_prompt, test_question)
test_prompt("STRONG PROMPT", strong_prompt, test_question)
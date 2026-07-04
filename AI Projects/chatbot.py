from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

conversation_history = [
    {
        "role": "system",
        "content": """You are a helpful assistant named JARVIS.
                   You are a personal AI and Machine Learning tutor for Dawood.
                   You help him learn, practice, debug and become 
                   a professional AI engineer.
                   Keep responses clear and practical."""
    }
]

def manage_history():

    max_messages = 10

    if len(conversation_history) > max_messages + 1:

        system_prompt = conversation_history[0]

        recent_messages = conversation_history[-max_messages:]

        conversation_history.clear()
        conversation_history.append(system_prompt)
        conversation_history.extend(recent_messages)

        print("\n[JARVIS memory optimized - keeping recent context]")

def chat(user_message):
    conversation_history.append({
        "role": "user",
        "content": user_message
    })
    
    manage_history()

    try:
        stream = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=conversation_history,
            max_tokens=500,
            stream=True
        )

        full_response = ""
        print("\nJARVIS: ", end="", flush=True)

        for chunk in stream:
            text_piece = chunk.choices[0].delta.content
            if text_piece is not None:
                print(text_piece, end="", flush=True)
                full_response += text_piece

        print()

        conversation_history.append({
            "role": "assistant",
            "content": full_response
        })

        return full_response

    except Exception as error:
        error_message = f"Sorry, I encountered an error: {str(error)}"
        print(f"\nJARVIS: {error_message}")

        conversation_history.pop()

        return None


def main():
    print("=" * 40)
    print("   JARVIS - Your AI Learning Assistant")
    print("=" * 40)
    print("Type 'quit' to exit")
    print("Type 'clear' to reset conversation")
    print("=" * 40)

    while True:
        user_input = input("\nYou: ")

        if user_input.lower() == "quit":
            print("\nJARVIS: Goodbye Dawood! Keep building!")
            break

        if user_input.lower() == "clear":
            conversation_history.clear()
            conversation_history.append({
                "role": "system",
                "content": """You are a helpful assistant named JARVIS.
                           You are a personal AI tutor for Dawood."""
            })
            print("\nJARVIS: Conversation cleared. Fresh start!")
            continue

        if user_input.strip() == "":
            print("JARVIS: Say something, I am listening.")
            continue

        chat(user_input)


main()
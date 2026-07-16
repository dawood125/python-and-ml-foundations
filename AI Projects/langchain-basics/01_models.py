from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage
load_dotenv()

model = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0.7,
)

print("=== Simple Invoke ===")
response = model.invoke("What is Python in one sentence?")
print(response.content)
print()

print("=== With Messages ===")

messages = [
    SystemMessage(content="You are a Python tutor. Be brief."),
    HumanMessage(content="What is Python in one sentence?")
]
response = model.invoke(messages)
print(response.content)
print()

print("=== Conversation ===")

conversation = [
    SystemMessage(content="You are a Python tutor. Be brief."),
    HumanMessage(content="What is a function?"),
    AIMessage(content="A function is a reusable block of code."),
    HumanMessage(content="Give me an example.")
]

response = model.invoke(conversation)
print(response.content)
print()

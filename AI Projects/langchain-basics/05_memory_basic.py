from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.output_parsers import StrOutputParser
from langchain_core.chat_history import BaseChatMessageHistory
from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory
from dotenv import load_dotenv

load_dotenv()

model = ChatGroq(model="llama-3.1-8b-instant", temperature=0.7)
parser = StrOutputParser()

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are an expert programming tutor. Be concise."),
    MessagesPlaceholder(variable_name="chat_history"),
   ("human", "{input}")
]) 

chain = prompt | model | parser

store = {}

def get_session_history(session_id: str) -> BaseChatMessageHistory:
    if session_id not in store:
        store[session_id] = ChatMessageHistory()
    return store[session_id]

chain_with_memory = RunnableWithMessageHistory(
    chain,
    get_session_history,
    history_messages_key="chat_history",
    input_messages_key="input",)


config={"configurable": {"session_id": "dawood_session_1"}}
     
print("=== Session 1 with Memory ===")

print("You: Python mein list kya hoti hai?")

response1 = chain_with_memory.invoke(
    {"input": "Python mein list kya hoti hai?"},
    config=config
)
print(f"JARVIS: {response1}\n")

print("You: Iska ek example do")

response2 = chain_with_memory.invoke(
    {"input": "Iska ek example do"},
    config=config
)

print(f"JARVIS: {response2}\n")

print("You: Aur list mein elements kaise add karte hain?")
response3 = chain_with_memory.invoke(
    {"input": "Aur list mein elements kaise add karte hain?"},
    config=config
)
print(f"JARVIS: {response3}\n")

print("=== Memory Contents ===")
history = store["dawood_session_1"]
for message in history.messages:
    role = "You" if message.type == "human" else "JARVIS"
    print(f"{role}: {message.content[:80]}...")
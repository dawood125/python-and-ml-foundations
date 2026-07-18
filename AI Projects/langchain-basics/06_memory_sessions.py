from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.output_parsers import StrOutputParser
from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_core.chat_history import BaseChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory
from dotenv import load_dotenv

load_dotenv()

model = ChatGroq(model="llama-3.1-8b-instant", temperature=0.7)
parser = StrOutputParser()

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a Python tutor. "
               "Remember who you are talking to. Be concise."),
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
    input_messages_key="input"
)

dawood_config = {"configurable": {"session_id": "dawood"}}

ali_config = {"configurable": {"session_id": "ali"}}

print("=== Dawood Ki Conversation ===")

chain_with_memory.invoke(
    {"input": "Hi, I am Dawood. I want to revise all the python concepts from basic to advanced because tommorow i have interview of it."},
    config=dawood_config
)

r1 = chain_with_memory.invoke(
    {"input": "What is my name and what am I learning?"},
    config=dawood_config
)

print(f"JARVIS to Dawood: {r1}\n")


print("=== Ali Ki Conversation ===")
chain_with_memory.invoke(
    {"input": "Hi, I am Ali. I want to learn about classes."},
    config=ali_config
)
r2 = chain_with_memory.invoke(
    {"input": "What is my name and what am I learning?"},
    config=ali_config
)
print(f"JARVIS to Ali: {r2}\n") 

print("=== Proof: Sessions are Separate ===")
print(f"Dawood session messages: {len(store['dawood'].messages)}")
print(f"Ali session messages: {len(store['ali'].messages)}")
print()

print("Dawood history sample:")
print(store['dawood'].messages[0].content[:60])
print()
print("Ali history sample:")
print(store['ali'].messages[0].content[:60])
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_core.chat_history import BaseChatMessageHistory
from dotenv import load_dotenv
from langchain_core.chat_history import BaseChatMessageHistory
from langchain_core.messages import BaseMessage
from typing import List

load_dotenv()

class WindowChatHistory(BaseChatMessageHistory):
    def __init__(self, window_size: int = 6):
        self.window_size = window_size
        self._messages: List[BaseMessage] = []
    @property
    def messages(self) -> List[BaseMessage]:
        return self._messages

    def add_message(self, message: BaseMessage) -> None:
        self._messages.append(message)

        if len(self._messages) > self.window_size:
            self._messages.pop(0)

    def clear(self) -> None:
        self._messages = []


model = ChatGroq(model="llama-3.1-8b-instant", temperature=0.7)
parser = StrOutputParser()

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a Python tutor. Be very concise — one line answers."),
    MessagesPlaceholder(variable_name="chat_history"),
    ("human", "{input}")
])

chain = prompt | model | parser

store = {}

def get_windowed_history(session_id: str) -> BaseChatMessageHistory:
    if session_id not in store:
        store[session_id] = WindowChatHistory(window_size=4)
    return store[session_id]

chain_with_window = RunnableWithMessageHistory(
    chain,
    get_windowed_history,
    history_messages_key="chat_history",
    input_messages_key="input"
)

config = {"configurable": {"session_id": "window_test"}}
          
questions = [
    "What is a variable?",       
    "What is a function?",       
    "What is a list?",           
    "What is a dictionary?",     
    "What was the first thing I asked about?",  
]

print("=== Window Memory Test (window=4) ===\n")

for i, question in enumerate(questions, 1):
    response = chain_with_window.invoke(
        {"input": question},
        config=config
    )
    print(f"Turn {i} - You: {question}")
    print(f"Turn {i} - JARVIS: {response}")

    history = store["window_test"]
    print(f"[Memory size: {len(history.messages)} messages]\n")
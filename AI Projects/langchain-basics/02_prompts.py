from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv

load_dotenv()

model = ChatGroq(model="llama-3.1-8b-instant", temperature=0.7)

prompt=ChatPromptTemplate.from_messages([
    ("system", "You are an expert {subject} tutor. Be concise."),
    ("human", "Explain {topic} in simple terms with one example.")
])

filled_prompt = prompt.format(subject="Python", topic="decorators")

print("=== Filled Prompt ===")
print(filled_prompt)
print()

response=model.invoke(filled_prompt)
print("=== Model Response ===")
print(response.content)
print()

print("=== Different Topics ===")

filled_prompt_2 = prompt.format(subject="JavaScript", topic="closures")
print("=== Filled Prompt 2 ===") 
print(filled_prompt_2)
print()

response_2=model.invoke(filled_prompt_2)
print("=== Model Response 2 ===")   
print(response_2.content)
print() 
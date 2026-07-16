from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from dotenv import load_dotenv

load_dotenv()

model = ChatGroq(model="llama-3.1-8b-instant", temperature=0.7)
parser = StrOutputParser()
print("===Simple Chain===")

prompt_1=ChatPromptTemplate.from_messages([
    ("system", "You are an expert python tutor. Be concise."),  
    ("human", "Explain {concept} in 2-3 sentences.")
])

chain_1 = prompt_1 |  model | parser

result_1 = chain_1.invoke({"concept": "list comprehension"})
print(result_1)
print(type(result_1))
print()

print("=== Multiple Topics ===")

topics = ["functions", "classes", "decorators"]

for topic in topics:
    result=chain_1.invoke({"concept": topic})
    print(f"=== {topic.capitalize()} ===")
    print(result)
    

print("\n=== Chained Chains ===")

explain_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a Python tutor."),
    ("human", "Explain {concept} in one sentence.")
])

explain_chain = explain_prompt | model | parser

example_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a Python tutor."),
    ("human", "Given this explanation: {explanation}\n"
              "Write a simple code example.")
])
example_chain = example_prompt | model | parser

full_chain = (
    {"explanation": explain_chain, "concept": RunnablePassthrough()}
    | example_prompt
    | model
    | parser
)

print("Concept: Python generators")
result = full_chain.invoke({"concept": "Python generators"})
print(result)
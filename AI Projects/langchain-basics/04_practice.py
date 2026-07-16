from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

model = ChatGroq(model="llama-3.1-8b-instant", temperature=0.7)
parser = StrOutputParser()

feature_prompt = ChatPromptTemplate.from_messages([
   ("system", "You are an expert programming tutor. Be concise."),
    ("human", "List the 3 best features of {programming_language} "
    "in bullet points. Max 3 lines each.")   
])

example_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are an expert programming tutor. Be concise."),
    ("human", "Given this list of features: {features}\n"
              "Write a simple code example that demonstrates one of them.")
])

feature_chain = feature_prompt | model | parser
example_chain = example_prompt | model | parser

languages = ["Python", "JavaScript", "PHP"]

for language in languages:
    features = feature_chain.invoke({"programming_language": language})
    print(f"=== {language} Features ===")
    print(features)
    print()

    example = example_chain.invoke({"features": features})
    print(f"=== {language} Example ===")
    print(example)
    print()
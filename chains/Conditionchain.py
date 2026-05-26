from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
from langchain_core.output_parsers import PydanticOutputParser, StrOutputParser
from langchain_core.runnables import RunnableLambda

load_dotenv()

llm1 = ChatGroq(model="llama-3.1-8b-instant",temperature=0.70,max_tokens=100)

ProfessionalPrompt=ChatPromptTemplate.from_messages([
    ("system","You are a professional assistant to help you in your work"),
    ("human","{question}")
])

funnyprompt=ChatPromptTemplate.from_messages([
    ("system","You are a funny assistant to help you in your work"),    
    ("human","{question}")
])



# def pick_prompt(input:dict): #receives dict
#     if "joke" in input["question"].lower():
#         return funnyprompt.invoke(input) #invoke the prompt and pass the input dict to it
#     else:
#         return ProfessionalPrompt.invoke(input)
    
# chain=RunnableLambda(pick_prompt)|llm1|StrOutputParser()

#try with RunnableBranch ln 32 to 38
from langchain_core.runnables import RunnableBranch
branch = RunnableBranch(
    (lambda x: "joke" in x["question"].lower(),   funnyprompt),        # condition 1
    (lambda x: "simple" in x["question"].lower(), ProfessionalPrompt),       # condition 2
    RunnableLambda(lambda x: "Invalid input")  # default case
)
chain=branch|llm1|StrOutputParser() ## directly pipeable — no RunnableLambda needed as RunnableBranch is
#already built by LangChain as a runnable



user_input=input("Ask your question:")
response=chain.invoke({"question": user_input})#passing as dict
print(response) 





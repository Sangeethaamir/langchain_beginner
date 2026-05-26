from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
from langchain_core.output_parsers  import StrOutputParser



load_dotenv('.env', override=True)
llm=ChatGroq(model="llama-3.3-70b-versatile",temperature=0.7)

Prompt=ChatPromptTemplate.from_messages([
    ("system","AI expert to assist resource in learing LLMs"),
    ("human","{question}")])

chain=Prompt|llm|StrOutputParser()
user_question=input("Ask you question:")


response=chain.invoke({"question":user_question})
print(response)







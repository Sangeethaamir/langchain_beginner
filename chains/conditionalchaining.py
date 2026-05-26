import os
from pydantic import BaseModel, Field
import streamlit as st
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder, PromptTemplate
from langchain_groq import ChatGroq
from langchain_core.output_parsers import PydanticOutputParser, StrOutputParser
from langchain_core.messages import HumanMessage, AIMessage
from langchain_core.runnables import RunnableBranch, RunnableLambda
from typing import Literal
#RunnableLambda-when we want to use plain python funcation in chain directly.
# RunnableBranch-Used when you want conditional routing in LangChain. 
#Literal-restrict values to fixed options.
load_dotenv()

llm1 = ChatGroq(
    model="llama-3.1-8b-instant",temperature=0,
)

parser = StrOutputParser()
class Feedback(BaseModel):
    sentiment:Literal['positive', 'negative']=Field(description="The sentiment of the feedback")

parser2=PydanticOutputParser(pydantic_object=Feedback)
prompt1=PromptTemplate(template="classify the sentiment of the following feedback: {feedback}, {format_instructions}",
   input_variables=['feedback'], partial_variables={"format_instructions":parser2.get_format_instructions()})
prompt2=PromptTemplate(
    template="Write response to this positive feedback: {feedback}."    ,
    input_variables=["feedback"])

classify_chain=prompt2|llm1|parser2
prompt3=PromptTemplate(
    template="Write response to this negative feedback: {feedback}."    ,
    input_variables=["feedback"])

branch_chain=RunnableBranch(
    (lambda x: x.sentiment=='positive',prompt2|llm1|parser2),
    (lambda x: x.sentiment=='negative',prompt3|llm1|parser2),
    RunnableLambda(lambda x: "Invalid sentiment found")
)
chain=classify_chain|branch_chain
result=chain.invoke({"feedback":"The product is fake and is in complete damange in all parts of the phone."})
print(result)
import os
import streamlit as st
from dotenv import load_dotenv, parser
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder, PromptTemplate
from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
from langchain_core.messages import HumanMessage, AIMessage

load_dotenv()

llm = ChatGroq(
    model="llama-3.1-8b-instant",temperature=0,
)

template1=PromptTemplate(template="What is the capital of {country}?", input_variables=["country"])

template2=PromptTemplate(template="Write a short description of {topic}.", input_variables=["topic"])
parser=StrOutputParser()

chain=template1|llm|parser|template2|llm|parser
response=chain.invoke({"country":"France","topic":"Paris"})
print(response)
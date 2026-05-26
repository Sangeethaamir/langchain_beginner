import os
import streamlit as st
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder, PromptTemplate
from langchain_groq import ChatGroq
from langchain_core.output_parsers import JsonOutputParser, StrOutputParser
from langchain_core.messages import HumanMessage, AIMessage

load_dotenv()

llm = ChatGroq(
    model="llama-3.1-8b-instant",temperature=0,
)

parser = JsonOutputParser()

template1=PromptTemplate(template="Give me the Full name,age and country of a fictional person. {format_instructions}", description="The output should be in the form of a JSON object with the following keys: full_name, age, country", input_variables=[], partial_variables={"format_instructions":parser.get_format_instructions()})

chain=template1|llm|parser
response=chain.invoke({})
print(response)
import os
from pydantic import BaseModel, Field
import streamlit as st
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder, PromptTemplate
from langchain_groq import ChatGroq
from langchain_core.output_parsers import JsonOutputParser, PydanticOutputParser, StrOutputParser
from langchain_core.messages import HumanMessage, AIMessage

load_dotenv()

llm = ChatGroq(
    model="llama-3.1-8b-instant",temperature=0,
)

class Person(BaseModel):
    full_name:str=Field(description="The full name of the person")
    age:int=Field(gt=18,lt=60,description="The age of the person")
    country:str=Field(description="The country of the person")

parser = PydanticOutputParser(pydantic_object=Person)

template=PromptTemplate(template=("Give me the Full name,age and country{place} of a fictional person.Make sure the age is between 18 and 60. {format_instructions}"), description="The output should be in the form of a JSON object with the following keys: full_name, age, country", input_variables=["place"], partial_variables={"format_instructions":parser.get_format_instructions()})

#prompt=template.invoke({'place': " USA "})
                        


chain=template|llm|parser
response=chain.invoke({'place': " USA "})
print(response) 
from langchain_core.runnables import RunnableParallel
import os
from pydantic import BaseModel, Field
import streamlit as st
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder, PromptTemplate
from langchain_groq import ChatGroq


load_dotenv()

llm1=ChatGroq(model="llama-3.1-8b-instant",temperature=1.2,max_tokens=100)
llm2=ChatGroq(model="llama-3.3-70b-versatile",temperature=0.7,max_tokens=100)

Prompt1=PromptTemplate(template="write simple notes on {topic}",
input_variables=["topic"])

Prompt2=PromptTemplate(template="generate 5 quotes  on {word}",
input_variables=["word"])

Prompt3=PromptTemplate(template="merge the quotes and  simple notes on {notes},{quotes}",
input_variables=["notes","quotes"])
parser=StrOutputParser()

runnable_chain=RunnableParallel({
    'notes': Prompt1 | llm1 | parser,
    'quotes': Prompt2 | llm2 | parser})
merged_chain=Prompt3 | llm1 | parser
final_chain=runnable_chain | merged_chain
text="""
The Taj Mahal is a magnificent white marble mausoleum located in Agra, India, built by Mughal emperor Shah Jahan in memory of his beloved wife Mumtaz Mahal. It was constructed between 1632 and 1653, taking over 20 years and 20,000 workers to complete. The monument is considered one of the greatest examples of Mughal architecture, blending Persian, Islamic, and Indian styles beautifully. It was designated a UNESCO World Heritage Site in 1983 and is recognized as one of the Seven Wonders of the World. Every year, millions of visitors from around the globe visit the Taj Mahal, making it India's most iconic and treasured landmark.
"""
response=final_chain.invoke({"topic": "Taj Mahal", "word": "Taj Mahal"})
print(response)




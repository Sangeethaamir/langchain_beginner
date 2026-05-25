from langchain_core.prompts import ChatPromptTemplate, PromptTemplate,FewShotChatMessagePromptTemplate
from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os

load_dotenv('.env', override=True)

#example for the shots
examples=[
    {"input":"cotton shirt", "output":"summer wear"},
    {"input":"woolen sweater", "output":"winter wear"},
    {"input":"denim jacket", "output":"winter wear"},
    {"input":"linen pants", "output":"summer wear"},
    {"input":"cotton saree", "output":"summer    wear"},  
]
#format for the examples
example_prompt=ChatPromptTemplate.from_messages([
    ("human", "{input}"),
    ("ai", "{output}"),
])

userfewshotprompt=FewShotChatMessagePromptTemplate(
    examples=examples,
    example_prompt=example_prompt,
)

prompt=ChatPromptTemplate.from_messages([
    ("system","you are a fashion expert who can classify the cloths into summer wear and winter wear"),
    userfewshotprompt,             
    ("human","{question}"),
    
    userfewshotprompt,
])

llm=ChatGroq(model="llama-3.3-70b-versatile",temperature=0.7,max_tokens=100)
chain=prompt|llm

response=chain.invoke({"question":"Its too sunny outside, I need to wear something light. What should I wear?"})
print(response.content)



import os
from dotenv import load_dotenv
from langchain_core.messages import AIMessage,HumanMessage
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq
load_dotenv()
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_PROJECT"] = "smith validation" 

os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGSMITH_API_KEY")
api_key=os.getenv("GROQ_API_KEY")
llm=ChatGroq(model="llama-3.3-70b-versatile",temperature=0.7,max_tokens=70)
prompt= ChatPromptTemplate.from_messages([("system","you are a news reporter"),
                                           ("user","{input}")])
chain= prompt|llm|StrOutputParser()
output=chain.invoke({"input":"when it will be raining next"})
print(output)
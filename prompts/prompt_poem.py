from  langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv('.env',override=True)
llm=ChatGroq(model="llama-3.3-70b-versatile")
print("Poem Generator")
prompt=ChatPromptTemplate.from_messages([
    ("system", "you are a creative poet writting peoms in simple lines"),
     ("human","write a poem on the topic of {topic}")
])
print("Enter the poem topic or exit")

chat_history=[]
while True:
    user_input=input("Enter the topic to write the poem:") 

    if user_input.lower()=='exit':
        print("thanks we are exiting")
        break



user_prompt=(prompt.format_messages(topic=user_input));

for msg in chat_history:
    user_prompt.append(msg)

response=llm.invoke(user_prompt)
print(user_prompt)
print(response.content)
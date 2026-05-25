from langchain_core.prompts import ChatPromptTemplate,SystemMessagePromptTemplate,HumanMessagePromptTemplate
from langchain_groq import ChatGroq
from dotenv import load_dotenv


load_dotenv('.env', override=True)
llm=ChatGroq(model="llama-3.3-70b-versatile",temperature=0.7)
print("Travel Blog Post Generator")
print("provide an idea or topic for the travel blog post. Fell free to type exit to finish the program")

user_input=input("Enter the topic: ")
prompt=ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template("You are a travel blog post generator. " \
    "You will generate a travel blog post based on the topic provided by the user. " \
    "The blog post should be engaging, informative and should include tips and recommendations for travelers."),
    HumanMessagePromptTemplate.from_template("Generate a travel blog post about {topic}")
])

# Initiate the chat history

chat_history=[]

while True:
    user_input=input("Any Insructions:")

    if user_input.lower() == "exit":
        print("Exiting the program. Goodbye!")
        break

    #prompt

    message=prompt.format_messages(topic=user_input)

    for prev in chat_history:
        message.append(prev)
    
    message.append(HumanMessagePromptTemplate.from_template(user_input).format_messages(user_input=user_input)[0])
    response=llm.invoke(message)
    print("Generated Travel Blog Post:",response.content)
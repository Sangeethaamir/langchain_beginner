from langchain_core.prompts import ChatPromptTemplate,StringPromptTemplate,HumanMessagePromptTemplate, SystemMessagePromptTemplate,AIMessagePromptTemplate

# chat_prompt=ChatPromptTemplate.from_messages([
#     SystemMessagePromptTemplate.from_template("You are a helpful assistant that provides information about {topic}."),
#     HumanMessagePromptTemplate.from_template("What is {topic}?")      
# ])
# #prompt=chat_prompt.format(topic="LLM")
# prompt=chat_prompt.format_messages(topic="LLM")#Used when working with chat-based prompts
# print(prompt)


user=ChatPromptTemplate.from_messages(
    [
        SystemMessagePromptTemplate.from_template("you are a fashion expert who worked in {company}"),
        HumanMessagePromptTemplate.from_template("What is that you wanted to know about {company} fashion trends?"),
        AIMessagePromptTemplate.from_template ("you are responsible for the holding the conversation memory"),
    ]
)
response=user.format(company="Zara")
print(response)
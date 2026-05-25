from langchain_core.prompts import PromptTemplate

# dynamic_prompt=PromptTemplate(
#     template="write a fun fact about {topic} in a {style} style",
#         input_variables=["topic", "style"] #dynamic variable for customization
#     )
# #any number of prompt we can declare using the temaplte
# prompt_text1=dynamic_prompt.format(topic="tomatoes", style="humorous") #we use format() to replace placeholders (variables) inside the prompt template with actual values.
# print(prompt_text1)
# prompt_text2=dynamic_prompt.format(topic="egg", style="innovative")
# print(prompt_text2)


user1=PromptTemplate(
    template="what are all the different cloths a women can try for {festival}",
    input_variables=["festival"]
    )
response1=user1.format(festival="new year")
print(response1)
response2=user1.format(festival="Christmas Eve")
print(response2)

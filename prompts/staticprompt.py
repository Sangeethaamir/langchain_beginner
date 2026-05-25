
# from langchain_core.prompts import PromptTemplate

# static_prompt=PromptTemplate(
#     input_variables=[], #No input variables for a static prompt
#     template="write a fun fact about LLM?"
# )

# prompt_text=static_prompt.format() #no input variables to format to pass
# print(prompt_text) 

from langchain_core.prompts import PromptTemplate



user1=PromptTemplate(
    template="What is the adverse effect of using the desisel engine?"
)

user2=PromptTemplate.from_template("what do you thing of getting expenbsive products")

response1=user1.format()
print(response1)
response2=user2.format()
print(response2)

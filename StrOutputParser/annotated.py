from langchain_core.prompts import ChatPromptTemplate,SystemMessagePromptTemplate,HumanMessagePromptTemplate
from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from typing import TypedDict, Annotated,Optional


load_dotenv('.env', override=True)
llm=ChatGroq(model="llama-3.3-70b-versatile",temperature=0.7)

#schema

class review(TypedDict):
    key_points:Annotated[list[str], "must write the key points of the review discueesed her"]
    title: Annotated[str, " write the title of the movie being reviewed"]
    rating: Annotated[int, " write the rating of the movie on a scale of 1 to 5"]
    review: Annotated[str, " write the review of the movie in maximun of 200 words"]
    summary: Annotated[str, " Just one line summary of the movie review"]
    sentiment: Annotated[str, " Either positive, negative or neutral"]
    Awards: Annotated[Optional[list[str]], " write the awards won by the movie if any, if not write None"]

prompt="""
You are a movie review analyzer. You will be given a movie review and you need to analyze it and 
provide the following information in the form of a JSON object with the following keys:
- title: The title of the movie being reviewed {topic}
- rating: The rating of the movie
- review: The review of the movie
- summary: A summary of the movie review
- sentiment: The sentiment of the movie review
"""

user_input=input("enter movie name:")
user_prompt=(prompt.format(topic=user_input))


structured_llm_response=llm.with_structured_output(review)
reponse=structured_llm_response.invoke(user_prompt)
print(reponse)
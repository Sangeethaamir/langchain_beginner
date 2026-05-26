from langchain_core.prompts import ChatPromptTemplate,SystemMessagePromptTemplate,HumanMessagePromptTemplate
from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from typing import TypedDict, Annotated,Optional,Literal
from pydantic import BaseModel, Field


load_dotenv('.env', override=True)
llm=ChatGroq(model="llama-3.3-70b-versatile",temperature=0.7)

#schema

class review(BaseModel):
    key_points: list[str] = Field(description="must write the key points of the review discussed here")
    title: str = Field(description="write the title of the movie being reviewed")
    rating: int = Field(description="write the rating of the movie on a scale of 1 to 5")
    review: str = Field(description="write the review of the movie in maximum of 200 words")
    summary: str = Field(description="just one line summary of the movie review")
    sentiment: str = Field(description="either positive, negative or neutral")
    Awards: Optional[list[str]] = Field(default=None,description="write the awards won by the movie if any")

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
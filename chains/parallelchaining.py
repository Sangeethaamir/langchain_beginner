from langchain_core.runnables import RunnableParallel
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()

llm    = ChatGroq(model="llama-3.1-8b-instant", temperature=0.7)
parser = StrOutputParser()

# Prompt 1 and 2 — run in parallel
notes_prompt  = PromptTemplate.from_template("Write 3 simple notes on {topic}")
quotes_prompt = PromptTemplate.from_template("Write 2 quotes on {topic}")

# Prompt 3 — combines output of 1 and 2
merge_prompt = PromptTemplate.from_template(
    "Combine the notes and quotes into a short paragraph:\nNotes: {notes}\nQuotes: {quotes}"
)

# Step 1 — parallel chain
parallel_chain = RunnableParallel({
    "notes":  notes_prompt  | llm | parser,
    "quotes": quotes_prompt | llm | parser,
})

# Step 2 — merge chain
merge_chain = merge_prompt | llm | parser

# Step 3 — connect both
final_chain = parallel_chain | merge_chain

# Run
response = final_chain.invoke({"topic": "Taj Mahal"})
print(response)
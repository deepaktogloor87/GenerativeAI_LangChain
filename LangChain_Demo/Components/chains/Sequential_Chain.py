from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

# HuggingFace endpoint LLM
llm = HuggingFaceEndpoint(
    repo_id='meta-llama/Llama-3.1-8B-Instruct',
    task='text-generation'
)

# Chat model wrapper
model = ChatHuggingFace(llm=llm)

# Prompt
prompt1 = ChatPromptTemplate.from_template("Generate summary of the {topic}")
prompt2 = ChatPromptTemplate.from_template("Generate 5 intresting text \n {text}")


# Output parser
parser = StrOutputParser()

# Chain using pipe syntax (works in langchain_core)
chain = prompt1 | model | parser | prompt2 | model | parser

# Run chain
result = chain.invoke({'topic': 'Grasshopper'})
print(result)

chain.get_graph().print_ascii()
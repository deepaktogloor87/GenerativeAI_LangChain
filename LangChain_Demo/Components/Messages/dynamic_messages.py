from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import HumanMessage, SystemMessage
from dotenv import load_dotenv
load_dotenv()

llm = HuggingFaceEndpoint(repo_id='meta-llama/Llama-3.2-1B-Instruct', 
                    task='text-generation')

model = ChatHuggingFace(llm=llm)

chat_template = ChatPromptTemplate([
    ('system', "You are a helpful assistant that provides information about {domain}"),
    ('human', "Can you tell me more about {topic} in the field of {domain}?")
])

prompt = chat_template.invoke({"domain": "technology", "topic": "blockchain"})

print(prompt)
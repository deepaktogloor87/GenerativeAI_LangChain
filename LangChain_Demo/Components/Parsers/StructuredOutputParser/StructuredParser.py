from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from langchain_core.prompts import PromptTemplate
from langchain.


from dotenv import load_dotenv
load_dotenv()

llm = HuggingFaceEndpoint(repo_id='meta-llama/Llama-3.1-8B-Instruct')

model = ChatHuggingFace(llm=llm)

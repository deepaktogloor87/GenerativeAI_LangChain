from langchain_community.llms import HuggingFaceHub
from dotenv import load_dotenv
import os

load_dotenv()

llm = HuggingFaceHub(
    repo_id="meta-llama/Llama-3.2-1B-Instruct",
    task="text-generation",
    model_kwargs={"temperature": 0.9, "max_length": 512},
    huggingfacehub_api_token=os.getenv("HUGGINGFACEHUB_API_TOKEN"))

result = llm.invoke("Explain LangChain simply")
print(result)
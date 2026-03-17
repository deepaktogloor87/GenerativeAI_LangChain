from langchain_huggingface import HuggingFacePipeline, ChatHuggingFace
from dotenv import load_dotenv
import os
load_dotenv()

os.environ["HF_HOME"] = "D:/huggingface_cache"

llm = HuggingFacePipeline.from_model_id(
    model_id="TinyLlama/TinyLlama-1.1B-intermediate-step-1431k-3T",
    task="text-generation")

model = ChatHuggingFace(llm=llm)
response = model.invoke("Who is the present of India?")
print(response.content)
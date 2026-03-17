from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from dotenv import load_dotenv

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.2-1B-Instruct",
    task="text-generation",
    model_kwargs={"temperature": 0.9, "max_length": 512},
)

model = ChatHuggingFace(llm=llm)
response = model.invoke("What is the capital of France?")
print(response)
from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from dotenv import load_dotenv
load_dotenv()

llm = HuggingFaceEndpoint(repo_id='meta-llama/Llama-3.2-1B-Instruct', 
                    task='text-generation')

model = ChatHuggingFace(llm=llm)

while True:
    user_input = input("Enter your query (or 'exit' to quit): ")
    if user_input.lower() == 'exit':
        break
    response = model.invoke(user_input)
    print("Response:", response.content)
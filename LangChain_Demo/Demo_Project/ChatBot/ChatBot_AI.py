from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from dotenv import load_dotenv

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id='meta-llama/Llama-3.2-1B-Instruct')
model = ChatHuggingFace(llm=llm)

chat_history = []

while True:
    usr_input = input("You: ")
    chat_history.append(usr_input)
    if usr_input.lower() in ['exit', 'quit']:
        print("Exiting the chat. Goodbye!")
        break
    result = model.invoke(chat_history)
    chat_history.append(result.content)
    print(f"AI: {result.content}")

print(chat_history)


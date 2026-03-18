from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from dotenv import load_dotenv
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id='meta-llama/Llama-3.2-1B-Instruct')
model = ChatHuggingFace(llm=llm)

chat_history = [
    SystemMessage(content="You are a helpful assistant."),
]

while True:
    usr_input = input("You: ")
    chat_history.append(HumanMessage(content=usr_input))
    if usr_input.lower() in ['exit', 'quit']:
        print("Exiting the chat. Goodbye!")
        break
    result = model.invoke(chat_history)
    chat_history.append(AIMessage(content=result.content))
    print(f"AI: {result.content}")

print(chat_history)


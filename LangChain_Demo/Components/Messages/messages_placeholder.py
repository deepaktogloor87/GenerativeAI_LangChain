from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

from dotenv import load_dotenv
load_dotenv()

llm = HuggingFaceEndpoint(repo_id='meta-llama/Llama-3.2-1B-Instruct', 
                    task='text-generation')

model = ChatHuggingFace(llm=llm)

# chat template
chat_template = ChatPromptTemplate([
    ('system', "You are a helpful customer support agent assistant."),
    MessagesPlaceholder(variable_name="chat_history"),
    ('human', "{query}]")
])

chat_history = []
# load chat history
with open('LangChain_Demo\\Components\\Messages\\chat_history.txt', 'r', encoding='utf-8') as f:
    chat_history.extend(f.readlines())

# create prompt
prompt = chat_template.invoke({
    'chat_history': chat_history,
    'query': 'where is my refund?'})

print(prompt)
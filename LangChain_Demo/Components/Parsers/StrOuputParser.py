from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from langchain_core.prompts import PromptTemplate

from dotenv import load_dotenv
load_dotenv()

llm = HuggingFaceEndpoint(repo_id='meta-llama/Llama-3.3-70B-Instruct')

model = ChatHuggingFace(llm=llm)

template1 = PromptTemplate(
    template = "You are a helpful assistant that extracts the main {topic} from a given text.",
    inputs_variables = ["topic"])

template2 = PromptTemplate(
    template = "Write a concise summary of the following text \n {text}",
    input_variables = ["text"])

prompt1 = template1.invoke({'topic': "LangGraph"})
result = model.invoke(prompt1)
prompt2 = template2.invoke({'text': result.content})
final_result = model.invoke(prompt2)
print(final_result.content)
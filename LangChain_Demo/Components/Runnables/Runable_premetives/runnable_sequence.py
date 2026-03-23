from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain_core.runnables import RunnableSequence

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id='dphn/Dolphin-Mistral-24B-Venice-Edition')



# define a prompt
prompt = PromptTemplate.from_template('Write a joke on the {topic}')

model = ChatHuggingFace(llm=llm)
parser = StrOutputParser()

expand_prompt = PromptTemplate.from_template('Explain bit more about {text}')

chain = RunnableSequence(prompt, model, parser, expand_prompt, model, parser)
result = chain.invoke({'topic':'AI'})
print(result)


from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain_core.runnables import RunnableSequence, RunnablePassthrough, RunnableParallel, RunnableLambda
from langchain_community.document_loaders import TextLoader
load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id='dphn/Dolphin-Mistral-24B-Venice-Edition',
    task='text-generation')

model = ChatHuggingFace(llm=llm)
parser = StrOutputParser()

loader = TextLoader('LangChain_Demo/RAG_Components/advik.txt',encoding='utf-8')
docs = loader.load()

prompt = PromptTemplate.from_template('Write a summary for the following poem\n {poem}')

chain = prompt | model | parser
result = chain.invoke({'poem':docs[0].page_content})
print(result)
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain_core.runnables import RunnableSequence, RunnablePassthrough, RunnableParallel, RunnableLambda
from langchain_community.document_loaders import PyPDFLoader
load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id='dphn/Dolphin-Mistral-24B-Venice-Edition',
    task='text-generation')

model = ChatHuggingFace(llm=llm)
parser = StrOutputParser()

loader = PyPDFLoader('LangChain_Demo/RAG_Components/Job_Description.pdf')
docs = loader.load()
print(docs[0].page_content)
print(docs[1].metadata)
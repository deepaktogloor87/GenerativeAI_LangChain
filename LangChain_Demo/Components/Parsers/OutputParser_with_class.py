from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

from dotenv import load_dotenv
load_dotenv()

llm = HuggingFaceEndpoint(repo_id='zai-org/GLM-5')

model = ChatHuggingFace(llm=llm)

template1 = PromptTemplate(
    template = "You are a helpful assistant that extracts the main {topic} from a given text.",
    input_variables = ["topic"])

template2 = PromptTemplate(
    template = "Write a 5 lines summary of the following text in bullet style \n {text}",
    input_variables = ["text"])

parser = StrOutputParser()
chain = (template1 
         | model 
         | parser 
         | template2 
         | model 
         | parser
         )

result = chain.invoke({'topic': "Black Hole"})
print(result.content)
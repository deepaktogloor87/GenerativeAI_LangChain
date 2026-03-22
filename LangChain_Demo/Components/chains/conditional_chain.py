from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableParallel, RunnableBranch, RunnableLambda
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from typing import Literal

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="mistralai/Mistral-7B-Instruct-v0.2"
)
model = ChatHuggingFace(llm=llm)
parser = StrOutputParser()

class Feedback(BaseModel):
    sentiment : Literal['positive','negative'] = Field(description='Give me the sentiment feedback')

parser2 = PydanticOutputParser(pydantic_object=Feedback)

prompt1 = PromptTemplate.from_template(
    template = 'Clasify the sentiment of the following feedback text into positive or negative \n {feedback}' \
    '{format_instruction}',
    partial_variables={'format_instruction':parser2.get_format_instructions()})

classifier_chain = prompt1 | model | parser2

positive_prompt = PromptTemplate.from_template(
    template = 'Write an appropriate response to this positive feedback \n {feedback}'
)

negative_prompt = PromptTemplate.from_template(
    template = 'Write an appropriate response to this negative feedback \n {feedback}'
)

branch_chain = RunnableBranch(
    (lambda x: x.sentiment == 'positive', positive_prompt | model | parser),
    (lambda x:x.sentiment == 'negative', positive_prompt | model | parser),
    RunnableLambda(lambda x: 'could not found sentiment')
)

chain = classifier_chain | branch_chain

result = chain.invoke({'feedback':'This is wonderful phone'})
print(result)
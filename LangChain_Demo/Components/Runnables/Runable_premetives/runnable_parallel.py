from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_anthropic import ChatAnthropic
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain_core.runnables import RunnableSequence, RunnableParallel 

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id='dphn/Dolphin-Mistral-24B-Venice-Edition')

HF_model = ChatHuggingFace(llm=llm)
AN_model = ChatAnthropic(model_name='Claude-3.5-25052024')
parser = StrOutputParser()

Link_prompt = PromptTemplate.from_template('Generate a linkedIn post on the topic {topic}')
X_prompt = PromptTemplate.from_template('Generate a x account post on the topic {topic}')


chain = RunnableParallel({
    'linkedin' : RunnableSequence(Link_prompt, HF_model, parser),
    'tweet' : RunnableSequence(X_prompt,AN_model, parser)})

result = chain.invoke({'topic':'Achievement on certification of AI course'})
print(result)



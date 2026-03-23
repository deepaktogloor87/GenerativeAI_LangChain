from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain_core.runnables import RunnableSequence, RunnablePassthrough, RunnableParallel

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id='dphn/Dolphin-Mistral-24B-Venice-Edition',
    task='text-generation')

model = ChatHuggingFace(llm=llm)
parser = StrOutputParser()

joke_prompt = PromptTemplate.from_template("Generate a joke on user provided {topic}")
joke_xpl_prompt = PromptTemplate.from_template("Generate a detailed explination about the {text}")

joke_gen_chain = RunnableSequence(joke_prompt, model, parser)
parallen_chain = RunnableParallel({
    'joke': RunnablePassthrough(),
    'explaination' : RunnableSequence(joke_xpl_prompt, model, parser)
})

com_chain = RunnableSequence(joke_gen_chain, parallen_chain)
result = com_chain.invoke({"topic":"cricket"})
print(result)
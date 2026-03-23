from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain_core.runnables import RunnableSequence, RunnablePassthrough, RunnableParallel, RunnableLambda

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id='dphn/Dolphin-Mistral-24B-Venice-Edition',
    task='text-generation')

model = ChatHuggingFace(llm=llm)
parser = StrOutputParser()

def word_count(text):
    return len(text.split())

prompt = PromptTemplate.from_template("Generate a joke about the given {topic}")

joke_gen_chain = RunnableSequence(prompt, model, parser)

parallel_chain = RunnableParallel({
    'joke':RunnablePassthrough(),
    'word_count' : RunnableLambda(word_count)
})

final_chain = RunnableSequence(joke_gen_chain, parallel_chain)
result = final_chain.invoke({'topic':'AI'})
print(result)
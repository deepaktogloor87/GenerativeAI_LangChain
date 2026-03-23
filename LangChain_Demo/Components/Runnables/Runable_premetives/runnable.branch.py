from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain_core.runnables import RunnableSequence, RunnablePassthrough, RunnableParallel, RunnableLambda, RunnableBranch

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id='dphn/Dolphin-Mistral-24B-Venice-Edition',
    task='text-generation')

model = ChatHuggingFace(llm=llm)
parser = StrOutputParser()

prompt1 = PromptTemplate.from_template("Write a detailed report on {topic}")
prompt2 = PromptTemplate.from_template("Summarize the following text:\n{text}")

report_gen_chain = RunnableSequence(prompt1, model, parser)

def is_long(text):
    return len(text.split()) > 500

summary_chain = RunnableSequence(
    RunnableLambda(lambda x: {"text": x}),  # FIX: wrap input properly
    prompt2,
    model,
    parser
)

branch_chain = RunnableBranch(
    (is_long, summary_chain),
    RunnablePassthrough()
)

# ✅ Use branch here
final_chain = RunnableSequence(report_gen_chain, branch_chain)

result = final_chain.invoke({'topic': 'Russian Girls'})
print(result)
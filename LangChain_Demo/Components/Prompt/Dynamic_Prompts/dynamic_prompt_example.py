from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
load_dotenv()

llm = HuggingFaceEndpoint(repo_id='meta-llama/Llama-3.2-1B-Instruct', 
                    task='text-generation')

model = ChatHuggingFace(llm=llm)

#template
template = PromptTemplate(
    template="""
    Create a {WORD_COUNT}-word blog post on {TOPIC}, focusing on {INTEREST}. Use an engaging introduction, clear subheadings, actionable tips, real-life examples, and a strong conclusion. Optimize for readability and include a conversational tone suitable for {TARGET_AUDIENCE}.
    """,
    input_variables=["WORD_COUNT", "TOPIC", "INTEREST", "TARGET_AUDIENCE"],
    validate_template=True
)

#placeholder values
prompt = template.invoke({
    "WORD_COUNT": int(input("Enter the desired word count: ")),
    "TOPIC": str(input("Enter the blog post topic: ")),
    "INTEREST": str(input("Enter the specific interest to focus on: ")),
    "TARGET_AUDIENCE": str(input("Enter the target audience: "))
})

while True:
    response = model.invoke(prompt)
    print("\nGenerated Blog Post:\n")
    print(response.content)

    cont = input("\nDo you want to generate another blog post? (yes/no): ")
    if cont.lower() != 'yes':
        break

    prompt = template.invoke({
        "WORD_COUNT": int(input("Enter the desired word count: ")),
        "TOPIC": str(input("Enter the blog post topic: ")),
        "INTEREST": str(input("Enter the specific interest to focus on: ")),
        "TARGET_AUDIENCE": str(input("Enter the target audience: "))
    })
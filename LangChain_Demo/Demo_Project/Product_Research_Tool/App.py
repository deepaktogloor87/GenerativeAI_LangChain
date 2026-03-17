from langchain_core.prompts import load_prompt
from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from dotenv import load_dotenv

load_dotenv()

# Initialize model
llm = HuggingFaceEndpoint(
    repo_id='meta-llama/Llama-3.2-1B-Instruct',
    task='text-generation'
)

model = ChatHuggingFace(llm=llm)

# Load prompt template
template = load_prompt("./product_research_template.json")

while True:
    print("\n--- Enter Product Research Details ---\n")

    prompt = template.invoke({
        "WEBSITE_DOMAIN": input("Website domain (e.g., amazon.com): "),
        "CATEGORY": input("Category (e.g., electronics): "),
        "PRODUCT_LINK": input("Product link: "),
        "PRODUCT_PRICE": float(input("Product price: ")),
        "RATING": float(input("Rating (e.g., 4.3): ")),
        "REVIEWS": int(input("Number of reviews: ")),
        "HIGH_MARGIN": input("High margin? (yes/no): "),
        
        # New variables
        "MIN_PRICE": float(input("Min price filter: ")),
        "MAX_PRICE": float(input("Max price filter: ")),
        "TREND": input("Trend (rising/stable/declining): "),
        "COMPETITION": input("Competition (low/medium/high): ")
    })

    # Invoke model AFTER prompt is created
    response = model.invoke(prompt)

    print("\n--- Product Analysis ---\n")
    print(response.content)

    cont = input("\nDo you want to continue research? (yes/no): ")
    if cont.lower() != 'yes':
        break
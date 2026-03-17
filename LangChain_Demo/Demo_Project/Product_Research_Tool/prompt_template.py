from langchain_core.prompts import PromptTemplate

template = PromptTemplate(
    template="""
    "Analyze the product from {WEBSITE_DOMAIN} in the {CATEGORY} category using the following details:
    Product Link: {PRODUCT_LINK}  
    Price: {PRODUCT_PRICE}  
    Rating: {RATING}  
    Number of Reviews: {REVIEWS}  
    High Margin Indicator: {HIGH_MARGIN}  

    Based on these inputs, evaluate:

    1. Whether this product is a high-potential affiliate product  
    2. Demand strength (based on reviews & rating)  
    3. Profitability potential (based on price & margin)  
    4. Competition level  
    5. Trustworthiness of the product  

    Then provide:
    - A clear verdict: (High / Medium / Low potential)  
    - Reasons for the verdict  
    - Suggestions to improve conversions (content angles, audience targeting, platforms)"
    """,
    input_variables=["WEBSITE_DOMAIN", "CATEGORY", "PRODUCT_LINK", "PRODUCT_PRICE", "RATING", "REVIEWS", "HIGH_MARGIN"],
    validate_template=True
)

template.save("product_research_template.json")
from langchain_huggingface import HuggingFaceEmbeddings
from dotenv import load_dotenv

load_dotenv()

embeddings = HuggingFaceEmbeddings(
    model_name="cointegrated/rubert-tiny2")

query = "What is the capital of France?"
embedding_vector = embeddings.embed_query(query)
print(str(embedding_vector))
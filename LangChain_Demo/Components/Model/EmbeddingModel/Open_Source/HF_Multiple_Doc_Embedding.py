from langchain_huggingface import HuggingFaceEmbeddings

embedding = HuggingFaceEmbeddings(
    model_name="cointegrated/rubert-tiny2")

documents = [
    "Delhi is the capital of India.",
    "Spain is the country in Europe.",
    "Berlin is the capital of Germany."
    "Bangalore is the capital of Karnataka."
]
embedding_doc_vectors = embedding.embed_documents(documents)
print(str(embedding_doc_vectors))

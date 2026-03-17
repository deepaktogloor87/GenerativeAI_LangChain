from langchain_huggingface import HuggingFaceEmbeddings
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity

load_dotenv()

model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
documents = [
    "The cat is on the table.",
    "A dog is running on the grass.",
    "The sun is shining brightly.",
    "Like a rolling stone gathers no moss.",
]

doc_vec = model.embed_documents(documents)
query = "Where the dog is running?"
que_vec = model.embed_query(query)
similarity = cosine_similarity([que_vec], doc_vec)
similarity_scores = similarity[0]
enumerated_scores = list(enumerate(similarity_scores))
index, score = sorted(enumerated_scores, key=lambda x: x[1])[-1]
print(documents[index], score)




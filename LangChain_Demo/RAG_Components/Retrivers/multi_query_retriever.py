from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings, HuggingFaceEndpoint
from langchain_core.documents import Document
from langchain_classic.retrievers.multi_query import MultiQueryRetriever
from dotenv import load_dotenv

load_dotenv()

docs = docs = [
    Document(page_content="A balanced diet includes carbohydrates, proteins, fats, vitamins, and minerals.", metadata={"category": "nutrition"}),
    Document(page_content="Drinking enough water supports digestion and circulation.", metadata={"category": "wellness"}),
    Document(page_content="Regular exercise improves cardiovascular health and mental wellbeing.", metadata={"category": "fitness"}),
    Document(page_content="Mental health includes emotional, psychological, and social well-being.", metadata={"category": "mental_health"}),
    Document(page_content="Sleep is essential for body repair and cognitive function.", metadata={"category": "sleep"}),
    Document(page_content="Preventive care includes vaccinations and regular check-ups.", metadata={"category": "prevention"}),
    Document(page_content="Heart health depends on diet, exercise, and avoiding smoking.", metadata={"category": "cardiology"}),
    Document(page_content="Diabetes affects how the body processes blood sugar.", metadata={"category": "disease"}),
    Document(page_content="The immune system protects against infections and diseases.", metadata={"category": "immunity"}),
    Document(page_content="Stress management techniques include meditation and exercise.", metadata={"category": "wellbeing"}),
    Document(page_content="Maintaining a daily routine with consistent wake-up and sleep times improves productivity and overall wellbeing.", metadata={"category": "lifestyle"}),
    Document(page_content="Healthy eating habits such as consuming whole foods and limiting processed items support long-term health.", metadata={"category": "lifestyle"}),
    Document(page_content="Regular physical activity like walking, yoga, or gym workouts helps maintain body fitness and reduces stress.", metadata={"category": "lifestyle"}),
    Document(page_content="Practicing mindfulness and meditation enhances mental clarity and emotional stability.", metadata={"category": "lifestyle"}),
    Document(page_content="Work-life balance is essential to prevent burnout and maintain both professional and personal satisfaction.", metadata={"category": "lifestyle"}),
    Document(page_content="Artificial intelligence enables machines to perform tasks that typically require human intelligence such as learning and problem-solving.", metadata={"category": "technology"}),
    Document(page_content="Cloud computing allows users to access computing resources like storage and servers over the internet.", metadata={"category": "technology"}),
    Document(page_content="Cybersecurity practices protect systems, networks, and data from digital attacks and unauthorized access.", metadata={"category": "technology"}),
    Document(page_content="Machine learning is a subset of AI that focuses on building systems that learn from data to improve performance.", metadata={"category": "technology"}),
    Document(page_content="Blockchain technology provides a decentralized and secure way to record transactions across multiple systems.", metadata={"category": "technology"}),
    Document(page_content="FAISS is a library developed by Facebook AI for efficient similarity search and clustering of dense vectors.", metadata={"category": "faiss"}),    
    Document(page_content="LangChain simplifies building applications with LLMs by providing tools for chaining prompts, memory, and retrieval.", metadata={"category": "faiss"}),
    Document(page_content="Vector databases store embeddings and enable semantic search by comparing vector similarity instead of keyword matching.", metadata={"category": "faiss"}),
    Document(page_content="Embeddings convert text into numerical vectors that capture semantic meaning for machine learning models.", metadata={"category": "faiss"}),
    Document(page_content="Retrieval-Augmented Generation combines vector search with language models to produce more accurate and context-aware responses.", metadata={"category": "faiss"}),
]

#initialize hugginface embedding
embedding_model = HuggingFaceEmbeddings()

# create FIASS vector store
vectorstore = FAISS.from_documents(documents=docs,
                                   embedding=embedding_model)

#  create simple retriever
similarity_retriever = vectorstore.as_retriever(search_type='similarity',
                                                search_kwargs={'k':5})

#create retrievers
multiquery_retriever = MultiQueryRetriever.from_llm(
    retriever = vectorstore.as_retriever(search_kwargs={'k':5}),
    llm=HuggingFaceEndpoint(repo_id='mistralai/Mistral-7B-Instruct-v0.2',
                            task='text-generation')
)

#query
query = 'How to improve my health ?'

#retrivever result.
similarity_results = similarity_retriever.invoke(query)
multiquery_results = multiquery_retriever.invoke(query)

for i, doc in enumerate(similarity_results):
    print(doc.page_content)

for i, doc in enumerate(multiquery_results):
    print(doc.page_content)

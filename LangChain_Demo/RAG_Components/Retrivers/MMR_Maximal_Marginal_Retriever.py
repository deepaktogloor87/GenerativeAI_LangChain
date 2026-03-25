from langchain_core.documents import Document
from langchain.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings


docs = [

    # AI cluster
    Document(
        page_content="Artificial Intelligence enables machines to mimic human intelligence.",
        metadata={"domain": "AI"}
    ),
    Document(
        page_content="AI includes machine learning and deep learning techniques.",
        metadata={"domain": "AI"}
    ),

    # ML cluster (overlaps with AI)
    Document(
        page_content="Machine learning is a subset of AI that learns from data.",
        metadata={"domain": "ML"}
    ),
    Document(
        page_content="Supervised learning and unsupervised learning are types of machine learning.",
        metadata={"domain": "ML"}
    ),

    # Cloud cluster
    Document(
        page_content="Cloud computing provides scalable infrastructure over the internet.",
        metadata={"domain": "Cloud"}
    ),
    Document(
        page_content="AWS and Azure are popular cloud service providers.",
        metadata={"domain": "Cloud"}
    ),

]

embeddings_model = HuggingFaceEmbeddings()

vectorStore = FIASS.from_documents(
    documents=docs,
    embedding=embeddings_model
)

retriever = vectorStore.as_retriever(
    search_type='mmr',
    search_kwargs={'k':3, 'lambda_mult':1}   #lambda_mult is relavance-diversity baance, k=top 3 research
)

query = 'What is langchain?'
result = retriever.invoke(query)

for i,doc in enumerate(result):
    print(doc.page_content)

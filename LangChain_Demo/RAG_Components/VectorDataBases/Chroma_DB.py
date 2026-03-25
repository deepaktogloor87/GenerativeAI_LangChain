from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from langchain_core.documents import Document

doc1 = Document(
    page_content="Hugging Face provides open-source models for NLP, vision, and audio.",
    metadata={"source": "tech_intro", "topic": "AI Hub"}
)
doc2 = Document(
    page_content="LangChain's integration with Hugging Face enables seamless local model usage.",
    metadata={"source": "integration_guide", "topic": "Frameworks"}
)
doc3 = Document(
    page_content="The Transformers library allows for easy loading of state-of-the-art models.",
    metadata={"source": "library_docs", "topic": "Transformers"}
)
doc4 = Document(
    page_content="Vector stores like FAISS help retrieve relevant documents for RAG systems.",
    metadata={"source": "retrieval_manual", "topic": "Vector DB"}
)
doc5 = Document(
    page_content="Embeddings convert text into numerical formats for semantic search.",
    metadata={"source": "embedding_basics", "topic": "NLP"}
)

docs = [doc1, doc2, doc3, doc4, doc5]

# 1. Initialize Embeddings
embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

# 2. Initialize Chroma DB
vector_store = Chroma(
    persist_directory='LangChain_Demo/RAG_Components/VectorDataBases/my_chroma_db',
    embedding_function=embeddings,
    collection_name='simple'
)
print('Chroma DB Sucessfully Initialized...!')

# # Add documents to the chromadb
# vector_store.add_documents(documents=docs)
# print("Documents successfully added to Chroma!")

# print(vector_store._collection.count())

# view documents from chromadb
res = vector_store.get(include=["documents", "embeddings", "metadatas"])
print(res)

# let's perform search on vectorStore.
res1 = vector_store.similarity_search(
    query='Suggest me a good framework?',
    k=1
)
# print(res1)

# sementic search score
res_score = vector_store.similarity_search_with_score(
    query='What is sementic search?',
    k=1
)
# print(res_score)

# apply filtering
res_fil = vector_store.similarity_search_with_score(
    query='',
    filter={'topic':'Vector DB'}
)
# print(res_fil)

# How to update existing document.
update_doc2 = Document(
    page_content="LangChain's integration with Hugging Face enables seamless local model usage because langchain is a good framework.",
    metadata={"source": "integration_guide", "topic": "Frameworks"}
)

vector_store.update_document(document_id='db62666b-b4de-4a95-b39c-2ccb928f4655', 
                             document=update_doc2)

# view after updating the document
updated_doc_res = vector_store.get(include=["embeddings","metadatas","documents"])
print(updated_doc_res)
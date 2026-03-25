from langchain_huggingface import HuggingFaceEmbeddings, HuggingFacePipeline
from langchain_community.vectorstores import FAISS
from langchain_community.document_loaders import WikipediaLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_classic.chains.retrieval_qa.base import RetrievalQA
from transformers import pipeline

# ✅ Correct query
query = "History of Gothic Architecture"

# Load documents
loader = WikipediaLoader(query=query, load_max_docs=2)
documents = loader.load()

print("Documents loaded:", len(documents))

if not documents:
    raise ValueError("No documents retrieved. Fix your query.")

# Split documents
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)
docs = text_splitter.split_documents(documents)

# Embeddings
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# Vector store
vectorstore = FAISS.from_documents(docs, embeddings)

# Retriever ✅ FIXED
retriever = vectorstore.as_retriever(search_kwargs={"k": 3})

# HuggingFace LLM ✅ FIXED
hf_pipeline = pipeline(
    "text2text-generation",
    model="google/flan-t5-base",
    max_length=512,
    temperature=0.5
)

llm = HuggingFacePipeline(pipeline=hf_pipeline)

# QA Chain ✅ FIXED
qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    retriever=retriever,
    chain_type="stuff"
)

# Run
response = qa_chain.invoke(query)

print("\n=== Final Answer ===\n")
print(response)
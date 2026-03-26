from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings, HuggingFaceEndpoint
from langchain_classic.retrievers.contextual_compression import ContextualCompressionRetriever
from langchain_classic.retrievers.document_compressors import LLMChainExtractor
from langchain_core.documents import Document
from dotenv import load_dotenv

load_dotenv()

docs = [
    Document(page_content="""India, located in South Asia, is the world's most populous and seventh-largest country, known for its extreme diversity in culture, language, and geography. A former British colony, it gained independence in 1947 to become a major democratic and economic power, rapidly growing with a focus on technology, space exploration, and sustainable energy.""",
    metadata={"source":"Doc1"}),
    
    Document(page_content="""
    Europe is the world's second-smallest continent, located in the Northern Hemisphere and known for its immense cultural, linguistic, and historical diversity. It boasts over 40 countries, spanning from the expansive Russian landscapes to the tiny Vatican City. As a hub for global history and tourism, it features iconic landmarks, temperate climates, and significant economic influence.""",
    metadata={"source":"Doc2"}),
    
    Document(page_content="""
    The North Atlantic Treaty Organization (NATO) is a political and military alliance formed in 1949 by 12 countries from Europe and North America to provide collective security against potential threats, primarily the Soviet Union at the time. Headquartered in Brussels, Belgium, NATO currently comprises 32 member nations, promoting democratic values and defending members under Article.""",
    metadata={"source":"Doc3"})

]

    
# Embeddings
embedding_model = HuggingFaceEmbeddings()

# Vector store
vectorstore = FAISS.from_documents(docs, embedding_model)

# Retriever
base_retriever = vectorstore.as_retriever(search_kwargs={"k": 2})

# LLM
llm = HuggingFaceEndpoint(
    repo_id='mistralai/Mistral-7B-Instruct-v0.2',
    task='text-generation'
)

# Compressor
compressor = LLMChainExtractor.from_llm(llm)

# Compression retriever
compression_retriever = ContextualCompressionRetriever(
    base_retriever=base_retriever,
    base_compressor=compressor
)

# Query
query = "What NATO is all about?"

compressed_result = compression_retriever.invoke(query)

# Output
for i, doc in enumerate(compressed_result):
    print(f"\nResult {i+1}:\n{doc.page_content}")
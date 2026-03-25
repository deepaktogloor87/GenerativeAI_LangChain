from langchain_community.vectorstores import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_core.documents import Document

docs = [
    Document(
        page_content="The United States has complex relations with Iran and Israel.",
        metadata={"source": "news", "topic": "geopolitics"}
    ),
    Document(
        page_content="Israel and Iran have been in conflict over regional influence.",
        metadata={"source": "wiki", "topic": "middle east"}
    ),
    Document(
        page_content="The US supports Israel in many strategic and military aspects.",
        metadata={"source": "analysis", "topic": "foreign policy"}
    ),
    Document(
        page_content="Iran's nuclear program has raised concerns globally.",
        metadata={"source": "report", "topic": "nuclear"}
    ),
]

embedding_model = HuggingFaceEmbeddings()

vectorStore = Chroma.from_documents(
    documents=docs,
    embedding=embedding_model,
    collection_name='My_Collections'
)

retriever = vectorStore.as_retriever(search_kwargs={'k':1})

query = 'What is the United State relationship with Iran?'
result = retriever.invoke(query)

for i, doc in enumerate(result):
    print(f'\n--- result {i+1}---')
    print(doc.page_content)


from langchain_community.document_loaders import DirectoryLoader,PyPDFLoader

loader = DirectoryLoader(
    path='LangChain_Demo/RAG_Components/SamplePDFdocuments',
    glob='*.pdf',
    loader_cls=PyPDFLoader
)

docs = loader.load()
print(docs[4].page_content)
print(docs[4].metadata)
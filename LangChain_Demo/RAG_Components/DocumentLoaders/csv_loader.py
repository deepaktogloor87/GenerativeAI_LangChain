from langchain_community.document_loaders import CSVLoader

loader = CSVLoader(file_path = 'LangChain_Demo/RAG_Components/Social_Network_Ads.csv')

data = loader.load()
print(data[1])

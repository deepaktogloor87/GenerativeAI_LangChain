from langchain_community.tools import DuckDuckGoSearchRun
search_tool = DuckDuckGoSearchRun()
results = search_tool.invoke('Tell me today\'s latest news on LPG in India')
print(results)
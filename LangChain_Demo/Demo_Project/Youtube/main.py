from dotenv import load_dotenv
from youtube_transcript_api import YouTubeTranscriptApi, TranscriptsDisabled
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_core.prompts import PromptTemplate
from langchain_openai import OpenAIEmbeddings

load_dotenv()

# PHASE 1 Indexing

#Step 1 : Fetching Transcript from video and creating transcript

video_id = 'NebOSOTp-zA'  # only the ID which is between V= and & in the url
try:
    api = YouTubeTranscriptApi()
    # if you don't care which language, this return the best one
    transcript_list = api.fetch(video_id=video_id, languages=['en'])
    # print(transcript_list)

    #Flatten it to plan text
    transcript = " ".join(chunk.text for chunk in transcript_list)
    # print(transcript)

except TranscriptsDisabled:
    print("No captions available for this video")
    exit()

# Step 2 : applying textsplitter to prepare the document
splitter = RecursiveCharacterTextSplitter(
    chunk_size = 1000, 
    chunk_overlap = 200
)
chunks = splitter.create_documents([transcript])
# print(len(chunks))
# print(chunks)

# Step 3 : Convert all the chunks to vectorStore
embeddings = OpenAIEmbeddings(model='text-embedding-3-small')
vector_store = FAISS.from_documents(chunks, embeddings)

print(vector_store.index_to_docstore_id)





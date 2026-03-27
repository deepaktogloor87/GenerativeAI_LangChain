from dotenv import load_dotenv
from youtube_transcript_api import YouTubeTranscriptApi, TranscriptsDisabled
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_core.prompts import PromptTemplate

load_dotenv()

# PHASE 1 Indexing
video_id = 'vJOGC8QJZJQ'  # only the ID which is between V= and & in the url
try:
    api = YouTubeTranscriptApi()
    # if you don't care which language, this return the best one
    transcript_list = api.fetch(video_id=video_id, languages=['en'])

    #Flatten it to plan text
    transcript = " ".join(chunk.text for chunk in transcript_list)
    print(transcript)
except TranscriptsDisabled:
    print("No captions available for this video")



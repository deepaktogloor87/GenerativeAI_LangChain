from dotenv import load_dotenv
from youtube_transcript_api import YouTubeTranscriptApi, TranscriptsDisabled
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_core.prompts import PromptTemplate
from langchain_openai import OpenAIEmbeddings, ChatOpenAI

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

# print(vector_store.index_to_docstore_id)

# Phase 2 : RETRIEVER
# Step 1 : Create a retriever 
retriver = vector_store.as_retriever(search_type='similarity', search_kwargs={"k": 4})

# Step 2: Invoke retriver with user query.
query = """How langsmith helpful for evaluation?"""
retriver_output_list = retriver.invoke(query)

# print(retriver_output_list)

# Phase 3 : AUGMENTATION
# Step 1 : Prompt Template creation.
prompt = PromptTemplate(
    template="""
    You are the helpful assistant.
    Answer ONLY from the provided transcript contenxt.
    if the context is insufficient, just say I don't have much information about this particular topic.

    {context}
    question : {question}
    """,
    input_variables=["context", "question"]
)

# Step 2: calling retriver again with our actual question this time.
question = 'Is this topic aligned to help tester?, if yes what they discussed.'
retrived_docs = retriver.invoke(question)
# print(retrived_docs)

# Step 3: Build the context
context_text = '\n\n'.join([doc.page_content for doc in retrived_docs])

# Step 4: Final prompt
llm = ChatOpenAI(model='gpt-4o-mini')
final_prompt = prompt.format(context=context_text,
                             question=question)

# Phase 4 : GENERATION
# Step 1: Simply invoke the final_prompt to generate answer
response = llm.invoke(final_prompt)
print(response.content)
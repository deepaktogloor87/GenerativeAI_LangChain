from langchain_experimental.text_splitter import SemanticChunker
from langchain_huggingface import HuggingFaceEmbeddings
from dotenv import load_dotenv

load_dotenv()

# hugging_face_embedding = HuggingFaceEmbeddings(
#     model_name = 'sentence-transformers/all-MiniLM-L6-v2'
# )


text = """
Former means “the first of the two.” It comes from the Old English word “forma,” meaning “first or “earliest in time or order,” according to the Online Etymology Dictionary. The original definition goes back to the mid–12th century and changed around the late 1500s to its current meaning.
Freedom Movement was followed by the movement for the unification of Karnataka. After Independence, the Mysore State was created in 1953, wherein all the Kannada dominant areas under different dispensations were unified and the enlarged Mysore state carved in 1956 and was renamed Karnataka in 1973.
Bollywood the Mumbai-based Hindi film industry—is one of the largest film production centres in the world, releasing hundreds of films annually across various genres. 
"""

text_splitter = SemanticChunker(
    HuggingFaceEmbeddings(), breakpoint_threshold_type='percentile',
    breakpoint_threshold_amount=1.2
)

docs = text_splitter.create_documents([text])
print(len(docs))
print(docs)
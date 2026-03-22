from langchain_huggingface import HuggingFacePipeline
from transformers import pipeline
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain_core.runnables import RunnableParallel
import os
load_dotenv()

os.environ["HF_HOME"] = "D:/huggingface_cache"

pipe = pipeline(
    "text2text-generation",
    model="google/flan-t5-base",
)
HF_model = HuggingFacePipeline(pipeline=pipe)

prompt1 = PromptTemplate.from_template(
"""Summarize the following text into clear bullet-point notes:  \n {text}""")

prompt2 = PromptTemplate.from_template(
"""Create 5 question-answer pairs from the text.\n {text}""")


prompt3 = PromptTemplate.from_template(
"""Combine the following into a well-structured document:

NOTES:
{notes}

QUIZ:
{quiz}

Format with headings and clean structure."""
)

parser = StrOutputParser()

parallel_chain = RunnableParallel(
    {
        'notes' : prompt1 | HF_model | parser,
        'quiz' : prompt2 | HF_model | parser
    }
)

merge_chain = prompt3 | HF_model | parser

chain = parallel_chain | merge_chain

text = """
Give feedback on a generated list
Gemini for Google Workspace:

Constantly learns
May not be able to support every request at this time
If you get a suggestion that’s inaccurate or that you feel is unsafe, you can submit feedback to us. Your feedback can be used to enhance AI-assisted Workspace features and expand Google efforts in AI.

To provide feedback:

Below the generated list, select Good suggestion  or Bad suggestion .
If you select Bad suggestion , you can select the issue you found and enter additional feedback.
If you want to include the output with your feedback, check "Output."
Select Submit.
To provide general feedback on this feature:

Open the Menu Google Play Store Menu Icon.
Select Help and feedback.
To report a legal issue, create a request.

Learn about Gemini feature suggestions
Gemini feature suggestions don’t represent Google’s views, and should not be attributed to Google.
Do not rely on Gemini as medical, legal, financial, or other professional advice.
Gemini may suggest inaccurate or inappropriate information. Your feedback makes Gemini more helpful and safe.
You can submit feedback about your experience using this feature. Please ensure that your feedback doesn’t contain personal, sensitive, or confidential information.
"""

result = chain.invoke({'text':text})
print(result)


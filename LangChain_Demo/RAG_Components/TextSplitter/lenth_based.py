from langchain_text_splitters import CharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader(
    file_path='LangChain_Demo/RAG_Components/Job_Description.pdf'
)

text2 = loader.load()

text = """
Our team of independent experts exposes threats to justice through original research and identifies practical changes to fix them. We campaign to change policies, support strategic litigation, reform policy and develop international standards and best practice. We do this by supporting local movements for reform and building partnerships with lawyers, activists, academics and other NGOs. Find out more about how we work.

Our vision
A world in which governments use the power of the criminal process with utmost restraint, humanity, fairness, equality, and respect for the rights and dignity of all people.

Our mission
We serve as an international criminal justice watchdog working to expose, challenge and remedy systemic injustice in criminal processes. We oppose overcriminalisation, discrimination, disparate treatment, and marginalisation of communities. Through evidence-based research, we support broad coalitions, where appropriate, to expose injustice and promote fundamental human rights at all stages of the criminal process.

Our principles
Fair Trials has developed a set of principles that guide our work and help us to deliver our vision and mission. These are outlined in our 2022 strategy, which is available to download in English, French and Spanish.

Where we work
Our mission is global but we are currently focused on campaigning for fair, equal and just criminal legal systems in Europe, Latin America, the UK and the US. We are the only international NGO that campaigns exclusively for the right to a fair trial, which gives us a comparative perspective on the causes of injustice and how to tackle them. Find out more about where we work.

Building a movement
We know that we will not achieve the changes we want on our own. We work with many partners and networks, to support and build wider movements for reform. These partners include local and international NGOs, lawyers and other criminal justice professionals, and academics. Find out more about how we are building a movement.

Funding and governance
Fair Trials is an independent non-profit organisation with no party-political affiliations. We are funded by a combination of charitable grants and donations. Fair Trials is governed by a board of volunteer Trustees, responsible for the charity’s strategic direction and financial management.

Our history
Human rights lawyer, Stephen Jakobi OBE, founded Fair Trials (then Fair Trials Abroad) in 1992, in response to high-profile cases of injustice across the globe. Today, Fair Trials campaigns for fair and equal criminal justice systems. Recent successes include playing a leading role in the reform of INTERPOL and the development of criminal procedural rights as directly enforceable laws in every EU member state. Between 2008-2021, the organisation was led by Jago Russell.

Charitable and legal status
“Fair Trials” includes Fair Trials International, Fair Trials Europe, and Fair Trials Americas. Fair Trials International is a registered charity (no. 1134586) and in 2010 was incorporated with limited liability in England and Wales (No. 7135273), and is based at 5 Castle Road, London, NW1 8PR. In May 2014, we founded Fair Trials Europe, which is a registered public foundation in Belgium (registered number 0552.688.677). In 2018 we founded Fair Trials Americas, which is a registered 501(c)(3) public charity in the United States of America (No DLN17053243307017).

Fair Trials International is registered with the Dutch Tax Inspectorate for tax exempt status. Its RSIN (Rechtspersonen en Samenwerkingsverband en Informatienummer) number is 8238.23.593.
"""

splitter = CharacterTextSplitter(
    separator='',
    chunk_size=200,
    chunk_overlap=0
)

# result = splitter.split_text(text)
# print(result)

result = splitter.split_documents(text2)
print(result[0].page_content)
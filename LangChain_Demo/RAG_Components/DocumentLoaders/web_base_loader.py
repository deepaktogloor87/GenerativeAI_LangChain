from langchain_community.document_loaders import WebBaseLoader

product_url = 'https://www.amazon.in/Play-Nation-Premium-Fastest-Birthday/dp/B0CQC2NXJ6/ref=sr_1_2_sspa?crid=WU081G88EFO5&dib=eyJ2IjoiMSJ9.2wn2DJNy9ftjJfN10xqLti_HZEAQ7tr88HtedmFEgbx73B7foPo4e3ycXr56BAisEygDrmZYh8c_fnamEsDwQnN9NdhlFGV8l570-o2kORptTsJvDE3ZpGTpucQccrWzFBaaDU72yc6Z3W_Tbyrbo1JnBmhmhIm8eKD1SUrCYWfssOe7SHu9XEBHKcEmEEWLDwYqvKd7NGtKTwqhYkbEP9K6_dJBOGB83pUrB_wcP8emOHtWxNWNk0xpYTViCILJ9D9tKegkXSwBtaaFS0p04ZKT8kve0hDZBrgU3cGXzek.DMTNj47jy-2LbFVfzTx2fM46GIyAZtMml9QWt4xrxbc&dib_tag=se&keywords=fastest+finger+first+board+game&qid=1774276496&sprefix=fastest+fin%2Caps%2C515&sr=8-2-spons&aref=1QgAIch98C&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&psc=1'
loader = WebBaseLoader(
    web_path=product_url)

docs = loader.load()
print(len(docs))
print(docs[0].page_content)
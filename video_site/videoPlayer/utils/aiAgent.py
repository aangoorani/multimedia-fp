import os
from langchain_community.llms import HuggingFaceHub

api = "HUGGING_FACE_API"
huggingfacehub_api_token = os.environ[api]

llm = HuggingFaceHub(repo_id='tiiuae/falcon-7b-instruct', huggingfacehub_api_token=huggingfacehub_api_token)

if __name__ == "__main__":
    input = 'Health is wealth, but is it the order of priority for most of us?'
    output = llm.invoke(input)
    print(output)


import weaviate
from dotenv import load_dotenv
import os
from langchain.embeddings import OpenAIEmbeddings
from langchain.chat_models import AzureChatOpenAI

load_dotenv()


auth_config = weaviate.AuthApiKey(api_key=os.getenv("WEAVIATE_KEY"))
client = weaviate.Client(
    url=os.getenv("WEAVIATE_URL"),
    auth_client_secret=auth_config, 
)


llm = AzureChatOpenAI( 
     temperature=0,
     openai_api_base=os.getenv("OPENAI_API_BASE"),
     openai_api_version="2023-05-15",
     deployment_name="GPT3-5",
     openai_api_key=os.getenv("OPENAI_API_KEY"),
     openai_api_type="azure"
     
)

client.schema.delete_class("Document")


embeddings = OpenAIEmbeddings (openai_api_key= os.getenv('OPENAI_API_KEY'),deployment="GPTVectorization")





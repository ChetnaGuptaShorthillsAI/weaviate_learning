from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.document_loaders import PyPDFLoader
from langchain.schema import Document
from langchain.embeddings import SentenceTransformerEmbeddings
import json
from client import embeddings
from langchain.document_loaders import TextLoader

loader = TextLoader("/home/shtlp_0145/shorthills_projects/gst_credibility/Section.txt")
docs=loader.load()


print(docs)
text_splitter = RecursiveCharacterTextSplitter(
            separators="////",
            chunk_size=100,
            chunk_overlap=20,
            length_function=len,
            is_separator_regex=False,
        )

chunks = text_splitter.split_documents(docs)

print(len(chunks))
vectordb=[]
json_data=[]

for i,chunk in enumerate(chunks):
 temp=chunk.page_content
#  print(temp)
 vector=embeddings.embed_query(temp)
 vectordb.append(vector)
 json_data.append({"text": chunk.page_content, "file_name":chunk.metadata['source'],"chunk_number":i+1} )

file_path = "data.json"


# Save the JSON data to the file
with open(file_path, "w") as json_file:
     json.dump(json_data, json_file, indent=2)

with open("vector.json", "w") as json_file:
     json.dump(vectordb, json_file, indent=2)


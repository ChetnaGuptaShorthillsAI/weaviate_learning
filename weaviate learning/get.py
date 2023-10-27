import json
from config import client
from langchain.chains.question_answering import load_qa_chain
from config import llm
from config import embeddings
from langchain.docstore.document import Document



# chain = load_qa_chain(llm, chain_type="stuff")
class_name = "Research"


vector=embeddings.embed_query("Unsupervised Feature-based Approaches")

docs = client.query.get(
    class_name,
    ["text", "chunk_number"]
).with_limit(10).with_near_vector({"vector": vector}).do()

print(json.dumps(docs, indent=2))


# results = co.rerank(model="rerank-english-v2.0", query="Lessor", documents=docs["data"]["Get"]["Lease"], top_n=5)

# print(results)

# docs = client.query.get(
#     class_name,
#     ["text", "chunk_number"]
# ).with_limit(3).with_near_vector({"vector": vector}
# ).with_additional(
#     ["distance", "id"]
# ).do()


# print(json.dumps(docs, indent=2))

# doc=docs["data"]["Get"][class_name]


# document_list = []
# for temp in doc:
#     document_list.append(Document(page_content=temp["text"]))


# question = "Context: This document is a scietific research paper. Give me a list of headings in this document."

# answer = chain.run(input_documents=document_list, question=question)

# print(answer)
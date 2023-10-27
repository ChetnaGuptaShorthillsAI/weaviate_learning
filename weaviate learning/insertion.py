import json
from config import client
from weaviate.util import generate_uuid5  

with open('data.json', 'r') as file:
    data = json.load(file)

with open('vector.json', 'r') as file:
    vectordb = json.load(file)

print(len(vectordb[0]))
print(len(vectordb))
class_name = "Research"

client.schema.delete_class(class_name)  # Replace with your class name - e.g. "Question"


client.batch.configure(
    batch_size=50,
    num_workers=2,   
)
with client.batch as batch:
    for i, data_obj in enumerate(data):
        batch.add_data_object(
            data_obj,
            class_name,
            uuid=generate_uuid5(data_obj),  # Optional: Specify an object ID
            vector=vectordb[i],  # Optional: Specify an object vector
        )


response = client.query.aggregate(
    class_name=class_name,
).with_meta_count().do()

print(json.dumps(response, indent=2))
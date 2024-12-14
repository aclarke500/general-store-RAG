# from sentence_transformers import SentenceTransformer
# import numpy as np
import lancedb
from product_meta_data import ProductMetaData
from vector_db_utils import create_vector_schema

# Load the SentenceTransformer model
# embedding_length = 768
# model = SentenceTransformer('all-MPNet-base-v2')

# def embed_item(item):
#     description = item['description']   
#     # Embed the description, convert it to vector of 768 in np array

#     embedding = model.encode(description) 
#     normalized_embedding = embedding / np.linalg.norm(embedding) # normalize the vector for more efficient comparison
#     return normalized_embedding

# def create_vector_schema(meta_data):
#     vector_schema = [] # list of dictionaries with meta data and vectorized description
#     for item in meta_data:
#         vector = embed_item(item)
#         item['vector'] = vector
#         vector_schema.append(item)
#     return vector_schema 

# connect to LanceDB
db = lancedb.connect("./general_store_db") # we expect to run this file from root directory

# Drop pre-existing data
for table_name in db.table_names():
    db.drop_table(table_name)

food_meta_data = ProductMetaData['food']
pet_meta_data = ProductMetaData['pet']
electronics_meta_data = ProductMetaData['electronics']

food_vector_schema = create_vector_schema(food_meta_data)
pet_vector_schema = create_vector_schema(pet_meta_data)
electronics_vector_schema = create_vector_schema(electronics_meta_data)

# Create tables
db.create_table("food", data=food_vector_schema)
db.create_table("electronics", data=electronics_vector_schema)
db.create_table("pet_supplies", data=pet_vector_schema)

print("Database created successfully!")
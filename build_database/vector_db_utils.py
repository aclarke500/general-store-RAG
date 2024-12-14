from sentence_transformers import SentenceTransformer
import numpy as np

# Load the SentenceTransformer model
model = SentenceTransformer('all-MPNet-base-v2')


def embed_item(item):
    description = item['description']   
    # Embed the description, convert it to vector of 768 in np array
    if not description:
        raise ValueError("Item must contain a 'description' field.")
    embedding = model.encode(description) 
    normalized_embedding = embedding / np.linalg.norm(embedding) # normalize the vector for more efficient comparison
    return normalized_embedding

def create_vector_schema(meta_data):
    vector_schema = [] # list of dictionaries with meta data and vectorized description
    for item in meta_data:
        vector = embed_item(item)
        item['vector'] = vector
        vector_schema.append(item)
    return vector_schema 
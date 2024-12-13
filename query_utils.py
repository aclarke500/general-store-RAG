from sentence_transformers import SentenceTransformer
import numpy as np
model = SentenceTransformer('distilbert-base-nli-stsb-mean-tokens')


def get_department(query):
    department = None
    category = query["category"]
    # if the query category matches our database categories exactly, return it
    # else return None because something has gone wrong
    categories = ["food", "pet_supplies", "electronics"]
    if category in categories:
        return category
    return None

def embed_query_description(query):
    if "description" not in query:
        raise ValueError("Query must contain a description")
    
    description = query["description"]
    embedding = model.encode(description)
    normalized_embedding = embedding / np.linalg.norm(embedding)
    return normalized_embedding
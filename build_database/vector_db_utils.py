from sentence_transformers import SentenceTransformer
import numpy as np

# Load the SentenceTransformer model
model = SentenceTransformer('all-MPNet-base-v2')


def embed_item(item: dict) -> np.ndarray:
    """
    Embeds the description in the item using the SentenceTransformer model.

    Args:
        item (dict): The item data.

    Returns:  
        np.ndarray: The normalized embedding of the description.
    """
    description = item['description']   
    # Embed the description, convert it to vector of 768 in np array
    if not description:
        raise ValueError("Item must contain a 'description' field.")
    embedding = model.encode(description) 
    normalized_embedding = embedding / np.linalg.norm(embedding) # normalize the vector for more efficient comparison
    return normalized_embedding

def create_vector_schema(meta_data: list[dict]) -> list[dict]:
    """
    Embeds the description in the query using the SentenceTransformer model.

    Args:
        meta_data (list[dict]): The meta data for the database items.

    Returns:
        list[dict]: The vectorized schema of the database.
    """
    vector_schema = [] # list of dictionaries with meta data and vectorized description
    for item in meta_data:
        vector = embed_item(item)
        item['vector'] = vector
        vector_schema.append(item)
    return vector_schema 
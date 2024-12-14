import unittest
import numpy as np
from build_database.vector_db_utils import embed_item, create_vector_schema
from build_database.product_meta_data import ProductMetaData

embedding_size = 768 # we use this in case the transformer model changes so we can dynamically update the size

class TestBuildDB(unittest.TestCase):
    def test_embed_item(self):
        item = {'description': 'This is a test description'}
        vector = embed_item(item)
        self.assertEqual(vector.shape, (embedding_size,), "Embedding is not of the correct shape. Did you change the transformer model?")

    def test_embed_item_no_description(self):
        item = {'description': ''}
        with self.assertRaises(ValueError) as context:
            embed_item(item)
        self.assertTrue('Item must contain a \'description\' field.' in str(context.exception), "No description error message not raised")

    def test_embedding_is_normalized(self):
        item = {'description': 'This is a test description'}
        vector = embed_item(item)
        self.assertTrue(np.linalg.norm(vector) - 1 <= 1e-5, "embedding is not normalizd") # check if the norm is close to 1

    def test_create_vector_schema(self):
        meta_data = ProductMetaData['food']
        vector_schema = create_vector_schema(meta_data)
        self.assertEqual(len(vector_schema), len(meta_data), "Vector schema does not have the same length as meta data")
        self.assertEqual(vector_schema[0]['vector'].shape, (embedding_size,), "Embedding is not of the correct shape. Did you change the transformer model?")
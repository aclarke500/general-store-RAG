import unittest
import numpy as np
from utils.query_utils import query_db, query_LLM, get_department, embed_query_description
import lancedb
import pandas as pd

class TestRAG(unittest.TestCase):
    embedding_size = 768
    sample_query_food = {"category": "food", "description": "I need some food", "price_min": 0, "price_max": 100, "quantity_min": 1}

    # get_department tests
    def test_get_department_returns_category(self):
        sample_query = {"category": "food", "description": "I need some food", "price_min": 0, "price_max": 100, "quantity_min": 1}
        result = get_department(sample_query)
        self.assertEqual(result, "food", "get_department should return the category if it exists in the database. Did not return food. Were the categories updated?")

    def test_get_department_returns_none(self):
        sample_query = {"category": "clothing", "description": "I need some clothes", "price_min": 0, "price_max": 100, "quantity_min": 1}
        result = get_department(sample_query)
        self.assertIsNone(result, "get_department should return None if the category does not exist in the database. Did not return None. Do the categories now include clothes?")

    def test_get_department_capitals(self):
        sample_query = {"category": "FOOD", "description": "I need some food", "price_min": 0, "price_max": 100, "quantity_min": 1}
        result = get_department(sample_query)
        self.assertEqual(result, "food", "get_department should return the category if it exists in the database. Did not return food. Were the categories updated?")

    def test_get_department_empty(self):
        sample_query = {"description": "I need some food", "price_min": 0, "price_max": 100, "quantity_min": 1}
        result = get_department(sample_query)
        self.assertIsNone(result, "get_department should return None if the category is not provided")
        
        

    # embed_query_description tests
    def test_embed_query_description_shape(self):
        result = embed_query_description(self.sample_query_food)
        self.assertEqual(result.shape, (self.embedding_size,), "embed_query_description should return a vector of shape (768,)")

    def test_embed_query_decription_is_normalized(self):
        result = embed_query_description(self.sample_query_food)
        self.assertAlmostEqual(np.linalg.norm(result), 1, 5, "embed_query_description should return a normalized vector")

    def test_embed_query_description_no_description(self):
        with self.assertRaises(ValueError):
            embed_query_description({"category": "food", "price_min": 0, "price_max": 100, "quantity_min": 1})
        
    def test_embed_query_description_empty_description(self):
        with self.assertRaises(ValueError):
            embed_query_description({"category": "food", "description": "", "price_min": 0, "price_max": 100, "quantity_min": 1})

    # query_db tests
    def test_query_db_returns_dataframe(self):
        db = lancedb.connect("./general_store_db")
        result = query_db(self.sample_query_food, db)
        self.assertIsInstance(result, pd.DataFrame, "query_db should return a pandas DataFrame")

    def test_query_db_invalid_department(self):
        db = lancedb.connect("./general_store_db")
        sample_query = {"category": "clothing", "description": "I need some clothes", "price_min": 0, "price_max": 100, "quantity_min": 1}
        result = query_db(sample_query, db)
        self.assertEqual(len(result), 0, "query_db should return an empty DataFrame if the department is not found")

    def test_query_db_no_department(self):
        db = lancedb.connect("./general_store_db")
        sample_query = {"description": "I need some food", "price_min": 0, "price_max": 100, "quantity_min": 1}
        result = query_db(sample_query, db)
        self.assertEqual(len(result), 0, "query_db should return an empty DataFrame if the department is not found")

    def test_query_db_no_description(self):
        db = lancedb.connect("./general_store_db")
        sample_query = {"category": "food", "price_min": 0, "price_max": 100, "quantity_min": 1}
        with self.assertRaises(ValueError):
            query_db(sample_query, db)
        
    # query_LLM tests
    def test_query_LLM_returns_string(self):
        result = query_LLM("I am interested in buying a laptop")
        self.assertIsInstance(result, dict, "query_LLM should return a dictionary object")

    def test_query_LLM_no_input(self):
        with self.assertRaises(ValueError, msg="query_LLM should raise a ValueError if the input is empty"):
            query_LLM("")

    def test_query_LLM_wrong_input_type(self):
        with self.assertRaises(ValueError, msg="query_LLM should raise a ValueError if the input is not a string"):
            query_LLM(123)
    
    def test_query_LLM_no_input(self):
        with self.assertRaises(TypeError, msg="query_LLM should raise a ValueError if the input is empty"):
            query_LLM()

    

    
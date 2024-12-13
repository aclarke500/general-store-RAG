import lancedb
import os
import pandas as pd
from dotenv import load_dotenv
from openai import OpenAI
from query_utils import get_department, embed_query_description
import json

load_dotenv()
api_key = os.getenv('open_ai_key')



db = lancedb.connect("./general_store_db")
food_table = db["food"]
pet_table = db["pet_supplies"]
electronics_table = db["electronics"]

client = OpenAI(api_key=api_key)

# def 

# Common keys across all categories: {'category', 'id', 'name', 'availability', 'quantity', 'price', 'description'}


def query_LLM(user_input):
    system_message = {
        "role": "system",
        "content": (
            "You are a helpful assistant that translates user prompts into structured queries "
            "for a vector database storing product information. The database has three departments: 'pet_supplies', 'food', and 'electronics'. "
            "Your goal is to interpret the user's intent and return a structured response in the following JSON format: "
            "{category: 'food', description: 'An iPad with 64GB of Storage', filters: {price: {'$gte': 0, '$lte': 500}, quantity: {'$gte': 1}, availability: True, sort_by: 'price', sort_order: 'asc'}}. "
            "The filters must include the following keys: "
            "'price' (a range specified as {'$gte': 0, '$lte': 1000000}), 'quantity' (default {'$gte': 0}), 'availability' (default True), "
            "'sort_by' (either 'quantity', 'price', or 'name'; default 'price'), and 'sort_order' ('asc' or 'desc'; default 'asc'). "
            "The 'description' should summarize the qualitative attributes of the product the user is requesting (e.g., 'An affordable and durable laptop'), "
            "without including specific filter values such as price or quantity. "
            "The 'category' field must match one of the three departments ('pet_supplies', 'food', or 'electronics') or default to 'food' if the category cannot be inferred. "
            "Always ensure that the 'filters' object is structured so it can be passed directly into a table.search(vector).filter(filters) call in Python. "
            "If the user provides no details, use the default values for all fields. "
            "Return the response as a valid JSON string with no extraneous text or formatting."
        )
    }


    user_message = {
        "role": "user",
        "content":user_input
    }

    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[system_message, user_message],
        max_tokens=150,
        temperature=0.7
    )
    response_message = json.loads(completion.choices[0].message.content)
    return response_message

def query_db(query):
    table_name = get_department(query)
    if not table_name:
        return [] # return an empty list if the department is not found
    print(table_name)
    table = db.open_table(table_name)
    query_vector = embed_query_description(query)

    results = table.search(query_vector, query["filters"]).to_pandas()

    return results


user_input = input("Enter your query: ")
response = query_LLM(user_input)

results = query_db(response)
print(results.head(10))
import lancedb
from query_utils import query_db, query_LLM
from intro import display_ascii_art

db = lancedb.connect("./general_store_db")


display_ascii_art()
message = 'Hi! I am Beedle, your assistant. What are you looking for?'
while True:
    user_input = input(message + '\n')
    response = query_LLM(user_input)
    print(response)

    results = query_db(response, db)
    print(results.head(10))
    message = 'Is there anything else I can help you with?'
import lancedb
from utils.query_utils import query_db, query_LLM
from utils.intro import display_ascii_art

def main():
    db = lancedb.connect("./general_store_db")

    display_ascii_art()
    message = 'Hi! I am Beedle, your assistant. What are you looking for? (Type "exit" to quit)'

    while True:
        try:
            user_input = input(message + '\n')
            if user_input.lower() == 'exit':
                print('Goodbye!')
                break
            response = query_LLM(user_input)

            results = query_db(response, db)
            print(results.head(10))
            message = 'Is there anything else I can help you with?'
        except Exception as e:
            print(f"An error occurred: {e}")
            message = 'Sorry, I encountered an error. Please try again.'

if __name__ == "__main__":
    main()

# general-store-RAG

## Dependencies
The dependencies are listed in the requirements.txt folder. They can be installed by running: <br> 
<code>pip install -r requirements.txt
</code>

## Api Keys - Setup Required
This project uses a GPT 3.5 for the LLM portion of the RAG. The API keys are obviously not included in this public repo. To add your own API key, create a .env file in the root directory and add this: <br>
<code>open_ai_key = sk-your-api-key-here
</code>

## Lance DB Setup
Due to it's modest size, the databse is included in it's entirety on the repo. However, on different machines the database may behave differently. If the database is not behaving properly, run (from the project root directory, or else it will not work): <br>
<code>python3 build_database/build_vector_db.py
</code> <br>
This will populate the general store with three tables, 'electronics', 'food', and 'pet supplies' meta data and vector embeddings.

## Usage
With that setup out of the way, execute <code>main.py</code> in the project root directory.

## Testing
In order to run the unit tests, execute <code>python -m unittest discover</code> in the project root directory.
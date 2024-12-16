echo "Setting up general-store-RAG"
touch .env # Create .env file for the api key

echo "Installing required packages"
pip install -r requirements.txt

echo "Setting up the database"
python3 build_database/build_vector_db.py

echo "Running unit tests..."
python3 -m unittest discover 

echo "Setup complete. Running the app..."
python3 main.py
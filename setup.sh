echo "Setting up general-store-RAG"

# Step 1: Create a virtual environment
python3 -m venv venv
source venv/bin/activate  # Activate the virtual environment

# Step 2: Create .env file for API key
touch .env

# Step 3: Install required packages
echo "Installing required packages"
pip install --upgrade pip
pip install -r requirements.txt

# Step 4: Setup the database
echo "Setting up the database"
python3 build_database/build_vector_db.py

# Step 5: Run unit tests
echo "Running unit tests..."
python3 -m unittest discover 

# Step 6: Start the app
echo "Setup complete. Running the app..."
python3 main.py

import lancedb

# Connect to LanceDB
db = lancedb.connect("./general_store_db")

# Define schemas
food_schema = [
    {"id": 1, "name": "Apple", "category": "Fruit", "price": 0.5, "availability": "In Stock", "shelf_life": "1 Week"},
    {"id": 2, "name": "Milk", "category": "Dairy", "price": 2.5, "availability": "In Stock", "shelf_life": "5 Days"}
]

electronics_schema = [
    {"id": 1, "name": "Laptop", "category": "Computers", "price": 800, "availability": "In Stock", "warranty_period": "1 Year"},
    {"id": 2, "name": "Headphones", "category": "Accessories", "price": 50, "availability": "Out of Stock", "warranty_period": "6 Months"}
]

pet_supplies_schema = [
    {"id": 1, "name": "Dog Food", "category": "Food", "price": 20, "availability": "In Stock", "suitable_for": "Dog"},
    {"id": 2, "name": "Cat Toy", "category": "Toys", "price": 5, "availability": "In Stock", "suitable_for": "Cat"}
]

# Create tables
db.create_table("food", data=food_schema)
db.create_table("electronics", data=electronics_schema)
db.create_table("pet_supplies", data=pet_supplies_schema)

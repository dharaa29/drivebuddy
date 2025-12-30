from database import get_collection

users = get_collection("users")

# Insert a test document
users.insert_one({"name": "Dharaa", "role": "admin"})

# Fetch and print documents
for user in users.find():
    print(user)

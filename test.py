from pymongo import MongoClient

try:
    client = MongoClient("your_connection_string")
    print(client.list_database_names())
except Exception as e:
    print("Connection failed:", e)

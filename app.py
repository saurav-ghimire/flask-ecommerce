from flask import Flask, jsonify, request
from pymongo import MongoClient
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

# Get credentials from environment
MONGODB_USERNAME = os.getenv("MONGODB_USERNAME")
MONGODB_PASSWORD = os.getenv("MONGODB_PASSWORD")

# MongoDB URI
MONGODB_URI = f"mongodb+srv://{MONGODB_USERNAME}:{MONGODB_PASSWORD}@cluster0.l2a9v.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# Initialize MongoDB client
try:
    client = MongoClient(MONGODB_URI)
    db = client["Ecommerce-Flask"]  #actual database name
    print("Connected to MongoDB successfully")
except Exception as e:
    print("Failed to connect to MongoDB:", e)
    db = None

@app.route("/")
def home():
    return jsonify({"message": "Welcome to the MongoDB Flask App!"})

@app.route("/collections", methods=["GET"])
def get_collections():
    try:
        collections = db.list_collection_names()
        return jsonify({"collections": collections})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/insert", methods=["POST"])
def insert_document():
    try:
        collection_name = request.json.get("collection", "default_collection")
        data = request.json.get("data", {})
        
        collection = db[collection_name]
        result = collection.insert_one(data)
        return jsonify({
            "message": "Document inserted successfully",
            "id": str(result.inserted_id)
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/find", methods=["GET"])
def find_documents():
    try:
        collection_name = request.args.get("collection", "default_collection")
        collection = db[collection_name]
        
        documents = list(collection.find({}, {"_id": 0}))  # Exclude MongoDB ObjectId
        return jsonify({"documents": documents})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)

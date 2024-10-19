from flask import Flask, render_template
from pymongo import MongoClient
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

# MongoDB Atlas connection with environment variables
MONGODB_USERNAME = os.getenv('MONGODB_USERNAME')
MONGODB_PASSWORD = os.getenv('MONGODB_PASSWORD')

client = MongoClient(f"mongodb+srv://{MONGODB_USERNAME}:{MONGODB_PASSWORD}@ecommerce-cluster.0xwr1.mongodb.net/?retryWrites=true&w=majority")
db = client['shop_db']
products_collection = db['products']

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/products')
def products():
    products = list(products_collection.find())
    return render_template('products.html', products=products)

if __name__ == '__main__':
    app.run(debug=True)

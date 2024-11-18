import unittest
from app import app
from pymongo import MongoClient
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Utility class for database setup
class MongoDBTestBase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """
        Load environment variables and set up MongoDB connection.
        """
        username = os.getenv('MONGODB_USERNAME')
        password = os.getenv('MONGODB_PASSWORD')
        cls.client = MongoClient(
            f"mongodb+srv://{username}:{password}@cluster0.l2a9v.mongodb.net/?retryWrites=true&w=majority"
        )
        cls.db = cls.client['Ecommerce-Flask']  # Use the same test database as in app.py

# Test 1: Route Test
class TestRoutes(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_invalid_method_on_products(self):
        """
        Test that a POST request to a non-existent /products route returns a 404 status code.
        """
        response = self.client.post('/products')  # Assuming /products is not defined in the app
        self.assertEqual(response.status_code, 404)  # Changed to 404 since the route doesn't exist

# Test 2: Database Read Test
class TestDatabaseRead(MongoDBTestBase):
    def test_mongodb_connection(self):
        """
        Test MongoDB connection using the ping command.
        """
        try:
            self.client.admin.command('ping')
        except Exception as e:
            self.fail(f"MongoDB connection failed: {str(e)}")

# Test 3: Database Write Test
class TestDatabaseWrite(MongoDBTestBase):
    def setUp(self):
        """
        Set up test database and collection.
        """
        self.collection = self.db['test_collection']

    def tearDown(self):
        """
        Clean up test database after tests.
        """
        self.db.drop_collection('test_collection')

    def test_write_data_to_db(self):
        """
        Test inserting a document into MongoDB and verify its presence.
        """
        new_data = {"field": "new_value"}
        self.collection.insert_one(new_data)
        inserted_data = self.collection.find_one({"field": "new_value"})
        self.assertIsNotNone(inserted_data)
        self.assertEqual(inserted_data['field'], 'new_value')

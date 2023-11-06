import pymongo
from bson import ObjectId


class MongoDBClient:
    """A class for connecting to and interacting with MongoDB."""

    def __init__(self, host="localhost", port=27017, database="my_database", username='mongodb_connector',
                 password='mongodb_connector'):
        """Initialize the MongoDB client.

        Args:
            host: The host address of the MongoDB server.
            port: The port number of the MongoDB server.
            database: The name of the MongoDB database to connect to.
        """
        print(host)
        print(port)
        print(database)
        self.client = pymongo.MongoClient(host, port, username=username, password=password)
        self.db = self.client[database]

    def connect(self):
        """Connect to the MongoDB server."""

        self.client.connect()

    def disconnect(self):
        """Disconnect from the MongoDB server."""

        self.client.close()

    def create_collection(self, collection_name):
        """Create a collection if it does not exist.

        Args:
            collection_name: The name of the collection to create.
        """

        if collection_name not in self.db.collection_names():
            self.db.create_collection(collection_name)

    def create_index(self, collection_name, field_name, unique=False):
        """Create an index on a field in a collection if it does not exist.

        Args:
            collection_name: The name of the collection to create the index on.
            field_name: The name of the field to create the index on.
            unique: Whether the index should be unique.
        """

        index_info = self.db[collection_name].index_information()
        if field_name not in index_info:
            self.db[collection_name].create_index(field_name, unique=unique)

    def save_facebook_post(self, post_id, text, image_url, created_time):
        """Save the text and image of a Facebook post to the database.

        Args:
            source: source of the posr
            post_id: The ID of the Facebook post.
            text: The text of the Facebook post.
            image_url: The URL of the Facebook post image.
            created_time: .
        """

        facebook_posts_collection = self.db["facebook_posts"]

        post = {
            '_id': ObjectId(),
            'source': 'facebook',
            "post_id": post_id,
            "text": text,
            "image_url": image_url,
            "created_time": created_time,
        }

        facebook_posts_collection.insert_one(post)

    def save_instagram_post(self, post_id, text, image_url, created_time):
        """Save the text and image of an Instagram post to the database.

        Args:
            post_id: The ID of the Instagram post.
            text: The text of the Instagram post.
            image_url: The URL of the Instagram post image.
            created_time: .
        """

        instagram_posts_collection = self.db["instagram_posts"]

        post = {
            '_id': ObjectId(),
            'source': 'instagram',
            "post_id": post_id,
            "text": text,
            "image_url": image_url,
            "created_time": created_time,
        }

        instagram_posts_collection.insert_one(post)

    def getAll(self, collection_name):
        # Access the database and collection
        collection = self.db[collection_name]

        # Retrieve all documents from the collection
        all_documents = list(collection.find())

        # Loop through the documents and print them
        for document in all_documents:
            print(document)

    def add(self, collection_name, post):
        self.db[collection_name].insert_one(post)

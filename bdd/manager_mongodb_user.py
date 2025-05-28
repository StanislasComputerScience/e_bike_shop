from pymongo import MongoClient
from pymongo.collection import Collection
from bson.objectid import ObjectId
import sys
import os
import bcrypt
import datetime as date
import random

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
# Add parent folder au sys.path
import const_values as cv


def generate_password() -> None:
    """Generate password"""
    # Declaring our password
    passwords = [
        "password123",
        "bonjour2024",
    ]

    for pwd in passwords:
        hashed = bcrypt.hashpw(pwd.encode(), bcrypt.gensalt())
        print(f"{pwd:<18} --- {hashed.decode('utf-8')}")


def get_collection(validator: dict) -> Collection:
    """Get collection 'User'

    Args:
        validator (dict): contain jsonSchema

    Returns:
        Collection: 'User' collection
    """

    # 1. Connection
    client = MongoClient(cv.MONGODB_LOCAL_PATH)
    db = client[cv.MONGODB_NAME]

    # Check if table User exist
    try:
        # 2. Création de la collection avec validation
        collection = db.create_collection("User", validator=validator)
    except:
        db.User.drop()
        # 2. Création de la collection avec validation
        collection = db.create_collection("User", validator=validator)

    return collection


def create_schema_user() -> dict:
    """Create schema collection 'User'

    Returns:
        dict: $jsonSchema: schema
    """
    # 1. Définition du schéma
    schema = {
        "bsonType": "object",
        "required": [
            "name",
            "firstname",
            "email",
            "password",
            "birth_date",
            "connection",
            "role",
        ],
        "properties": {
            "name": {"bsonType": "string"},
            "firstname": {"bsonType": "string"},
            "birth_date": {"bsonType": "date"},
            "email": {"bsonType": "string"},
            "password": {"bsonType": "string"},
            "age": {
                "bsonType": "int",
                "minimum": 0,
            },
            "phone": {"bsonType": "string"},
            "connection": {
                "enum": [
                    "timeout",
                    "pending",
                    "connected",
                ],
                "description": "Must be either timeout, pending or connected",
            },
            "role": {
                "enum": [
                    "admin",
                    "user",
                ],
                "description": "Must be either admin or user",
            },
            "shoppingcarts": {
                "bsonType": "array",
                "minItems": 0,
                "items": {
                    # shoppingcart
                    "bsonType": "array",
                    "minItems": 1,
                    "items": {
                        "bsonType": "object",
                        "required": [
                            "id_product",
                            "price_ET",
                            "quantity",
                            "rate_VAT",
                        ],
                        "properties": {
                            # commandline
                            "id_product": {"bsonType": "objectId"},
                            "price_ET": {
                                "bsonType": "double",
                                "minimum": 0.0,
                            },
                            "quantity": {
                                "bsonType": "int",
                                "minimum": 0,
                            },
                            "rate_VAT": {
                                "bsonType": "double",
                                "minimum": 0.0,
                            },
                        },
                    },
                    "description": "List contain all commandline of a shoppingcart",
                },
                "description": "List contain all shoppingcart of the user",
            },
        },
    }

    validator = {"$jsonSchema": schema}
    get_collection(validator)
    return validator


def create_users(validator: dict) -> None:
    """Create users

    Args:
        validator (dict): $jsonSchema: schema
    """
    # 1. Get 'User' collection
    collection = get_collection(validator)

    products_list = find_all_products()

    # 2. Insérer un document (INSERT MANY)
    new_users = [
        {
            "name": "Dupont",
            "firstname": "Paul",
            "email": "paul.dupont@generator.com",
            "password": "$2b$12$okUsS9JFZjXAJZYvbyTRfObd6YkVvfEXMSspN2LGO48l1MIoNBCNe",
            "birth_date": date.datetime(1992, 1, 13, 5, 45, 42),
            "connection": "timeout",
            "role": "user",
            "age": 33,
            "phone": "010203040506",
        },
        {
            "name": "Martin",
            "firstname": "Claire",
            "email": "claire.martin@generator.com",
            "password": "$2b$12$x3M8LUmxAWcYEZbGoLVlKOVcM1lG/Stz7w4oOES1q/aG5aKUU5QTS",
            "birth_date": date.datetime(1988, 7, 22, 5, 45, 42),
            "connection": "timeout",
            "role": "admin",
            "age": 37,
            "phone": "060102030405",
        },
    ]
    result_many = collection.insert_many(new_users)
    print("IDs inséré pour Paul Dupont & Claire Martin :", result_many.inserted_ids)


def find_user_id(name: str, firstname: str) -> ObjectId:
    """Find user id

    Args:
        name (str): user name
        firstname (str): user firstname

    Returns:
        ObjectId: User id
    """
    # 1. Connection to MongoDB
    client = MongoClient(cv.MONGODB_LOCAL_PATH)

    # 2. Access database and collection
    db = client[cv.MONGODB_NAME]
    collection = db[cv.USER_COLLECTION]

    # 3. Create filters and fields
    fields = {
        "_id": 1,
    }
    filter = {
        "name": name,
        "firstname": firstname,
    }

    # 4. Use find() with filter : get the user
    user_id = [doc["_id"] for doc in collection.find(filter, fields)]
    return user_id[0]


def find_all_products() -> list:
    """Find all products

    Returns:
        list: list of all products
    """
    # 1. Connection to MongoDB
    client = MongoClient(cv.MONGODB_LOCAL_PATH)

    # 2. Access database and collection
    db = client[cv.MONGODB_NAME]
    collection = db[cv.PRODUCT_COLLECTION]

    # 3. Create filters and fields
    fields = {
        "_id": 1,
        "price_ET": 1,
        "number_of_units": 1,
        "rate_vat": 1,
    }
    filter = {}

    # 4. Use find() without filter : get all products
    products = collection.find(filter, fields)

    # 5. Create list
    product_list = []
    for doc in products:
        product_dict = {}
        product_dict["_id"] = doc["_id"]
        product_dict["price_ET"] = doc["price_ET"]
        product_dict["number_of_units"] = doc["number_of_units"]
        product_dict["rate_vat"] = doc["rate_vat"]
        product_list.append(product_dict)

    return product_list


def find_random_products() -> list:
    """Find a random product on a list

    Returns:
        list: list of random products
    """
    return random.sample(find_all_products(), k=3)


def create_shoppingcart() -> dict:
    """Create shoppingcart

    Returns:
        dict: new shoppingcart
    """
    # 1. Get random products
    product_list = find_random_products()

    # 2. Create shoppingcart
    new_shoppingcart = []

    for product in product_list:
        # 3. Create commandline
        commandline = {}
        commandline["id_product"] = product["_id"]
        commandline["price_ET"] = product["price_ET"]
        commandline["quantity"] = random.randint(0, product["number_of_units"])
        commandline["rate_VAT"] = product["rate_vat"]
        new_shoppingcart.append(commandline)

    return new_shoppingcart


def insert_shoppingcart(id_user: ObjectId) -> None:
    """Insert shoppingcart

    Args:
        id_user (ObjectId): user id
    """
    # 1. Connection to MongoDB
    client = MongoClient(cv.MONGODB_LOCAL_PATH)

    # 2. Access database and collection
    db = client[cv.MONGODB_NAME]
    collection = db[cv.USER_COLLECTION]

    # 3. Create filters and fields
    # Add new shoppingcart at the end of the list shoppingcarts
    fields = {
        "$push": {"shoppingcarts": create_shoppingcart()},
    }
    filter = {
        "_id": id_user,
    }

    # 4. Update User: id_user
    collection.update_one(filter, fields)

    print(f"Insertion d'un panier pour l'utilisateur : {id_user}")


def main():
    pass
    # generate_password()
    validator = create_schema_user()
    create_users(validator)
    insert_shoppingcart(find_user_id("Dupont", "Paul"))
    insert_shoppingcart(find_user_id("Martin", "Claire"))


if __name__ == "__main__":
    main()

from pymongo import MongoClient
from pymongo.collection import Collection
from bson.objectid import ObjectId
import sys
import os
import bcrypt
import datetime as date

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
# Add parent folder au sys.path
import const_values as cv


def generate_password() -> str:
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
    # 1. Get 'User' collection
    collection = get_collection(validator)

    products_list = find_product()

    # 2. Insérer un document (INSERT ONE)
    result_one = collection.insert_one(
        {
            "name": "Dupont",
            "firstname": "Paul",
            "email": "paul.dupont@generator.com",
            "password": "$2b$12$ZqRrJY6w4seDPYtsuSD69u73YCjLMgDwTduM9VV7YcINcQOi.trSi",
            "birth_date": date.datetime(1992, 1, 13, 5, 45, 42),
            "connection": "timeout",
            "role": "user",
            "age": 33,
            "phone": "010203040506",
            "shoppingcarts": [
                [
                    {
                        "id_product": ObjectId("6836bd824d83684c0652079e"),
                        "price_ET": 899.99,
                        "quantity": 1,
                        "rate_VAT": 0.2,
                    },
                    {
                        "id_product": ObjectId("6836bd824d83684c0652079e"),
                        "price_ET": 749.99,
                        "quantity": 4,
                        "rate_VAT": 0.2,
                    },
                ],
            ],
        }
    )
    print("ID inséré pour Paul Dupont :", result_one.inserted_id)


def find_product():
    pass


def main():
    # generate_password()
    validator = create_schema_user()
    create_users(validator)


if __name__ == "__main__":
    main()

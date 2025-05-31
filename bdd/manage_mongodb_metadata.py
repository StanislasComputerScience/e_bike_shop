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


def get_collection(validator: dict) -> Collection:
    """Get collection 'Metadata'

    Args:
        validator (dict): contain jsonSchema

    Returns:
        Collection: 'Metadata' collection
    """

    # 1. Connection
    client = MongoClient(cv.MONGODB_LOCAL_PATH)
    db = client[cv.MONGODB_NAME]

    # Check if table Metadata exist
    try:
        # 2. Création de la collection avec validation
        collection = db.create_collection("Metadata", validator=validator)
    except:
        db.Metadata.drop()
        # 2. Création de la collection avec validation
        collection = db.create_collection("Metadata", validator=validator)

    return collection


def create_schema_metadata() -> dict:
    """Create schema collection 'Metadata'

    Returns:
        dict: $jsonSchema: schema
    """
    # 1. Définition du schéma
    schema = {
        "bsonType": "object",
        "properties": {
            "vat": {
                "bsonType": "array",
                "items": {
                    "bsonType": "object",
                    "required": [
                        "name",
                        "rate",
                    ],
                    "properties": {
                        "name": {
                            "bsonType": "string",
                        },
                        "rate": {
                            "bsonType": "double",
                            "minimum": 0.0,
                        },
                    },
                },
                "description": "List contain all vat",
            },
            "category": {
                "bsonType": "array",
                "items": {
                    "bsonType": "object",
                    "required": [
                        "name",
                    ],
                    "properties": {
                        "name": {
                            "bsonType": "string",
                        },
                    },
                },
                "description": "List contain all category",
            },
            "role": {
                "bsonType": "array",
                "items": {
                    "bsonType": "object",
                    "required": [
                        "name",
                    ],
                    "properties": {
                        "name": {
                            "bsonType": "string",
                        },
                    },
                },
                "description": "List contain all role",
            },
        },
    }

    validator = {"$jsonSchema": schema}
    get_collection(validator)
    return validator


def create_metadata(validator: dict) -> None:
    """Create metadata

    Args:
        validator (dict): $jsonSchema: schema
    """
    # 1. Get 'Metadata' collection
    collection = get_collection(validator)

    # 2. Insérer un document (INSERT MANY)
    new_metadata = dict(
        {
            "vat": [
                {"name": "french (standard)", "rate": 0.2},
            ],
            "category": [
                {
                    "name": "bike",
                },
                {
                    "name": "accessory",
                },
            ],
            "role": [
                {
                    "name": "user",
                },
                {
                    "name": "admin",
                },
            ],
        },
    )
    result_one = collection.insert_one(new_metadata)
    print("METADATA inséré :", result_one.inserted_id)


def main():
    pass
    validator = create_schema_metadata()
    create_metadata(validator)


if __name__ == "__main__":
    main()

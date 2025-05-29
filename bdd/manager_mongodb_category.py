from pymongo import MongoClient
from pymongo.collection import Collection
from bson.objectid import ObjectId
import sys
import os
import datetime as date

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
# Add parent folder au sys.path
import const_values as cv


def get_collection(validator: dict) -> Collection:
    """Get collection 'Category'

    Args:
        validator (dict): contain jsonSchema

    Returns:
        Collection: 'Category' collection
    """

    # 1. Connection
    client = MongoClient(cv.MONGODB_LOCAL_PATH)
    db = client[cv.MONGODB_NAME]

    # Check if table VAT exist
    try:
        # 2. Création de la collection avec validation
        collection = db.create_collection(cv.CATEGORY_COLLECTION, validator=validator)
    except:
        db.Category.drop()
        # 2. Création de la collection avec validation
        collection = db.create_collection(cv.CATEGORY_COLLECTION, validator=validator)

    return collection


def create_schema_category() -> dict:
    """Create schema collection 'Category'

    Returns:
        dict: $jsonSchema: schema
    """
    # 1. Définition du schéma
    schema = {
        "bsonType": "object",
        "required": [
            "name",
        ],
        "properties": {
            "name": {
                "bsonType": "string",
            },
        },
    }

    validator = {"$jsonSchema": schema}
    get_collection(validator)
    return validator


def create_category(validator: dict) -> None:
    """Create category

    Args:
        validator (dict): $jsonSchema: schema
    """
    # 1. Get 'User' collection
    collection = get_collection(validator)

    # 2. Insérer un document (INSERT MANY)
    new_category = [
        {
            "name": "bike",
        },
        {
            "name": "accessory",
        },
    ]
    result_many = collection.insert_many(new_category)
    print("IDs inséré pour bike et accessory :", result_many.inserted_ids)


def main():
    pass
    # generate_password()
    validator = create_schema_category()
    create_category(validator)


if __name__ == "__main__":
    main()

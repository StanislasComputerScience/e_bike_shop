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
    """Get collection 'VAT'

    Args:
        validator (dict): contain jsonSchema

    Returns:
        Collection: 'VAT' collection
    """

    # 1. Connection
    client = MongoClient(cv.MONGODB_LOCAL_PATH)
    db = client[cv.MONGODB_NAME]

    # Check if table VAT exist
    try:
        # 2. Création de la collection avec validation
        collection = db.create_collection(cv.VAT_COLLECTION, validator=validator)
    except:
        db.VAT.drop()
        # 2. Création de la collection avec validation
        collection = db.create_collection(cv.VAT_COLLECTION, validator=validator)

    return collection


def create_schema_vat() -> dict:
    """Create schema collection 'VAT'

    Returns:
        dict: $jsonSchema: schema
    """
    # 1. Définition du schéma
    schema = {
        "bsonType": "object",
        "required": [
            "name",
            "rate",
        ],
        "properties": {
            "name": {
                "bsonType": "string",
            },
            "age": {
                "bsonType": "double",
                "minimum": 0.0,
            },
        },
    }

    validator = {"$jsonSchema": schema}
    get_collection(validator)
    return validator


def create_vat(validator: dict) -> None:
    """Create category

    Args:
        validator (dict): $jsonSchema: schema
    """
    # 1. Get 'User' collection
    collection = get_collection(validator)

    # 2. Insérer un document (INSERT MANY)
    new_category = {
        "name": "french (standard)",
        "rate": 0.2,
    }
    result_one = collection.insert_one(new_category)
    print("ID inséré pour french (standard) :", result_one.inserted_id)


def main():
    pass
    # generate_password()
    validator = create_schema_vat()
    create_vat(validator)


if __name__ == "__main__":
    main()

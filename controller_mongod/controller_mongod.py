from pymongo import MongoClient
from pymongo.database import Database
from pymongo.collection import Collection
from bson.objectid import ObjectId
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
# Add parent folder au sys.path
import const_values as cv


# region Collection connect
def connect_to_collection(name_collection: str) -> Collection:
    # 1. Connection to MongoDB
    client = MongoClient(cv.MONGODB_LOCAL_PATH)

    # 2. Access database and collection
    db = client[cv.MONGODB_NAME]
    collection = db[name_collection]

    return collection


def connect_to_mongodb() -> Database:
    """Connect to the mongodb database and return its content

    Returns:
        Database: Content of the database
    """

    client = MongoClient("mongodb://localhost:27017/")
    db = client["ecommerce_database"]
    return db


def product_catalog() -> list[dict]:
    """Returns the list of products in the catalogue,
    and most of the associated information

    Returns:
        list[dict]: list of all product
    """

    db = connect_to_mongodb()
    fields = [
        "name",
        "description",
        "tech_specification",
        "image_path",
        "price_ET",
        "rate_vat",
    ]
    products = [doc for doc in db.Product.find(projection=fields)]

    count = 0
    for product in products:
        count += 1
        product["id_prod"] = count
        product["price_it"] = product["price_ET"] * (1 + product["rate_vat"])

    return products


# region Connection
def get_user_info_connect(user_email: str) -> list[dict]:
    """Get the user information

    Args:
        user_email (str): user email

    Returns:
        list[dict]: user information
    """
    # 1. Connect to collection
    collection = connect_to_collection(cv.USER_COLLECTION)

    # 2. Create filters and fields
    fields = {
        "_id": 1,
        "password": 1,
    }
    filter = {
        "email": user_email,
    }

    # 3. Use find() with filter : get the user
    user_info = collection.find(filter, fields)
    user_info_list = []

    for user in user_info:
        dict_temp = {}
        dict_temp["id_user"] = user["_id"]
        dict_temp["password"] = user["password"]
        user_info_list.append(dict_temp)
    return user_info_list


# User is validated
def connect_user(id_user: ObjectId) -> None:
    """Update the user connection

    Args:
        id_user (ObjectId): user id
    """
    # 1. Connect to collection
    collection = connect_to_collection(cv.USER_COLLECTION)

    # 2. Create filters and fields
    fields = {
        "$set": {"connection": "connected"},
    }
    filter = {
        "_id": id_user,
    }

    # 3. Update User: connection
    collection.update_one(filter, fields)


def disconnect_user(id_user: ObjectId) -> None:
    """Update the user connection

    Args:
        id_user (ObjectId): user id
    """
    # 1. Connect to collection
    collection = connect_to_collection(cv.USER_COLLECTION)

    # 2. Create filters and fields
    fields = {
        "$set": {"connection": "timeout"},
    }
    filter = {
        "_id": id_user,
    }

    # 3. Update User: connection
    collection.update_one(filter, fields)


def main():
    pass
    # products = product_catalog()
    # for product in products:
    #     print(product)
    # get_user_info_connect("paul.dupont@generator.com")
    # connect_user(ObjectId("683705696b9ec1d18895d51d"))


if __name__ == "__main__":
    main()

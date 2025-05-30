from pymongo import MongoClient
from pymongo.database import Database
from pymongo.collection import Collection
from bson.objectid import ObjectId
import sys
import os
import datetime as dt

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
# Add parent folder at the sys.path
import const_values as cv


# region Collection connect
def connect_to_mongodb() -> Database:
    """Connect to the mongodb database and return its content

    Returns:
        Database: Content of the database
    """

    client = MongoClient(cv.MONGODB_LOCAL_PATH)
    db = client[cv.MONGODB_NAME]
    return db


def connect_to_collection(name_collection: str) -> Collection:
    """Return a specific collection in the database

    Args:
        name_collection (str): Name of the collection

    Returns:
        Collection: Collection content
    """
    db = connect_to_mongodb()
    collection = db[name_collection]

    return collection


# region Catalogue & Mosaique
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


# region Panier & Commande
# Shopping cart id
def user_open_shopping_cart_id(id_user: ObjectId) -> tuple[ObjectId, int] | None:
    """Return the index of the latest opened shopping cart
    associated to the user with id id_user. An opened shopping cart
    is a shopping cart that is stored in a document of the collection
    User.

    Args:
        id_user (ObjectId): User Id

    Returns:
        int: Index of the shopping cart in the list of the user's shopping carts
    """

    # Connection
    db = connect_to_mongodb()

    # Request
    fields = {"_id": False, "shoppingcarts": True}
    filter = {"_id": id_user}
    response = [doc for doc in db.User.find(filter=filter, projection=fields)]

    # Result
    if response[0]:
        return (id_user, len(response[0]["shoppingcarts"]) - 1)
    else:
        return None


# Shopping cart
def user_shopping_cart(id_user_and_shoppingcart: tuple[ObjectId, int]) -> list[dict]:
    """Return information of a shopping cart of a user.
    Interrogate the database with the name ecommerce_db_name.

    Args:
        id_user_and_shoppingcart (tuple[ObjectId, int]): User Id and index of the shopping cart in its shopping cart list

    Returns:
        (list[dict]): list of shopping cart command lines to display
        on the page "Panier" or "Command".
    """

    # Connection
    db = connect_to_mongodb()

    # Split tuple
    id_user = id_user_and_shoppingcart[0]
    idx_shoppingcart = id_user_and_shoppingcart[1]

    # Request
    fields = {"_id": False, "shoppingcarts": True}
    filter = {"_id": id_user}
    response = [doc for doc in db.User.find(filter=filter, projection=fields)]

    if response[0]:
        # Get the shopping cart in the list
        shoppingcarts = response[0]["shoppingcarts"]
        try:
            shoppingcart = shoppingcarts[idx_shoppingcart]
        except:
            raise IndexError("Wrong index in the list of shopping carts.")

        fields = ["image_path", "name", "number_of_units"]
        count = 0
        for commandLine in shoppingcart:
            filter = {"_id": commandLine["id_product"]}
            response = [
                doc for doc in db.Product.find(filter=filter, projection=fields)
            ]

            try:
                product = response[0]
                commandLine["product_name"] = product["name"]
                commandLine["image_path"] = product["image_path"]
                commandLine["number_of_units"] = product["number_of_units"]
                commandLine["id_shoppingcart"] = id_user_and_shoppingcart
                commandLine["id_prod"] = product["_id"]

                count += 1
            except:
                raise Exception("Error...")

        return shoppingcart

    else:
        return list()


# Update command line
def update_command_line(
    id_prod: ObjectId, id_shoppingcart: tuple[ObjectId, int], new_quantity: int
) -> None:
    """Update the database to modify the
    quantity of the command line associated to id_prod for the user
    shopping cart identified by id_shoppingcart

    Args:
        id_prod (ObjectId): id of the product associated to the command line
        id_shoppingcart (tuple[ObjectId, int]): Id of the user and index of the shopping cart in its shopping cart list
        new_quantity (int): the new quantity
    """

    # Connection
    db = connect_to_mongodb()

    filter = {
        "_id": id_shoppingcart[0],
    }
    update = {
        "$set": {
            "shoppingcarts."
            + str(id_shoppingcart[1])
            + ".$[line].quantity": new_quantity
        }
    }
    array_filters = [{"line.id_product": id_prod}]
    db.User.update_one(filter=filter, update=update, array_filters=array_filters)


# Remove command line
def remove_command_line(
    id_prod: ObjectId, id_shoppingcart: tuple[ObjectId, int]
) -> None:
    """Remove in the database the command line associated with the product
    id_prod to the user shopping cart identified by the pair id_shoppingcart.

    Args:
        id_prod (int): id of the product
        id_shoppingcart (int): User id and the index of the shopping cart in its shopping cart list
    """

    # Connection
    db = connect_to_mongodb()

    fields = {"_id": False, "shoppingcarts": True}
    filter = {
        "_id": id_shoppingcart[0],
    }
    response = db.User.find_one(filter=filter, projection=fields)
    if response:
        count = 0
        for command_line in response["shoppingcarts"][id_shoppingcart[1]]:
            if command_line["id_product"] == id_prod:
                response["shoppingcarts"][id_shoppingcart[1]].pop(count)

            count += 1

        filter = {
            "_id": id_shoppingcart[0],
        }
        update = {"$set": {"shoppingcarts": response["shoppingcarts"]}}
        db.User.update_one(filter=filter, update=update)
    else:
        raise KeyError(
            f"No document with user Id {id_shoppingcart[0]} in collection User"
        )


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


# region Commande
def get_all_info_user(id_user: str) -> dict:
    """Get user information

    Args:
        id_user (str): user id

    Returns:
        dict: user information
    """
    # 1. Connect to collection
    collection = connect_to_collection(cv.USER_COLLECTION)

    # 2. Create filters and fields
    fields = {
        "name": 1,
        "firstname": 1,
        "email": 1,
        "phone": 1,
    }
    filter = {
        "_id": id_user,
    }

    # 3. Get User information
    user_info_list = []
    for user in collection.find(filter, fields):
        info = {}
        info["name"] = user["name"]
        info["firstname"] = user["firstname"]
        info["email"] = user["email"]
        info["phone"] = user["phone"]
        user_info_list.append(info)
    return user_info_list


def get_user_address(id_user: int) -> list[tuple]:
    """Get user address

    Args:
        id_user (int): user id

    Returns:
        list[tuple]: each tuple contain address: (street, city)
    """
    # 1. Connect to collection
    collection = connect_to_collection(cv.USER_COLLECTION)

    # 2. Create filters and fields
    fields = {
        "_id": 0,
        "address": 1,
    }
    filter = {
        "_id": id_user,
    }

    # 3. Get information
    user_address_collect = collection.find_one(filter, fields)
    user_address_list = user_address_collect["address"]

    user_info_list = []
    for user in user_address_list:
        info = (
            f"{user["number"]} {user["street"]}",
            f"{user["postal_code"]} {user["city"]}",
        )
        user_info_list.append(info)
    return user_info_list


def create_invoice(id_user: int) -> None:
    """Create invoice

    Args:
        id_user (int): user id
    """
    # 1. Connect to collection
    collection_user = connect_to_collection(cv.USER_COLLECTION)
    collection_invoice = connect_to_collection(cv.USER_COLLECTION)

    # 2. Create filters, fields and new_invoice{}
    _, id_shoppingcart = user_open_shopping_cart_id(id_user)

    # fields_user = {
    #     "_id": 0,
    #     f"shoppingcarts.{id_shoppingcart}": 1,
    # }
    # filter_user = {
    #     "_id": id_user,
    # }

    # # 3. Get information
    # result_one = collection_user.find_one(filter_user, fields_user)
    # result_many = result_one["shoppingcarts"]
    # for doc in result_many:
    #     print(doc)

    # 4. Create invoice
    today_date = dt.datetime.now()
    # new_invoice = {
    #     "date": today_date,
    #     "shoppingcart": ,
    # }


# region Admin
def is_admin(id_user: int) -> bool:
    """Verify if the user is admin

    Args:
        id_user (int): user id

    Returns:
        bool: condition if the user is admin
    """
    # 1. Connect to collection
    collection = connect_to_collection(cv.USER_COLLECTION)

    # 2. Create filters and fields
    fields = {
        "_id": 0,
        "role": 1,
    }
    filter = {
        "_id": id_user,
    }

    # 3. Get information
    user_role = [doc["role"] for doc in collection.find(filter, fields)]
    return "admin" in user_role


def create_new_product(
    name: str,
    choice_cat: str,
    number_of_units: int,
    description: str,
    tech_specification: str,
    price_ET: int,
    choice_vat: str,
    file_path: str,
) -> None:
    """Create new product

    Args:
        name (str): product name
        choice_cat (str): product category
        number_of_units (int): number of units
        description (str): product description
        tech_specification (str): product technical specification
        price_ET (int): price ET
        choice_vat (str): product vAT
        file_path (str): product picture file path
    """
    pass


def main():
    # products = product_catalog()
    # for product in products:
    #     print(product)

    id_user = "683970c434aa88b4792013f0"
    id_product = "683970c0b906f90c552d4b03"
    ids = user_open_shopping_cart_id(ObjectId(id_user))
    # print(user_open_shopping_cart_id(ObjectId(id_user)))
    # print(ids)
    # print(user_shopping_cart(ids))
    if ids:
        update_command_line(ObjectId(id_product), ids, 15)
        remove_command_line(ObjectId(id_product), ids)

    # products = product_catalog()
    # for product in products:
    #     print(product)
    # get_user_info_connect("paul.dupont@generator.com")
    # connect_user(ObjectId("683705696b9ec1d18895d51d"))
    # print(get_all_info_user(ObjectId("68371c28564b2590bf657cef")))
    # print(is_admin(ObjectId("68385cce9e2c02e0112976ca")))
    print(user_open_shopping_cart_id(ObjectId("683972d4934bfa48a1e9ce69")))


if __name__ == "__main__":
    main()

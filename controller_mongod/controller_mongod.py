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
def user_shopping_cart(id_shoppingcart: tuple[ObjectId, int]) -> list[dict]:
    """Return information of a shopping cart of a user.
    Interrogate the database with the name ecommerce_db_name.

    Args:
        id_shoppingcart (tuple[ObjectId, int]): User Id and index of the shopping cart in its shopping cart list

    Returns:
        (list[dict]): list of shopping cart command lines to display
        on the page "Panier" or "Command".
    """

    # Connection
    db = connect_to_mongodb()

    # Request
    fields = {"_id": False, "shoppingcarts": True}
    filter = {"_id": id_shoppingcart[0]}
    response = [doc for doc in db.User.find(filter=filter, projection=fields)]

    if response[0]:
        # Get the shopping cart in the list
        shoppingcarts = response[0]["shoppingcarts"]
        try:
            shoppingcart = shoppingcarts[id_shoppingcart[1]]
        except:
            raise IndexError("Wrong index in the list of shopping carts.")

        fields = ["image_path", "name", "number_of_units"]
        for commandLine in shoppingcart:
            filter = {"_id": commandLine["id_product"]}
            response = [
                doc for doc in db.Product.find(filter=filter, projection=fields)
            ]

            try:
                product = response[0]
                commandLine["name"] = product["name"]
                commandLine["image_path"] = product["image_path"]
                commandLine["number_of_units"] = product["number_of_units"]
                commandLine["id_shoppingcart"] = id_shoppingcart
            except:
                raise Exception("Error...")

        # TODO: Should add a shopping cart date
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
    response = [doc for doc in db.User.find(filter=filter, projection=fields)]
    # TODO find_one permet de supprimer les [0]
    count = 0
    for command_line in response[0]["shoppingcarts"][id_shoppingcart[1]]:
        if command_line["id_product"] == id_prod:
            response[0]["shoppingcarts"][id_shoppingcart[1]].pop(count)

        count += 1

    filter = {
        "_id": id_shoppingcart[0],
    }
    update = {"$set": {"shoppingcarts": response[0]["shoppingcarts"]}}
    db.User.update_one(filter=filter, update=update)


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
    # products = product_catalog()
    # for product in products:
    #     print(product)

    id_user = "683968d120a2a1c3a8a8a911"
    id_product = "683966affa3736d5110d1519"
    ids = user_open_shopping_cart_id(ObjectId(id_user))
    # print(user_open_shopping_cart_id(ObjectId(id_user)))
    # print(ids)
    # print(user_shopping_cart(ids))
    update_command_line(ObjectId(id_product), ids, 15)
    remove_command_line(ObjectId(id_product), ids)

    # products = product_catalog()
    # for product in products:
    #     print(product)
    # get_user_info_connect("paul.dupont@generator.com")
    # connect_user(ObjectId("683705696b9ec1d18895d51d"))


if __name__ == "__main__":
    main()

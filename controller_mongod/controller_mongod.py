from pymongo import MongoClient
from pymongo.database import Database
from bson.objectid import ObjectId


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


# region Panier & Commande
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
        return (id_user, len(response[0]["shoppingcarts"])-1)
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
        
        fields = [
            "image_path",
            "name",
            "number_of_units"
        ]
        for commandLine in shoppingcart:
            filter = {"_id": commandLine["id_product"]}
            response = [doc for doc in db.Product.find(filter=filter, projection=fields)]

            try:
                product = response[0]
                commandLine["name"] = product["name"]
                commandLine["image_path"] = product["image_path"]
                commandLine["number_of_units"] = product["number_of_units"]          
            except:
                raise Exception("Error...")
            
        # TODO: Should add a shopping cart date
        return shoppingcart

    else:
        return list()


def test():
    # products = product_catalog()
    # for product in products:
    #     print(product)

    ids = user_open_shopping_cart_id(ObjectId("683703f4815f01c742a4ef96"))
    user_shopping_cart(ids)

#    print(user_open_shopping_cart_id(ObjectId("683703f4815f01c742a4ef97")))


if __name__ == "__main__":
    test()

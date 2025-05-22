import sqlite3


def user_shopping_cart(
    ecommerce_db_name: str, id_user: int
) -> list[dict[str, str, int, float, float, str]]:
    """Return information of the user shopping cart.
    Interrogate the database with the name ecommerce_db_name

    Args:
        ecommerce_db_name (str): name of the database
        id_user (int): id of the user

    Returns:
        (list[dict[str, str, int, float, float, str]]): result of the request
    """

    with sqlite3.connect(f"{ecommerce_db_name}.db") as connexion:
        cursor = connexion.cursor()

        query = cursor.execute(
            """ SELECT
                    prod.image_path,
                    prod.name,
                    cl.quantity,
                    cl.price_ET,
                    cl.rate_vat,
                    cart.date
                FROM CommandLine as cl
                LEFT JOIN ShoppingCart as cart
                ON cart.id_shoppingcart = cl.id_shoppingcart
                LEFT JOIN Product as prod
                ON prod.id_prod = cl.id_prod
                WHERE cart.id_user = (:id_user)
                ;
            """,
            {"id_user": id_user},
        )

        # Convert tuple into dictionnary
        shopping_cart = []
        for command_line in query.fetchall():
            command_line_as_dict = dict()
            command_line_as_dict["image_path"] = command_line[0]
            command_line_as_dict["product_name"] = command_line[1]
            command_line_as_dict["quantity"] = command_line[2]
            command_line_as_dict["price_ET"] = command_line[3]
            command_line_as_dict["rate_vat"] = command_line[4]
            command_line_as_dict["date"] = command_line[5]
            shopping_cart.append(command_line_as_dict)

        return shopping_cart


if __name__ == "__main__":
    for i in range(3):
        for info in user_shopping_cart("ecommerce_database", i + 1):
            print(info)
        print()

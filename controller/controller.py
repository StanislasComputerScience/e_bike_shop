import sqlite3


def user_shopping_cart(
    ecommerce_db_name: str, id_user: int
) -> list[tuple[str, str, int, float, float, str]]:
    """Return information of the user shopping cart.
    Interrogate the database with the name ecommerce_db_name

    Args:
        ecommerce_db_name (str): name of the database
        id_user (int): id of the user

    Returns:
        (list[tuple[str, str, int, float, float, str]]): result of the request
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
        return query.fetchall()


if __name__ == "__main__":
    for i in range(3):
        for info in user_shopping_cart("ecommerce_database", i + 1):
            print(info)
        print()

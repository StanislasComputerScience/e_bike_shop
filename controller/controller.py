import sqlite3


# region Home
# Most 2 popular products
def most_popular_products(ecommerce_db_name: str) -> list[dict]:
    """Most popular products

    Args:
        ecommerce_db_name (str): database name

    Returns:
        list[dict]: list of product most popular
    """
    with sqlite3.connect(f"bdd/{ecommerce_db_name}.db") as connexion:
        cursor = connexion.cursor()

        query = cursor.execute(
            """SELECT prod.name,
                      prod.image_path
               FROM Product as prod
               ORDER BY prod.popularity DESC
               LIMIT 2;
            """
        )
        product_list = []
        for prod_info in query.fetchall():
            dict_temp = {}
            dict_temp["name"] = prod_info[0]
            dict_temp["image_path"] = prod_info[1]
            product_list.append(dict_temp)
        return product_list


# Most 2 products buy
def most_products_buy(ecommerce_db_name: str) -> list[dict]:
    """Most buy products

    Args:
        ecommerce_db_name (str): database name

    Returns:
        list[dict]: list of product most popular
    """
    with sqlite3.connect(f"bdd/{ecommerce_db_name}.db") as connexion:
        cursor = connexion.cursor()

        query = cursor.execute(
            """SELECT prod.name,
                      prod.image_path
               FROM Product as prod 
               RIGHT JOIN (SELECT cl.id_prod, 
                                SUM(cl.quantity) as number_sale,
                                ROUND(SUM(cl.quantity) * SUM(cl.price_ET),2) as total_price_product_sale
                            FROM CommandLine as cl
                            RIGHT JOIN ShoppingCart as sc on sc.id_shoppingcart = cl.id_shoppingcart
                            RIGHT JOIN Invoice as inv on inv.id_invoice = sc.id_shoppingcart
                            GROUP BY cl.id_prod) as prod_sale on prod_sale.id_prod = prod.id_prod
               ORDER BY prod_sale.number_sale DESC, prod_sale.total_price_product_sale DESC
               LIMIT 2;
            """
        )
        product_list = []
        for prod_info in query.fetchall():
            dict_temp = {}
            dict_temp["name"] = prod_info[0]
            dict_temp["image_path"] = prod_info[1]
            product_list.append(dict_temp)
        return product_list


# region Connection
# Get id_user
def get_user_info(ecommerce_db_name: str, user_email: str) -> list[dict]:
    """Get the user information

    Args:
        ecommerce_db_name (str): database name
        user_email (str): user email

    Returns:
        list[dict]: user information
    """
    with sqlite3.connect(f"bdd/{ecommerce_db_name}.db") as connexion:
        cursor = connexion.cursor()

        query = cursor.execute(
            """SELECT u.id_user, u.password
                FROM User as u
                WHERE u.email = (:email)
               ;
            """,
            {"email": user_email},
        )
        user_info_list = []
        for prod_info in query.fetchall():
            dict_temp = {}
            dict_temp["id_user"] = prod_info[0]
            dict_temp["password"] = prod_info[1]
            user_info_list.append(dict_temp)
        return user_info_list


# User is validated
def connect_user(ecommerce_db_name: str, id_user: str) -> None:
    with sqlite3.connect(f"bdd/{ecommerce_db_name}.db") as connexion:
        cursor = connexion.cursor()

        query = cursor.execute(
            """UPDATE User
                SET id_connection = (SELECT con.id_connection 
                                     FROM Connection as con 
                                     WHERE con.status = 'connected')
                WHERE id_user = (:id_user)
                ;
            """,
            {"id_user": id_user},
        )


def deconnect_user(ecommerce_db_name: str, id_user: str) -> None:
    with sqlite3.connect(f"bdd/{ecommerce_db_name}.db") as connexion:
        cursor = connexion.cursor()

        query = cursor.execute(
            """UPDATE User
                SET id_connection = (SELECT con.id_connection 
                                     FROM Connection as con 
                                     WHERE con.status = 'timeout')
                WHERE id_user = (:id_user)
                ;
            """,
            {"id_user": id_user},
        )


def main():
    db_name = "ecommerce_database"
    user_info = get_user_info(db_name, "paul.dupont@generator.com")
    print(user_info)


if __name__ == "__main__":
    main()

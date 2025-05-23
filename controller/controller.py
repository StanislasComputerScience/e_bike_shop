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
        list_product = []
        for prod_info in query.fetchall():
            dict_temp = {}
            dict_temp["name"] = prod_info[0]
            dict_temp["image_path"] = prod_info[1]
            list_product.append(dict_temp)
        return list_product


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
        list_product = []
        for prod_info in query.fetchall():
            dict_temp = {}
            dict_temp["name"] = prod_info[0]
            dict_temp["image_path"] = prod_info[1]
            list_product.append(dict_temp)
        return list_product
    
# region Panier
# Shopping cart
def user_shopping_cart(
    ecommerce_db_name: str, id_user: int
) -> list[dict]:
    """Return information of the user shopping cart.
    Interrogate the database with the name ecommerce_db_name

    Args:
        ecommerce_db_name (str): database name
        id_user (int): id of the user

    Returns:
        (list[dict]): list of shopping cart command lines to display
        on the page "Panier".
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


def main():
    db_name = "ecommerce_database"

    # Test most_popular_products
    list_product = most_popular_products(db_name)
    print(f"list_product= {list_product}")

    # Test user_shopping_cart
    for i in range(3):
        for info in user_shopping_cart(db_name, i + 1):
            print(info)
        print()


if __name__ == "__main__":
    main()

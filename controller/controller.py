import sqlite3
from datetime import datetime


def execute_sql_query(query, params=()):
    try:
        with sqlite3.connect("./bdd/ecommerce_database.db") as connexion:
            cursor = connexion.cursor()
            cursor.execute(query, params)
            result = cursor.fetchall()
            connexion.commit()
            return result
    except sqlite3.Error as e:
        print(f"Erreur SQL : {e}")
        return None


def product_catalog():
    query = """
        SELECT p.id_prod, p.name, p.description, p.tech_specification,
               p.image_path, p.price_ET * (1 + v.rate) AS price_it, p.price_ET as price_et
        FROM Product p
        INNER JOIN VAT v ON v.id_vat = p.id_vat
    """
    params = ()
    result = execute_sql_query(query, params)

    if result:
        fields = [
            "id_prod",
            "name",
            "description",
            "tech_specification",
            "image_path",
            "price_it",
            "price_ET",
        ]

        # Transformation result into a dictionnary
        return [dict(zip(fields, row)) for row in result]


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
def get_user_info_connect(ecommerce_db_name: str, user_email: str) -> list[dict]:
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


def disconnect_user(ecommerce_db_name: str, id_user: str) -> None:
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


# region Invoice
def get_all_info_user(ecommerce_db_name: str, id_user: str) -> dict:
    with sqlite3.connect(f"bdd/{ecommerce_db_name}.db") as connexion:
        cursor = connexion.cursor()

        query = cursor.execute(
            """SELECT u.name, u.firstname, u.email, u.phone
                FROM User as u
                WHERE id_user = (:id_user)
                ;
            """,
            {"id_user": id_user},
        )
        user_info_dict = {}
        for prod_info in query.fetchall():
            user_info_dict["name"] = prod_info[0]
            user_info_dict["firstname"] = prod_info[1]
            user_info_dict["email"] = prod_info[2]
            user_info_dict["phone"] = prod_info[3]
        return user_info_dict


# region Panier & Commande
def user_open_shopping_cart_id(ecommerce_db_name: str, id_user: int) -> int | None:
    """Return the id_shoppingcart of the latest opened shopping cart
    associated to the user with id id_user. An opened shopping cart
    is a shopping cart that does not have an invoice yet.

    Args:
        ecommerce_db_name (str): Database name
        id_user (int): User Id

    Returns:
        int: Shopping cart Id
    """
    query = f"""SELECT
                    MAX(id_shoppingcart) as max_id_shoppingcart
                FROM ShoppingCart
                WHERE id_invoice IS NULL AND
                      id_user = {id_user};
            """

    params = ()
    result = execute_sql_query(query, params)
    print(result)
    print(type(result))

    if result:
        return result[0][0]
    else:
        return None


# Shopping cart
def user_shopping_cart(ecommerce_db_name: str, id_shoppingcart: int) -> list[dict]:
    """Return information of a shopping cart.
    Interrogate the database with the name ecommerce_db_name.

    Args:
        ecommerce_db_name (str): database name
        id_shoppingcart (int): shopping cart id

    Returns:
        (list[dict]): list of shopping cart command lines to display
        on the page "Panier" or "Command".
    """

    query = f"""SELECT 
                    cl.id_prod,
                    cl.id_shoppingcart,
                    prod.image_path,
                    prod.name,
                    prod.number_of_units,
                    cl.quantity,
                    cl.price_ET,
                    cl.rate_vat,
                    cart.date
                FROM CommandLine as cl
                LEFT JOIN Product as prod
                ON prod.id_prod = cl.id_prod
                LEFT JOIN ShoppingCart as cart
                ON cart.id_shoppingcart = cl.id_shoppingcart
                WHERE cl.id_shoppingcart = {id_shoppingcart};
            """
    params = ()
    result = execute_sql_query(query, params)

    if result:
        fields = [
            "id_prod",
            "id_shoppingcart",
            "image_path",
            "product_name",
            "number_of_units",
            "quantity",
            "price_ET",
            "rate_vat",
            "date",
        ]

        # Transformation result into a dictionnary
        return [dict(zip(fields, row)) for row in result]
    else:
        return list()


# Update command line
def update_command_line(
    ecommerce_db_name: str, id_prod: int, id_shoppingcart: int, new_quantity: int
):
    """Update the database with the name ecommerce_db_name to modify the
    quantity of the entry with primary key id_prod, id_shopingcart

    Args:
        ecommerce_db_name (str): database name
        id_prod (int): id of the product
        id_shoppingcart (int): id of the shoppingcart
        new_quantity (int): the new quantity
    """

    with sqlite3.connect(f"bdd/{ecommerce_db_name}.db") as connexion:
        cursor = connexion.cursor()

        query = cursor.execute(
            """UPDATE CommandLine
                SET quantity = (:new_quantity)
                WHERE id_prod = (:id_prod) AND id_shoppingcart = (:id_shoppingcart);
            """,
            {
                "new_quantity": new_quantity,
                "id_prod": id_prod,
                "id_shoppingcart": id_shoppingcart,
            },
        )


# region Commande


def get_user_address(id_user: int) -> list[tuple]:
    query = f"""SELECT
                    number,
                    street,
                    postal_code,
                    city
                FROM Address
                WHERE id_user = {id_user};
            """

    params = ()
    result = execute_sql_query(query, params)
    final_result = []
    for result_tuple in result:
        temp_result = (
            f"{result_tuple[0]} {result_tuple[1]}",
            f"{result_tuple[2]} {result_tuple[3]}",
        )
        final_result.append(temp_result)
    return final_result


# pour améliorer la facturation, créer une clé étrangère dans invoice: id_address
def create_invoice(ecommerce_db_name: str, id_user: int) -> None:
    id_shoppingcart = user_open_shopping_cart_id(ecommerce_db_name, id_user)
    today_date = datetime.now().strftime("%d/%m/%Y")
    query = f"""INSERT INTO Invoice(id_shoppingcart, date)
                VALUES({id_shoppingcart},'{today_date}');
            """

    params = ()
    execute_sql_query(query, params)
    update_shoppingcart(id_shoppingcart)


def update_shoppingcart(id_shoppingcart: int) -> None:
    query = f"""UPDATE ShoppingCart
                SET id_invoice = (SELECT inv.id_invoice
                                  FROM ShoppingCart as sc
                                  LEFT JOIN Invoice as inv on inv.id_shoppingcart = sc.id_shoppingcart
                                  WHERE sc.id_shoppingcart = {id_shoppingcart});
            """
    params = ()
    execute_sql_query(query, params)


def main():
    db_name = "ecommerce_database"

    # # Test user_shopping_cart
    # for i in range(3):
    #     for info in user_shopping_cart(db_name, i + 1):
    #         print(info)
    #     print()

    # get_user_address(1)


if __name__ == "__main__":
    main()

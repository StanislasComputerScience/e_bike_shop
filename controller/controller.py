import sqlite3
from datetime import datetime
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import const_values as cv


def execute_sql_query(query: str, params=()) -> list[tuple] | None:
    """Function to execute sql query

    Args:
        query (str): sql query
        params (tuple, optional): parameters. Defaults to ().

    Returns:
        list[tuple]: query result
    """
    try:
        with sqlite3.connect(cv.bdd_path) as connexion:
            cursor = connexion.cursor()
            cursor.execute(query, params)
            result = cursor.fetchall()
            connexion.commit()
            return result
    except sqlite3.Error as e:
        print(f"Erreur SQL : {e}")
        return None


def product_catalog() -> list[dict] | None:
    """Function to execute sql query

    Args:
        query (str): sql query
        params (tuple, optional): parameters. Defaults to ().

    Returns:
        list[dict]: list of all product
    """
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
    else:
        return None


def is_command_line_exist(id_shoppingcart: int, id_prod: int) -> bool:
    """Return True id the command line with primary key (id_shoppingcart, id_prod)
    is present in the table CommandLine

    Args:
        id_shopping_cart (int): Id of the shoppingcart
        id_prod (int): Id of the products"""
    query = """
            SELECT com.id_shoppingcart,
                   com.id_prod
            FROM CommandLine com
            WHERE com.id_shoppingcart = ? AND com.id_prod = ?;
        """
    params = (id_shoppingcart, id_prod)
    result = execute_sql_query(query, params)
    return not result == []


def add_new_command_line(
    id_prod: int, id_shoppingcart: int, price: float, rate_vat: float
) -> None:
    """Add a new entry in the table CommandLine corresponding to
    the id_prod and id_shoppingcart

    Args:
        id_prod (int): Id of the products
        id_shopping_cart (int): Id of the shoppingcart
    """
    query = f"""INSERT INTO CommandLine (id_prod, id_shoppingcart, price_ET, quantity, rate_vat)
                VALUES ({id_prod},{id_shoppingcart},{price:.2f}, 1, {rate_vat:.1f})
    """
    params = ()
    execute_sql_query(query, params)


def add_new_shoppingcart(id_user: int) -> None:
    """Add a new shopping cart in the table ShoppingCart corresponding to
    the user with id_user

    Args:
        id_user (int): Id of the user
    """
    today_date = datetime.now().strftime("%d/%m/%Y")
    query = f"""INSERT INTO ShoppingCart (id_user, date)
                VALUES ({id_user},'{today_date}');
            """

    params = ()
    execute_sql_query(query, params)


# region Home
def most_popular_products() -> list[dict]:
    """Most 2 popular products

    Args:
        No args

    Returns:
        list[dict]: list of product most popular
    """
    query = f"""SELECT prod.name,
                    prod.image_path
            FROM Product as prod
            ORDER BY prod.popularity DESC
            LIMIT 2;"""
    params = ()
    result = execute_sql_query(query, params)
    product_list = []
    for prod_info in result:
        dict_temp = {}
        dict_temp["name"] = prod_info[0]
        dict_temp["image_path"] = prod_info[1]
        product_list.append(dict_temp)
    return product_list


def most_products_buy() -> list[dict]:
    """Most 2 buy products

    Args:
        No args

    Returns:
        list[dict]: list of product most popular
    """
    query = f"""SELECT prod.name,
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
            LIMIT 2;"""
    params = ()
    result = execute_sql_query(query, params)
    product_list = []
    for prod_info in result:
        dict_temp = {}
        dict_temp["name"] = prod_info[0]
        dict_temp["image_path"] = prod_info[1]
        product_list.append(dict_temp)
    return product_list


# region Connection
def get_user_info_connect(user_email: str) -> list[dict]:
    """Get the user information

    Args:
        user_email (str): user email

    Returns:
        list[dict]: user information
    """
    query = f"""SELECT u.id_user, u.password
            FROM User as u
            WHERE u.email = '{user_email}';"""
    params = ()
    result = execute_sql_query(query, params)
    user_info_list = []
    for prod_info in result:
        dict_temp = {}
        dict_temp["id_user"] = prod_info[0]
        dict_temp["password"] = prod_info[1]
        user_info_list.append(dict_temp)
    return user_info_list


# User is validated
def connect_user(id_user: int) -> None:
    """Update the user connection

    Args:
        id_user (int): user id
    """
    query = f"""UPDATE User
                SET id_connection = (SELECT con.id_connection
                                     FROM Connection as con
                                     WHERE con.status = 'connected')
                WHERE id_user = {id_user};"""
    params = ()
    execute_sql_query(query, params)


def disconnect_user(id_user: str) -> None:
    """Update the user connection

    Args:
        id_user (int): user id
    """
    query = f"""UPDATE User
                SET id_connection = (SELECT con.id_connection
                                     FROM Connection as con
                                     WHERE con.status = 'timeout')
                WHERE id_user = {id_user};"""
    params = ()
    execute_sql_query(query, params)


# region Panier & Commande
def user_open_shopping_cart_id(id_user: int) -> int | None:
    """Return the id_shoppingcart of the latest opened shopping cart
    associated to the user with id id_user. An opened shopping cart
    is a shopping cart that does not have an invoice yet.

    Args:
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

    if result:
        return result[0][0]
    else:
        return None


# Shopping cart
def user_shopping_cart(id_shoppingcart: int) -> list[dict]:
    """Return information of a shopping cart.
    Interrogate the database with the name ecommerce_db_name.

    Args:
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
def update_command_line(id_prod: int, id_shoppingcart: int, new_quantity: int) -> None:
    """Update the database to modify the
    quantity of the entry with primary key id_prod, id_shopingcart

    Args:
        id_prod (int): id of the product
        id_shoppingcart (int): id of the shoppingcart
        new_quantity (int): the new quantity
    """
    query = f"""UPDATE CommandLine
            SET quantity = {new_quantity}
            WHERE id_prod = {id_prod} AND id_shoppingcart = {id_shoppingcart};
        """
    params = ()
    execute_sql_query(query, params)


# Remove command line
def remove_command_line(id_prod: int, id_shoppingcart: int) -> None:
    """Remove in the database the command line matching the
    primary key id_prod, id_shopingcart

    Args:
        id_prod (int): id of the product
        id_shoppingcart (int): id of the shoppingcart
    """
    query = f"""DELETE FROM CommandLine
            WHERE id_prod = {id_prod} AND id_shoppingcart = {id_shoppingcart};
        """
    params = ()
    execute_sql_query(query, params)


# region Commande
def get_all_info_user(id_user: str) -> dict:
    """Get user information

    Args:
        id_user (str): user id

    Returns:
        dict: user information
    """
    query = f"""SELECT u.name, u.firstname, u.email, u.phone
            FROM User as u
            WHERE id_user = {id_user}
            ;"""
    params = ()
    result = execute_sql_query(query, params)
    user_info_dict = {}
    for prod_info in result:
        user_info_dict["name"] = prod_info[0]
        user_info_dict["firstname"] = prod_info[1]
        user_info_dict["email"] = prod_info[2]
        user_info_dict["phone"] = prod_info[3]
    return user_info_dict


def get_user_address(id_user: int) -> list[tuple]:
    """Get user address

    Args:
        id_user (int): user id

    Returns:
        list[tuple]: each tuple contain address: (street, city)
    """
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


# TODO pour améliorer la facturation, créer une clé étrangère dans invoice: id_address
def create_invoice(id_user: int) -> None:
    """Create invoice

    Args:
        id_user (int): user id
    """
    id_shoppingcart = user_open_shopping_cart_id(id_user)
    today_date = datetime.now().strftime("%d/%m/%Y")
    query = f"""INSERT INTO Invoice(id_shoppingcart, date)
                VALUES({id_shoppingcart},'{today_date}');
            """

    params = ()
    execute_sql_query(query, params)
    update_shoppingcart(id_shoppingcart)


def update_shoppingcart(id_shoppingcart: int) -> None:
    """Update shoppingcart: id_invoice

    Args:
        id_shoppingcart (int): _description_
    """
    query = f"""UPDATE ShoppingCart
                SET id_invoice = (SELECT inv.id_invoice
                                  FROM ShoppingCart as sc
                                  LEFT JOIN Invoice as inv on inv.id_shoppingcart = sc.id_shoppingcart
                                  WHERE sc.id_shoppingcart = {id_shoppingcart});
            """
    params = ()
    execute_sql_query(query, params)


# region Admin


def is_admin(id_user: int) -> bool:
    """Verify if the user is admin

    Args:
        id_user (int): user id

    Returns:
        bool: condition if the user is admin
    """
    query = f"""SELECT r.name
                FROM User as u
                LEFT JOIN Role as r on r.id_role = u.id_role
                WHERE id_user = {id_user};
            """
    params = ()
    result = execute_sql_query(query, params)

    return result[0][0] == "admin"


# region main local
def main():
    db_name = cv.bdd_path

    # # Test user_shopping_cart
    # for i in range(3):
    #     for info in user_shopping_cart(db_name, i + 1):
    #         print(info)
    #     print()

    # get_user_address(1)
    # print(is_admin(2))
    # get_user_info_connect("paul.dupont@generator.com")


if __name__ == "__main__":
    main()

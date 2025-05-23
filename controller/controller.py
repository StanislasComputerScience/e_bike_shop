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


def main():
    db_name = "ecommerce_database"
    list_product = most_popular_products(db_name)
    print(f"list_product= {list_product}")


if __name__ == "__main__":
    main()

import sqlite3


# region Home
# Most 2 popular products
def most_popular_products(ecommerce_db_name: str) -> list[tuple[str, str]]:
    with sqlite3.connect(f"{ecommerce_db_name}.db") as connexion:
        cursor = connexion.cursor()

        query = cursor.execute(
            """SELECT prod.name,
                      prod.image_path
               FROM Product as prod
               ORDER BY prod.popularity DESC
               LIMIT 2;
            """
        )
        return query.fetchall()


# Most 2 products buy
def most_products_buy(ecommerce_db_name: str):
    with sqlite3.connect(f"{ecommerce_db_name}.db") as connexion:
        cursor = connexion.cursor()

        query = cursor.execute(
            """SELECT prod.name,
                      prod.image_path
               FROM Product as prod
               RIGHT JOIN (SELECT cl.id_product
                            FROM Invoice as fact
                            INNER JOIN ShoppingCart as sc on sc.id_shoppingcart = fact.id_shoppingcart 
                                                            and sc.id_invoice = fact.id_invoice
                            INNER JOIN CommandLine as cl on cl.id_shoppingcart = sc.id_shoppingcart
                            GROUP BY cl.id_product) as prod_sale on prod_sale.id_product = prod.id_prod
               ORDER BY prod.popularity DESC
               LIMIT 2
            """
        )
        print(query.fetchall())


def main():
    db_name = "ecommerce_database"
    most_products_buy(db_name)


if __name__ == "__main__":
    main()

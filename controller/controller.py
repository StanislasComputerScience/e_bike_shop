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
        return query.fetchall()


def main():
    db_name = "ecommerce_database"
    most_products_buy(db_name)


if __name__ == "__main__":
    main()

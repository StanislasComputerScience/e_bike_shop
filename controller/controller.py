import sqlite3


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


def main():
    db_name = "ecommerce_database"
    most_popular_products(db_name)


if __name__ == "__main__":
    main()

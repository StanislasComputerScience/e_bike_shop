import sqlite3


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
               p.image_path, p.price_ET * (1 + v.rate) AS price_it
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
        ]

        # Transformation du résultat en une liste de dictionnaires
        return [dict(zip(fields, row)) for row in result]


print(product_catalog()[0])

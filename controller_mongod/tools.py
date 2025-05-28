from .controller_mongod import product_catalog


def load_products_and_c():
    l_products = product_catalog()
    name_products = [p["name"] for p in l_products]

    return l_products, name_products
from .controller_mongod import product_catalog


def load_products_and_c() -> tuple[list[dict], list[str]]:
    """Get the product catalog and create a list of their names.

    Returns:
        tuple[list[dict], list[str]]: the catalog and the list of names
    """
    l_products = product_catalog()
    name_products = [p["name"] for p in l_products]

    return l_products, name_products

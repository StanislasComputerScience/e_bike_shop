import sqlite3

ecommerce_db_dict = {}

def create_json_db():
    """Function permit to create json db
    """

def create_table_db(ecommerce_db_dict: dict):
    ecommerce_db_dict["create table Category"] = \
        """CREATE TABLE IF NOT EXISTS Category (
            id_category INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, 
            name TEXT NOT NULL
        )"""
    ecommerce_db_dict["create table VAT"] = \
        """CREATE TABLE IF NOT EXISTS VAT (
            id_vat INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, 
            rate REAL UNSIGNED NOT NULL,
            name TEXT NOT NULL
        )"""
    ecommerce_db_dict["create table Product"] = \
        """CREATE TABLE IF NOT EXISTS Product (
            id_prod INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            id_category INTEGER NOT NULL,
            id_vat INTEGER NOT NULL,
            name TEXT NOT NULL,
            number_of_units INTEGER UNSIGNED NOT NULL,
            description TEXT NOT NULL,
            tech_specification TEXT,
            image_path TEXT,
            price_ET REAL UNSIGNED NOT NULL,
            FOREIGN KEY(id_category) REFERENCES Category(id_category),
            FOREIGN KEY(id_vat) REFERENCES VAT(id_vat)
        )"""
    ecommerce_db_dict["create table CommandLine"] = \
        """CREATE TABLE IF NOT EXISTS CommandLine (
            id_prod INTEGER PRIMARY KEY NOT NULL,
            id_shoppingcart INTEGER PRIMARY KEY NOT NULL,
            price_ET REAL UNSIGNED NOT NULL,
            quantity INTEGER UNSIGNED NOT NULL,
            rate_vat REAL UNSIGNED NOT NULL,
            FOREIGN KEY(id_prod) REFERENCES Product(id_prod),
            FOREIGN KEY(id_shoppingcart) REFERENCES VAT(ShoppingCart)
       )"""
    ecommerce_db_dict["create_table_role"] = """CREATE TABLE Role (id_role INTEGER PRIMARY KEY AUTOINCREMENT, 
                                                                   role_name TEXT NOT NULL);"""
    ecommerce_db_dict["create_table_connexion"] = """CREATE TABLE Connexion (id_connexion INTEGER PRIMARY KEY AUTOINCREMENT, 
                                                                             connexion_name TEXT NOT NULL);"""

def main():
    pass

if __name__ == "__main__":
        main()    

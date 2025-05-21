import sqlite3

def create_json_db():
    """Function permit to create json db
    """

def create_table_db(ecommerce_db_dict: dict):
    """Function to create table of the db
    """
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
    ecommerce_db_dict["create_table_role"] = \
        """CREATE TABLE IF NOT EXISTS Role (
            id_role INTEGER PRIMARY KEY AUTOINCREMENT, 
            name TEXT NOT NULL);"""
    ecommerce_db_dict["create_table_connexion"] = \
        """CREATE TABLE IF NOT EXISTS Connexion (
            id_connexion INTEGER PRIMARY KEY AUTOINCREMENT, 
            status TEXT NOT NULL);"""
    ecommerce_db_dict["create_table_user"] = \
        """CREATE TABLE IF NOT EXISTS User (
            id_user INTEGER PRIMARY KEY AUTOINCREMENT, 
            id_connexion INTEGER NOT NULL,
            id_role INTEGER NOT NULL,
            name TEXT NOT NULL,
            firstname TEXT NOT NULL,
            birth_date TEXT,
            email TEXT NOT NULL,
            phone TEXT,
            FOREIGN KEY(id_connexion) REFERENCES Connexion(id_connexion),
            FOREIGN KEY(id_role) REFERENCES Role(id_role));"""
    ecommerce_db_dict["create_table_address"] = \
        """CREATE TABLE IF NOT EXISTS Address (
            id_address INTEGER PRIMARY KEY AUTOINCREMENT, 
            id_user INTEGER NOT NULL,
            number INTEGER NOT NULL,
            street TEXT NOT NULL,
            postal_code TEXT NOT NULL,
            city TEXT NOT NULL,
            FOREIGN KEY(id_user) REFERENCES User(id_user));"""
    ecommerce_db_dict["create_table_shopping_cart"] = \
        """CREATE TABLE IF NOT EXISTS ShoppingCart (
            id_shoppingcart INTEGER PRIMARY KEY AUTOINCREMENT, 
            id_user INTEGER NOT NULL,
            date TEXT NOT NULL,
            FOREIGN KEY(id_user) REFERENCES User(id_user));"""
    ecommerce_db_dict["create_table_invoice"] = \
        """CREATE TABLE IF NOT EXISTS Invoice (
            id_invoice INTEGER PRIMARY KEY AUTOINCREMENT, 
            id_shoppingcart INTEGER NOT NULL,
            date TEXT NOT NULL,
            FOREIGN KEY(id_shoppingcart) REFERENCES ShoppingCart(id_shoppingcart));"""
            

def create_database(ecommerce_db_dict: dict, database_name: str):
    """Create your database

    Args:
        ecommerce_db_dict (dict): contain all queries to create your database
        database_name (str): database name
    """
    try:
        connexion = sqlite3.connect(f"{database_name}.db")
        cursor = connexion.cursor()
        for key, sql_command in ecommerce_db_dict.items():
            print(key)
            cursor.execute(sql_command)
    except:
         print(f"{database_name} already exist !")

def main():
    ecommerce_db_dict = {}
    create_table_db(ecommerce_db_dict)
    create_database(ecommerce_db_dict, "ecommerce_database")

if __name__ == "__main__":
        main()    

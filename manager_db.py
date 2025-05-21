import sqlite3

ecommerce_db_dict = {}


def create_table_db(ecommerce_db_dict: dict):

    ecommerce_db_dict["create table Category"] = \
        """CREATE TABLE IF NOT EXISTS Category (
            id_category INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, 
            name TEXT NOT NULL
        )"""
    ecommerce_db_dict["create table VAT"] = \
        """CREATE TABLE IF NOT EXISTS VAT (
            id_vat INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, 
            rate REAL NOT NULL,
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
            price_ET INTEGER UNSIGNED NOT NULL,
            FOREIGN KEY(id_category) REFERENCES Category(id_category),
            FOREIGN KEY(id_vat) REFERENCES VAT(id_vat)
        )"""

def test():
    create_table_db(ecommerce_db_dict)
    with sqlite3.connect("test.db") as connection:
        print(connection.total_changes)
        cursor = connection.cursor()
        for action, sql_command in ecommerce_db_dict.items():
            print(f"{action}...")
            cursor.execute(sql_command)

if __name__ == "__main__":
    test()

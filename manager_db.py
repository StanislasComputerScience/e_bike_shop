import sqlite3

def create_json_db():
    """Function permit to create json db
    """

def create_table_db(ecommerce_db_dict: dict):
    """Function to create table of the db
    """
    ecommerce_db_dict["create_table_role"] = """CREATE TABLE Role (id_role INTEGER PRIMARY KEY AUTOINCREMENT, 
                                                                   role_name TEXT NOT NULL);"""
    ecommerce_db_dict["create_table_connexion"] = """CREATE TABLE Connexion (id_connexion INTEGER PRIMARY KEY AUTOINCREMENT, 
                                                                             connexion_name TEXT NOT NULL);"""

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

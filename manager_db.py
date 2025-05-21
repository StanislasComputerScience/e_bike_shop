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
    ecommerce_db_dict["create_table_user"] = """CREATE TABLE User (id_user INTEGER PRIMARY KEY AUTOINCREMENT, 
                                                                   id_connexion INTEGER NOT NULL,
                                                                   id_role INTEGER NOT NULL,
                                                                   user_name TEXT NOT NULL,
                                                                   user_firstname TEXT NOT NULL,
                                                                   birth_date TEXT,
                                                                   user_email TEXT NOT NULL,
                                                                   user_phone TEXT,
                                                                   FOREIGN KEY(id_connexion) REFERENCES Connexion(id_connexion),
                                                                   FOREIGN KEY(id_role) REFERENCES Role(id_role));"""

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

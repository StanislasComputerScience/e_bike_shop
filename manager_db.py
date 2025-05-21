import sqlite3

ecommerce_db_dict = {}

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
    
def main():
    pass

if __name__ == "__main__":
        main()    

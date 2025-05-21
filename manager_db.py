import sqlite3


def create_json_db():
    """Function permit to create json db"""

    """Function permit to create json db"""


def create_table_db(ecommerce_db_dict: dict):
    """Function to create table of the db"""
    ecommerce_db_dict[
        "create table Role"
    ] = """CREATE TABLE IF NOT EXISTS Role (
            id_role INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, 
            name TEXT NOT NULL
        );"""
    ecommerce_db_dict[
        "create table Connection"
    ] = """CREATE TABLE IF NOT EXISTS Connection (
            id_connection INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, 
            status TEXT NOT NULL
        );"""
    ecommerce_db_dict[
        "create table User"
    ] = """CREATE TABLE IF NOT EXISTS User (
            id_user INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, 
            id_connection INTEGER NOT NULL,
            id_role INTEGER NOT NULL,
            name TEXT NOT NULL,
            firstname TEXT NOT NULL,
            birth_date TEXT,
            email TEXT NOT NULL,
            phone TEXT,
            FOREIGN KEY(id_connection) REFERENCES Connection(id_connection),
            FOREIGN KEY(id_role) REFERENCES Role(id_role)
        );"""
    ecommerce_db_dict[
        "create table Address"
    ] = """CREATE TABLE IF NOT EXISTS Address (
            id_address INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, 
            id_user INTEGER NOT NULL,
            number INTEGER NOT NULL,
            street TEXT NOT NULL,
            postal_code TEXT NOT NULL,
            city TEXT NOT NULL,
            FOREIGN KEY(id_user) REFERENCES User(id_user)
        );"""
    ecommerce_db_dict[
        "create table Category"
    ] = """CREATE TABLE IF NOT EXISTS Category (
            id_category INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, 
            name TEXT NOT NULL
        );"""
    ecommerce_db_dict[
        "create table VAT"
    ] = """CREATE TABLE IF NOT EXISTS VAT (
            id_vat INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, 
            rate REAL UNSIGNED NOT NULL,
            name TEXT NOT NULL
        );"""
    ecommerce_db_dict[
        "create table Product"
    ] = """CREATE TABLE IF NOT EXISTS Product (
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
        );"""
    ecommerce_db_dict[
        "create table ShoppingCart"
    ] = """CREATE TABLE IF NOT EXISTS ShoppingCart (
            id_shoppingcart INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, 
            id_user INTEGER NOT NULL,
            date TEXT NOT NULL,
            FOREIGN KEY(id_user) REFERENCES User(id_user)
        );"""
    ecommerce_db_dict[
        "create table Invoice"
    ] = """CREATE TABLE IF NOT EXISTS Invoice (
            id_invoice INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, 
            id_shoppingcart INTEGER NOT NULL,
            date TEXT NOT NULL,
            FOREIGN KEY(id_shoppingcart) REFERENCES ShoppingCart(id_shoppingcart)
        );"""
    ecommerce_db_dict[
        "create table CommandeLine"
    ] = """CREATE TABLE IF NOT EXISTS CommandLine (
            id_prod INTEGER NOT NULL,
            id_shoppingcart INTEGER NOT NULL,
            price_ET REAL UNSIGNED NOT NULL,
            quantity INTEGER UNSIGNED NOT NULL,
            rate_vat REAL UNSIGNED NOT NULL,
            PRIMARY KEY(id_prod,id_shoppingcart)
            FOREIGN KEY(id_prod) REFERENCES Product(id_prod)
            FOREIGN KEY(id_shoppingcart) REFERENCES ShoppingCart(id_shoppingcart)
       );"""


def create_insert_into_tables(ecommerce_db_dict: dict):
    ecommerce_db_dict[
        "insert into Role: user"
    ] = """INSERT INTO Role(name)
            VALUES('user');
        """

    ecommerce_db_dict[
        "insert into Role: admin"
    ] = """INSERT INTO Role(name)
            VALUES('admin');
        """

    ecommerce_db_dict[
        "insert into Connection: timeout"
    ] = """INSERT INTO Connection(status)
            VALUES('timeout');
        """

    ecommerce_db_dict[
        "insert into Connection: pending"
    ] = """INSERT INTO Connection(status)
            VALUES('pending');
        """

    ecommerce_db_dict[
        "insert into Connection: connected"
    ] = """INSERT INTO Connection(status)
            VALUES('connected');
        """

    ecommerce_db_dict[
        "insert into User: first_user"
    ] = """INSERT INTO User(id_connection, id_role, name,firstname,birth_date,email,phone)
        VALUES(1,1,'Dupont','Paul','13/01/1992','paul.dupont@generator.com','010203040506');
    """

    ecommerce_db_dict[
        "insert into User: second_user"
    ] = """INSERT INTO User(id_connection, id_role, name,firstname,birth_date,email,phone)
            VALUES(1,1,'Martin','Claire','22/07/1988','claire.martin@generator.com','060102030405');
        """

    ecommerce_db_dict[
        "insert into User: third_user"
    ] = """INSERT INTO User(id_connection, id_role, name,firstname,birth_date,email,phone)
            VALUES(1,1,'Bernard','Luc','05/11/1990','luc.bernard@generator.com','070809101112');
        """

    ecommerce_db_dict[
        "insert into User: fourth_user"
    ] = """INSERT INTO User(id_connection, id_role, name,firstname,birth_date,email,phone)
            VALUES(1,1,'Lemoine','Sophie','17/03/1985','sophie.lemoine@generator.com','060708091011');
        """

    ecommerce_db_dict[
        "insert into User: fifth_user"
    ] = """INSERT INTO User(id_connection, id_role, name,firstname,birth_date,email,phone)
            VALUES(1,1,'Roux','Antoine','30/06/1993','antoine.roux@generator.com','010101010101');
        """

    ecommerce_db_dict[
        "insert into User: sixth_user"
    ] = """INSERT INTO User(id_connection, id_role, name,firstname,birth_date,email,phone)
            VALUES(1,1,'Garcia','Emma','09/12/1996','emma.garcia@generator.com','050505050505');
        """

    ecommerce_db_dict[
        "insert into User: seventh_user"
    ] = """INSERT INTO User(id_connection, id_role, name,firstname,birth_date,email,phone)
            VALUES(1,1,'Moreau','Julien','14/02/1991','julien.moreau@generator.com','020304050607');
        """

    ecommerce_db_dict[
        "insert into User: eighth_user"
    ] = """INSERT INTO User(id_connection, id_role, name,firstname,birth_date,email,phone)
            VALUES(1,1,'Fournier','Camille','25/09/1989','camille.fournier@generator.com','080807070707');
        """

    ecommerce_db_dict[
        "insert into User: ninth_user"
    ] = """INSERT INTO User(id_connection, id_role, name,firstname,birth_date,email,phone)
            VALUES(1,1,'Girard','Hugo','08/08/1994','hugo.girard@generator.com','090909090909');
        """

    ecommerce_db_dict[
        "insert into User: tenth_user"
    ] = """INSERT INTO User(id_connection, id_role, name,firstname,birth_date,email,phone)
            VALUES(1,1,'Lambert','Nina','01/04/1995','nina.lambert@generator.com','040404040404');
        """

    ecommerce_db_dict[
        "insert into Address: first address"
    ] = """INSERT INTO Address(id_user, number, street, postal_code, city)
        VALUES(1,2,'Rue de la Mouette','97400','Saint-Denis');
    """

    ecommerce_db_dict[
        "insert into Address: second address"
    ] = """INSERT INTO Address(id_user, number, street, postal_code, city)
            VALUES(1,10,'Avenue des Cèdres','75012','Paris');
        """

    ecommerce_db_dict[
        "insert into Address: third address"
    ] = """INSERT INTO Address(id_user, number, street, postal_code, city)
            VALUES(2,5,'Rue des Lilas','69007','Lyon');
        """

    ecommerce_db_dict[
        "insert into Address: fourth address"
    ] = """INSERT INTO Address(id_user, number, street, postal_code, city)
            VALUES(2,17,'Boulevard Victor Hugo','06000','Nice');
        """

    ecommerce_db_dict[
        "insert into Address: fifth address"
    ] = """INSERT INTO Address(id_user, number, street, postal_code, city)
            VALUES(3,22,'Rue Saint-Sauveur','59800','Lille');
        """

    ecommerce_db_dict[
        "insert into Address: sixth address"
    ] = """INSERT INTO Address(id_user, number, street, postal_code, city)
            VALUES(3,3,'Chemin des Érables','34000','Montpellier');
        """

    ecommerce_db_dict[
        "insert into Address: seventh address"
    ] = """INSERT INTO Address(id_user, number, street, postal_code, city)
            VALUES(4,9,'Allée des Peupliers','31000','Toulouse');
        """

    ecommerce_db_dict[
        "insert into Address: eighth address"
    ] = """INSERT INTO Address(id_user, number, street, postal_code, city)
            VALUES(5,12,'Rue de la République','13001','Marseille');
        """

    ecommerce_db_dict[
        "insert into Address: ninth address"
    ] = """INSERT INTO Address(id_user, number, street, postal_code, city)
            VALUES(5,44,'Rue des Primevères','29200','Brest');
        """

    ecommerce_db_dict[
        "insert into Address: tenth address"
    ] = """INSERT INTO Address(id_user, number, street, postal_code, city)
            VALUES(6,7,'Rue de l’Atlantique','17000','La Rochelle');
        """

    ecommerce_db_dict[
        "insert into Address: eleventh address"
    ] = """INSERT INTO Address(id_user, number, street, postal_code, city)
            VALUES(6,15,'Rue de la Plage','33120','Arcachon');
        """

    ecommerce_db_dict[
        "insert into Address: twelfth address"
    ] = """INSERT INTO Address(id_user, number, street, postal_code, city)
            VALUES(7,1,'Place du Marché','25000','Besançon');
        """

    ecommerce_db_dict[
        "insert into Address: thirteenth address"
    ] = """INSERT INTO Address(id_user, number, street, postal_code, city)
            VALUES(7,8,'Rue des Fleurs','41000','Blois');
        """

    ecommerce_db_dict[
        "insert into Address: fourteenth address"
    ] = """INSERT INTO Address(id_user, number, street, postal_code, city)
            VALUES(8,20,'Rue du Château','67000','Strasbourg');
        """

    ecommerce_db_dict[
        "insert into Address: fifteenth address"
    ] = """INSERT INTO Address(id_user, number, street, postal_code, city)
            VALUES(9,6,'Avenue des Pins','84000','Avignon');
        """

    ecommerce_db_dict[
        "insert into Address: sixteenth address"
    ] = """INSERT INTO Address(id_user, number, street, postal_code, city)
            VALUES(9,13,'Rue Victor Schoelcher','97300','Cayenne');
        """

    ecommerce_db_dict[
        "insert into Address: seventeenth address"
    ] = """INSERT INTO Address(id_user, number, street, postal_code, city)
            VALUES(10,19,'Rue Pasteur','97110','Pointe-à-Pitre');
        """

    ecommerce_db_dict[
        "insert into Address: eighteenth address"
    ] = """INSERT INTO Address(id_user, number, street, postal_code, city)
            VALUES(10,33,'Avenue de la Liberté','98800','Nouméa');
        """

    ecommerce_db_dict[
        "insert into Address: nineteenth address"
    ] = """INSERT INTO Address(id_user, number, street, postal_code, city)
            VALUES(10,4,'Rue Jean Jaurès','72000','Le Mans');
        """

    ecommerce_db_dict[
        "insert into Address: twentieth address"
    ] = """INSERT INTO Address(id_user, number, street, postal_code, city)
            VALUES(4,11,'Rue du Stade','86000','Poitiers');
        """

    ecommerce_db_dict[
        "insert into ShoppingCart: first ShopCart"
    ] = """INSERT INTO ShoppingCart(id_user, date)
        VALUES(1,'12/03/2024');
    """

    ecommerce_db_dict[
        "insert into ShoppingCart: second ShopCart"
    ] = """INSERT INTO ShoppingCart(id_user, date)
            VALUES(2,'05/01/2024');
        """

    ecommerce_db_dict[
        "insert into ShoppingCart: third ShopCart"
    ] = """INSERT INTO ShoppingCart(id_user, date)
            VALUES(3,'22/11/2023');
        """

    ecommerce_db_dict[
        "insert into ShoppingCart: fourth ShopCart"
    ] = """INSERT INTO ShoppingCart(id_user, date)
            VALUES(4,'30/10/2023');
        """

    ecommerce_db_dict[
        "insert into ShoppingCart: fifth ShopCart"
    ] = """INSERT INTO ShoppingCart(id_user, date)
            VALUES(5,'15/08/2023');
        """

    ecommerce_db_dict[
        "insert into ShoppingCart: sixth ShopCart"
    ] = """INSERT INTO ShoppingCart(id_user, date)
            VALUES(6,'19/04/2024');
        """

    ecommerce_db_dict[
        "insert into ShoppingCart: seventh ShopCart"
    ] = """INSERT INTO ShoppingCart(id_user, date)
            VALUES(7,'03/05/2024');
        """

    ecommerce_db_dict[
        "insert into ShoppingCart: eighth ShopCart"
    ] = """INSERT INTO ShoppingCart(id_user, date)
            VALUES(8,'25/12/2023');
        """

    ecommerce_db_dict[
        "insert into ShoppingCart: ninth ShopCart"
    ] = """INSERT INTO ShoppingCart(id_user, date)
            VALUES(9,'01/01/2024');
        """

    ecommerce_db_dict[
        "insert into ShoppingCart: tenth ShopCart"
    ] = """INSERT INTO ShoppingCart(id_user, date)
            VALUES(10,'09/02/2024');
        """

    ecommerce_db_dict[
        "insert into Invoice: first Invoice"
    ] = """INSERT INTO Invoice(id_shoppingcart, date)
        VALUES(1,'13/03/2024');
    """

    ecommerce_db_dict[
        "insert into Invoice: second Invoice"
    ] = """INSERT INTO Invoice(id_shoppingcart, date)
            VALUES(2,'06/01/2024');
        """

    ecommerce_db_dict[
        "insert into Invoice: third Invoice"
    ] = """INSERT INTO Invoice(id_shoppingcart, date)
            VALUES(3,'23/11/2023');
        """

    ecommerce_db_dict[
        "insert into Invoice: fourth Invoice"
    ] = """INSERT INTO Invoice(id_shoppingcart, date)
            VALUES(4,'31/10/2023');
        """

    ecommerce_db_dict[
        "insert into Invoice: fifth Invoice"
    ] = """INSERT INTO Invoice(id_shoppingcart, date)
            VALUES(5,'16/08/2023');
        """

    ecommerce_db_dict[
        "insert into Invoice: sixth Invoice"
    ] = """INSERT INTO Invoice(id_shoppingcart, date)
            VALUES(6,'20/04/2024');
        """

    ecommerce_db_dict[
        "insert into Invoice: seventh Invoice"
    ] = """INSERT INTO Invoice(id_shoppingcart, date)
            VALUES(7,'04/05/2024');
        """

    ecommerce_db_dict[
        "insert into Invoice: eighth Invoice"
    ] = """INSERT INTO Invoice(id_shoppingcart, date)
            VALUES(8,'26/12/2023');
        """

    ecommerce_db_dict[
        "insert into Invoice: ninth Invoice"
    ] = """INSERT INTO Invoice(id_shoppingcart, date)
            VALUES(9,'02/01/2024');
        """

    ecommerce_db_dict[
        "insert into Invoice: tenth Invoice"
    ] = """INSERT INTO Invoice(id_shoppingcart, date)
            VALUES(10,'10/02/2024');
        """


def create_database(ecommerce_db_dict: dict, database_name: str):
    """Create your database

    Args:
        ecommerce_db_dict (dict): contain all queries to create your database
        database_name (str): database name
    """
    try:
        Connection = sqlite3.connect(f"{database_name}.db")
        cursor = Connection.cursor()
        for key, sql_command in ecommerce_db_dict.items():
            print(key)
            cursor.execute(sql_command)
        Connection.commit()
    except:
        print(f"{database_name} already exist !")
        print(f"{database_name} already exist !")


def main():
    ecommerce_db_dict = {}
    create_table_db(ecommerce_db_dict)
    create_insert_into_tables(ecommerce_db_dict)
    create_database(ecommerce_db_dict, "ecommerce_database")


if __name__ == "__main__":
    main()

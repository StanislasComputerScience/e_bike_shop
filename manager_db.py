import sqlite3


def create_json_db():
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
        "create table CommandLine"
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
        "insert into User: first user"
    ] = """INSERT INTO User(id_connection, id_role, name,firstname, birth_date, email, phone)
            VALUES(1,1,'Dupont','Paul','13/01/1992','paul.dupont@generator.com','010203040506');
        """
    ecommerce_db_dict[
        "insert into User: second user"
    ] = """INSERT INTO User(id_connection, id_role, name,firstname, birth_date, email, phone)
        VALUES(1,1,'Martin','Claire','22/07/1988','claire.martin@generator.com','060102030405');
    """
    ecommerce_db_dict[
        "insert into User: third user"
    ] = """INSERT INTO User(id_connection, id_role, name,firstname, birth_date, email, phone)
            VALUES(1,1,'Bernard','Luc','05/11/1990','luc.bernard@generator.com','070809101112');
        """
    ecommerce_db_dict[
        "insert into User: fourth user"
    ] = """INSERT INTO User(id_connection, id_role, name,firstname, birth_date, email, phone)
            VALUES(1,1,'Lemoine','Sophie','17/03/1985','sophie.lemoine@generator.com','060708091011');
        """
    ecommerce_db_dict[
        "insert into User: fifth user"
    ] = """INSERT INTO User(id_connection, id_role, name,firstname, birth_date, email, phone)
            VALUES(1,1,'Roux','Antoine','30/06/1993','antoine.roux@generator.com','010101010101');
        """
    ecommerce_db_dict[
        "insert into User: sixth user"
    ] = """INSERT INTO User(id_connection, id_role, name,firstname, birth_date, email, phone)
            VALUES(1,1,'Garcia','Emma','09/12/1996','emma.garcia@generator.com','050505050505');
        """
    ecommerce_db_dict[
        "insert into User: seventh user"
    ] = """INSERT INTO User(id_connection, id_role, name,firstname, birth_date, email, phone)
            VALUES(1,1,'Moreau','Julien','14/02/1991','julien.moreau@generator.com','020304050607');
        """
    ecommerce_db_dict[
        "insert into User: eighth user"
    ] = """INSERT INTO User(id_connection, id_role, name,firstname, birth_date, email, phone)
            VALUES(1,1,'Fournier','Camille','25/09/1989','camille.fournier@generator.com','080807070707');
        """
    ecommerce_db_dict[
        "insert into User: ninth user"
    ] = """INSERT INTO User(id_connection, id_role, name,firstname, birth_date, email, phone)
            VALUES(1,1,'Girard','Hugo','08/08/1994','hugo.girard@generator.com','090909090909');
        """
    ecommerce_db_dict[
        "insert into User: tenth user"
    ] = """INSERT INTO User(id_connection, id_role, name,firstname, birth_date, email, phone)
            VALUES(1,1,'Lambert','Nina','01/04/1995','nina.lambert@generator.com','040404040404');
        """
    ecommerce_db_dict[
        "insert into Address: first address"
    ] = """INSERT INTO Address(id_user, number, street, postal_code, city)
            VALUES(1,2,'Rue de la mouette','97400','Saint-Denis');
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
        "insert into ShoppingCart: first ShopCart"
    ] = """INSERT INTO ShoppingCart(id_user, date)
            VALUES(1,'28/12/1911');
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
            VALUES(1,'04/01/2001');
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
    ecommerce_db_dict[
        "insert into Category: bike"
    ] = """INSERT INTO Category (name) VALUES ('bike');
        """
    ecommerce_db_dict[
        "insert into Category: accessory "
    ] = """INSERT INTO Category (name) VALUES ('accessory');
        """
    ecommerce_db_dict[
        "insert into VAT: french (standard)"
    ] = """INSERT INTO VAT (rate, name) VALUES (0.2, 'french (standard)');
        """
    ecommerce_db_dict[
        "insert into Product: first product"
    ] = """INSERT INTO Product (id_category, id_vat, name, number_of_units, description, tech_specification, image_path, price_ET)
            VALUES (1, 1, "VTT 1250XC", 10, 
            "Ce VTT est conçu pour se lancer dans la pratique du VTT Cross Country (XC). Votre premier
             VTT XC axé performance à prix contenu. Cadre aluminium et transmission 11 vitesses.",
            "Cadre: Aluminium, tubes à épaisseurs variables ; Transmission: Plateau de 32 ; Roues: 29'' ; Amortisseur: simple ; Freins : hydraulique",
            "vers/mon/image.jpeg", 899.99)
        """
    ecommerce_db_dict[
        "insert into Product: ten bikes"
    ] = """INSERT INTO Product (id_category, id_vat, name, number_of_units, description, tech_specification, image_path, price_ET)
            VALUES
            (1, 1, "VTT Trail 500", 15, "VTT robuste pour les sentiers forestiers et les randonnées en montagne.", 
            "Cadre: Aluminium 6061 ; Transmission: Shimano 9 vitesses ; Roues: 27.5'' ; Freins: Disques hydrauliques",
            "images/vtt_trail_500.jpeg", 749.99),
            (1, 1, "Vélo de route AeroX", 8, "Vélo de route profilé pour les cyclistes avides de performance sur bitume.", 
            "Cadre: Carbone ; Transmission: Shimano 105 ; Roues: 700C ; Freins: Patins", 
            "images/aerox.jpeg", 1299.00),
            (1, 1, "VTT XC Pro 900", 5, "Modèle haute performance pour le cross-country intensif.", 
            "Cadre: Carbone ; Transmission: SRAM Eagle 12v ; Amortisseur: RockShox ; Freins: Disques hydrauliques", 
            "images/xc_pro_900.jpeg", 1999.99),
            (1, 1, "VTC Urbain 300", 20, "Vélo tout chemin idéal pour les trajets quotidiens en ville ou en campagne.", 
            "Cadre: Acier ; Vitesses: 7 intégrées ; Porte-bagages ; Garde-boue", 
            "images/vtc_urbain_300.jpeg", 499.50),
            (1, 1, "Gravel TerraMix", 7, "Vélo gravel polyvalent pour la route et les chemins non goudronnés.", 
            "Cadre: Aluminium ; Transmission: 2x10 Shimano GRX ; Pneus: 40 mm ; Freins: Disques", 
            "images/terramix.jpeg", 1149.00),
            (1, 1, "Vélo enfant KidRider 16''", 12, "Vélo 16 pouces pour enfants de 4 à 6 ans avec stabilisateurs amovibles.", 
            "Cadre: Acier ; Transmission: Monovitesse ; Freins: V-brake", 
            "images/kidrider_16.jpeg", 159.90),
            (1, 1, "Vélo électrique E-City 400", 6, "Vélo à assistance électrique pour les déplacements urbains confortables.", 
            "Cadre: Aluminium ; Moteur: 250W ; Batterie: 36V 10Ah ; Autonomie: 70 km", 
            "images/e_city_400.jpeg", 1699.00),
            (1, 1, "Fixie Urban Classic", 10, "Vélo fixie élégant et minimaliste pour la ville.", 
            "Cadre: Acier chromé ; Transmission: Single Speed ; Freins: Caliper", 
            "images/fixie_urban_classic.jpeg", 399.00),
            (1, 1, "Fatbike SnowBeast", 3, "Vélo tout-terrain à gros pneus pour rouler sur neige ou sable.", 
            "Cadre: Aluminium ; Pneus: 4.5'' ; Transmission: Shimano 1x9 ; Freins: Disques", 
            "images/snowbeast.jpeg", 899.99),
            (1, 1, "Vélo pliant Compact 20", 9, "Vélo pliable pour les trajets multimodaux et les petits espaces.", 
            "Cadre: Aluminium pliant ; Roues: 20'' ; Vitesses: 6 ; Porte-bagages intégré", 
            "images/compact_20.jpeg", 569.00);
        """
    ecommerce_db_dict[
        "insert into Product: ten accessories"
    ] = """INSERT INTO Product (id_category, id_vat, name, number_of_units, description, tech_specification, image_path, price_ET)
            VALUES
            (2, 1, "Casque UrbanRide", 25, "Casque léger et ventilé pour les trajets urbains.", 
            "Taille: M/L ; Certification: EN1078 ; Poids: 280g ; 14 aérations", 
            "images/casque_urbanride.jpeg", 49.99),
            (2, 1, "Antivol U LockMax", 30, "Antivol en U haute sécurité avec double verrouillage.", 
            "Matériau: Acier trempé ; Dimensions: 18x24cm ; Serrure anti-perçage", 
            "images/ulockmax.jpeg", 59.90),
            (2, 1, "Lumières LED avant/arrière", 40, "Kit de lumières rechargeables pour une meilleure visibilité de nuit.", 
            "Batterie: USB ; Autonomie: 10h ; Modes: 4 ; Étanchéité: IPX4", 
            "images/lumieres_led.jpeg", 24.90),
            (2, 1, "Pompe à pied ProAir", 18, "Pompe avec manomètre pour un gonflage précis de tous types de pneus.", 
            "Pression max: 11 bars ; Corps: aluminium ; Embout: Presta/Schrader", 
            "images/pompe_proair.jpeg", 39.00),
            (2, 1, "Bidon isotherme 600ml", 50, "Bidon cycliste double paroi pour conserver vos boissons au frais.", 
            "Matériau: Sans BPA ; Capacité: 600ml ; Poids: 180g", 
            "images/bidon_600.jpeg", 14.50),
            (2, 1, "Selle Gel Confort+", 22, "Selle large avec gel pour une assise confortable sur longue distance.", 
            "Rails: Acier ; Housse: Synthétique ; Longueur: 270mm", 
            "images/selle_confort.jpeg", 34.99),
            (2, 1, "Gants été respirants", 35, "Gants légers avec paumes renforcées pour cyclisme estival.", 
            "Taille: S à XL ; Matière: Lycra ; Inserts en gel", 
            "images/gants_ete.jpeg", 19.90),
            (2, 1, "Sacoche de cadre étanche", 14, "Sacoche pour smartphone et objets essentiels.", 
            "Volume: 1.2L ; Fixation: velcro ; Écran tactile compatible", 
            "images/sacoche_cadre.jpeg", 29.95),
            (2, 1, "Rétroviseur latéral universel", 27, "Rétroviseur adaptable sur guidon gauche ou droit.", 
            "Angle réglable ; Fixation: collier universel ; Matériau: ABS", 
            "images/retroviseur.jpeg", 12.99),
            (2, 1, "Porte-bagages arrière aluminium", 11, "Support de charge arrière pour vélos avec freins à disque.", 
            "Charge max: 25 kg ; Matériau: Alu anodisé ; Montage rapide", 
            "images/porte_bagages.jpeg", 44.90);
        """

def create_database(ecommerce_db_dict: dict, database_name: str):
    """Create your database

    Args:
        ecommerce_db_dict (dict): contain all queries to create your database
        database_name (str): database name
    """
    try:
        connection = sqlite3.connect(f"{database_name}.db")
        cursor = connection.cursor()
        for key, sql_command in ecommerce_db_dict.items():
            print(key)
            cursor.execute(sql_command)
        connection.commit()
    except:
        print(f"{database_name} already exist !")


def main():
    ecommerce_db_dict = {}
    create_table_db(ecommerce_db_dict)
    create_insert_into_tables(ecommerce_db_dict)
    create_database(ecommerce_db_dict, "ecommerce_database")


if __name__ == "__main__":
    main()

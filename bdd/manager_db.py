import sqlite3
import json
import bcrypt


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
            password TEXT NOT NULL,
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
            popularity INTEGER UNSIGNED,
            FOREIGN KEY(id_category) REFERENCES Category(id_category),
            FOREIGN KEY(id_vat) REFERENCES VAT(id_vat)
        );"""
    ecommerce_db_dict[
        "create table ShoppingCart"
    ] = """CREATE TABLE IF NOT EXISTS ShoppingCart (
            id_shoppingcart INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            id_user INTEGER NOT NULL,
            id_invoice INTEGER,
            date TEXT NOT NULL,
            FOREIGN KEY(id_user) REFERENCES User(id_user),
            FOREIGN KEY(id_invoice) REFERENCES Invoice(id_invoice)
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
    ] = """INSERT INTO User(id_connection, id_role, name, firstname, birth_date, email, password, phone)
            VALUES(1,1,'Dupont','Paul','13/01/1992','paul.dupont@generator.com', '$2b$12$Va0N.6FKF341HjLiDRvgeOlSW6vN2hLLDwmqKZ5dms5MZB7dFZ16a','010203040506');
        """
    ecommerce_db_dict[
        "insert into User: second user"
    ] = """INSERT INTO User(id_connection, id_role, name,firstname, birth_date, email, password, phone)
        VALUES(1,1,'Martin','Claire','22/07/1988','claire.martin@generator.com', '$2b$12$i8VbU.ONeJ4MQeLAJnq.uO3wVtXg1/dyVuyPNMf544ivhuZvtZOuS','060102030405');
    """
    ecommerce_db_dict[
        "insert into User: third user"
    ] = """INSERT INTO User(id_connection, id_role, name,firstname, birth_date, email, password, phone)
            VALUES(1,1,'Bernard','Luc','05/11/1990','luc.bernard@generator.com', '$2b$12$4DBeNvxpOMNFrUmxDAzXNOBVCCD3tQp3x2rNtk.GCnzsMjqlXnrK2','070809101112');
        """
    ecommerce_db_dict[
        "insert into User: fourth user"
    ] = """INSERT INTO User(id_connection, id_role, name,firstname, birth_date, email, password, phone)
            VALUES(1,1,'Lemoine','Sophie','17/03/1985','sophie.lemoine@generator.com', '$2b$12$atfoZMRhfoxTvZldTM4hzepfWVYmSGKce9P1zI6k.bW9iPPdm/OD2','060708091011');
        """
    ecommerce_db_dict[
        "insert into User: fifth user"
    ] = """INSERT INTO User(id_connection, id_role, name,firstname, birth_date, email, password, phone)
            VALUES(1,1,'Roux','Antoine','30/06/1993','antoine.roux@generator.com', '$2b$12$iTgVbR7U7L47S/anDA85cemWY2g8APVVKU2f4oekB1sdH5api0lFO','010101010101');
        """
    ecommerce_db_dict[
        "insert into User: sixth user"
    ] = """INSERT INTO User(id_connection, id_role, name,firstname, birth_date, email, password, phone)
            VALUES(1,1,'Garcia','Emma','09/12/1996','emma.garcia@generator.com', '$2b$12$M8v9HVFgqP3czM70OgXYAOwlfWESliTwXgvTs.ZyX2hd3sQj8WlFS','050505050505');
        """
    ecommerce_db_dict[
        "insert into User: seventh user"
    ] = """INSERT INTO User(id_connection, id_role, name,firstname, birth_date, email, password, phone)
            VALUES(1,1,'Moreau','Julien','14/02/1991','julien.moreau@generator.com', '$2b$12$fF0qa1C7MEpnEFpFImmE4OtrdI0d2wKyCeaMeorzNHhJh/NDsIkNe','020304050607');
        """
    ecommerce_db_dict[
        "insert into User: eighth user"
    ] = """INSERT INTO User(id_connection, id_role, name,firstname, birth_date, email, password, phone)
            VALUES(1,1,'Fournier','Camille','25/09/1989','camille.fournier@generator.com', '$2b$12$dz4PXTvCalkZVQtMHNELyuWxTro02jf28eg5ZGCrYWq00pFN8/SIm','080807070707');
        """
    ecommerce_db_dict[
        "insert into User: ninth user"
    ] = """INSERT INTO User(id_connection, id_role, name,firstname, birth_date, email, password, phone)
            VALUES(1,1,'Girard','Hugo','08/08/1994','hugo.girard@generator.com', '$2b$12$kKzL8uIHwibwVCiXpQVUcOHUCSxKQrUET.kD7.ptA4ODMAVbeqWDi','090909090909');
        """
    ecommerce_db_dict[
        "insert into User: tenth user"
    ] = """INSERT INTO User(id_connection, id_role, name,firstname, birth_date, email, password, phone)
            VALUES(1,1,'Lambert','Nina','01/04/1995','nina.lambert@generator.com', '$2b$12$ATS2k0Q/zd7mj.kfVhEo4uSzTe3a32ljO/hnejWYQu02KDCMnNu0.','040404040404');
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
        "insert into ShoppingCart: first ShopCart"
    ] = """INSERT INTO ShoppingCart(id_user, id_invoice, date)
            VALUES(1,1,'28/12/1911');
        """
    ecommerce_db_dict[
        "insert into ShoppingCart: second ShopCart"
    ] = """INSERT INTO ShoppingCart(id_user, id_invoice, date)
        VALUES(2,2,'05/01/2024');
    """
    ecommerce_db_dict[
        "insert into ShoppingCart: third ShopCart"
    ] = """INSERT INTO ShoppingCart(id_user, id_invoice, date)
            VALUES(3,3,'22/11/2023');
        """
    ecommerce_db_dict[
        "insert into ShoppingCart: fourth ShopCart"
    ] = """INSERT INTO ShoppingCart(id_user, id_invoice, date)
            VALUES(4,4,'30/10/2023');
        """
    ecommerce_db_dict[
        "insert into ShoppingCart: fifth ShopCart"
    ] = """INSERT INTO ShoppingCart(id_user, id_invoice, date)
            VALUES(5,5,'15/08/2023');
        """
    ecommerce_db_dict[
        "insert into ShoppingCart: sixth ShopCart"
    ] = """INSERT INTO ShoppingCart(id_user, id_invoice, date)
            VALUES(6,6,'19/04/2024');
        """
    ecommerce_db_dict[
        "insert into ShoppingCart: seventh ShopCart"
    ] = """INSERT INTO ShoppingCart(id_user, id_invoice, date)
            VALUES(7,7,'03/05/2024');
        """
    ecommerce_db_dict[
        "insert into ShoppingCart: eighth ShopCart"
    ] = """INSERT INTO ShoppingCart(id_user, id_invoice, date)
            VALUES(8,8,'25/12/2023');
        """
    ecommerce_db_dict[
        "insert into ShoppingCart: ninth ShopCart"
    ] = """INSERT INTO ShoppingCart(id_user, id_invoice, date)
            VALUES(9,9,'01/01/2024');
        """
    ecommerce_db_dict[
        "insert into ShoppingCart: tenth ShopCart"
    ] = """INSERT INTO ShoppingCart(id_user, id_invoice, date)
            VALUES(10,10,'09/02/2024');
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
    ] = """INSERT INTO Product (id_category, id_vat, name, number_of_units, description, tech_specification, image_path, price_ET, popularity)
            VALUES (1, 1, "VTT 1250XC", 10,
            "Ce VTT est conçu pour se lancer dans la pratique du VTT Cross Country (XC). Votre premier
             VTT XC axé performance à prix contenu. Cadre aluminium et transmission 11 vitesses.",
            "Cadre: Aluminium, tubes à épaisseurs variables ; Transmission: Plateau de 32 ; Roues: 29'' ; Amortisseur: simple ; Freins : hydraulique",
            "bdd/assets/products/vtt_1250xc.jpg", 899.99, 23)
        """
    ecommerce_db_dict[
        "insert into Product: ten bikes"
    ] = """INSERT INTO Product (id_category, id_vat, name, number_of_units, description, tech_specification, image_path, price_ET, popularity)
            VALUES
            (1, 1, "VTT Trail 500", 15, "VTT robuste pour les sentiers forestiers et les randonnées en montagne.",
            "Cadre: Aluminium 6061 ; Transmission: Shimano 9 vitesses ; Roues: 27.5'' ; Freins: Disques hydrauliques",
            "bdd/assets/products/vtt_trail_500.jpeg", 749.99, 36),
            (1, 1, "Vélo de route AeroX", 8, "Vélo de route profilé pour les cyclistes avides de performance sur bitume.",
            "Cadre: Carbone ; Transmission: Shimano 105 ; Roues: 700C ; Freins: Patins",
            "bdd/assets/products/aerox.jpeg", 1299.00, 14),
            (1, 1, "VTT XC Pro 900", 5, "Modèle haute performance pour le cross-country intensif.",
            "Cadre: Carbone ; Transmission: SRAM Eagle 12v ; Amortisseur: RockShox ; Freins: Disques hydrauliques",
            "bdd/assets/products/xc_pro_900.jpg", 1999.99, 9),
            (1, 1, "VTC Urbain 300", 20, "Vélo tout chemin idéal pour les trajets quotidiens en ville ou en campagne.",
            "Cadre: Acier ; Vitesses: 7 intégrées ; Porte-bagages ; Garde-boue",
            "bdd/assets/products/vtc_urbain_300.jpeg", 499.50, 4),
            (1, 1, "Gravel TerraMix", 7, "Vélo gravel polyvalent pour la route et les chemins non goudronnés.",
            "Cadre: Aluminium ; Transmission: 2x10 Shimano GRX ; Pneus: 40 mm ; Freins: Disques",
            "bdd/assets/products/terramix.jpeg", 1149.00, 28),
            (1, 1, "Vélo enfant KidRider 16''", 12, "Vélo 16 pouces pour enfants de 4 à 6 ans avec stabilisateurs amovibles.",
            "Cadre: Acier ; Transmission: Monovitesse ; Freins: V-brake",
            "bdd/assets/products/kidrider_16.jpeg", 159.90, 7),
            (1, 1, "Vélo électrique E-City 400", 6, "Vélo à assistance électrique pour les déplacements urbains confortables.",
            "Cadre: Aluminium ; Moteur: 250W ; Batterie: 36V 10Ah ; Autonomie: 70 km",
            "bdd/assets/products/e_city_400.jpeg", 1699.00, 0),
            (1, 1, "Fixie Urban Classic", 10, "Vélo fixie élégant et minimaliste pour la ville.",
            "Cadre: Acier chromé ; Transmission: Single Speed ; Freins: Caliper",
            "bdd/assets/products/fixie_urban_classic.jpeg", 399.00, 45),
            (1, 1, "Fatbike SnowBeast", 3, "Vélo tout-terrain à gros pneus pour rouler sur neige ou sable.",
            "Cadre: Aluminium ; Pneus: 4.5'' ; Transmission: Shimano 1x9 ; Freins: Disques",
            "bdd/assets/products/snowbeast.jpeg", 899.99, 34),
            (1, 1, "Vélo pliant Compact 20", 9, "Vélo pliable pour les trajets multimodaux et les petits espaces.",
            "Cadre: Aluminium pliant ; Roues: 20'' ; Vitesses: 6 ; Porte-bagages intégré",
            "bdd/assets/products/compact_20.jpeg", 569.00, 23);
        """
    ecommerce_db_dict[
        "insert into Product: ten accessories"
    ] = """INSERT INTO Product (id_category, id_vat, name, number_of_units, description, tech_specification, image_path, price_ET, popularity)
            VALUES
            (2, 1, "Casque UrbanRide", 25, "Casque léger et ventilé pour les trajets urbains.",
            "Taille: M/L ; Certification: EN1078 ; Poids: 280g ; 14 aérations",
            "bdd/assets/products/casque_urbanride.jpeg", 49.99, 12),
            (2, 1, "Antivol U LockMax", 30, "Antivol en U haute sécurité avec double verrouillage.",
            "Matériau: Acier trempé ; Dimensions: 18x24cm ; Serrure anti-perçage",
            "bdd/assets/products/ulockmax.jpeg", 59.90, 56),
            (2, 1, "Lumières LED avant/arrière", 40, "Kit de lumières rechargeables pour une meilleure visibilité de nuit.",
            "Batterie: USB ; Autonomie: 10h ; Modes: 4 ; Étanchéité: IPX4",
            "bdd/assets/products/lumieres_led.jpeg", 24.90, 3),
            (2, 1, "Pompe à pied ProAir", 18, "Pompe avec manomètre pour un gonflage précis de tous types de pneus.",
            "Pression max: 11 bars ; Corps: aluminium ; Embout: Presta/Schrader",
            "bdd/assets/products/pompe_proair.jpeg", 39.00, 6),
            (2, 1, "Bidon isotherme 600ml", 50, "Bidon cycliste double paroi pour conserver vos boissons au frais.",
            "Matériau: Sans BPA ; Capacité: 600ml ; Poids: 180g",
            "bdd/assets/products/bidon_600.jpeg", 14.50, 2),
            (2, 1, "Selle Gel Confort+", 22, "Selle large avec gel pour une assise confortable sur longue distance.",
            "Rails: Acier ; Housse: Synthétique ; Longueur: 270mm",
            "bdd/assets/products/selle_confort.jpeg", 34.99, 4),
            (2, 1, "Gants été respirants", 35, "Gants légers avec paumes renforcées pour cyclisme estival.",
            "Taille: S à XL ; Matière: Lycra ; Inserts en gel",
            "bdd/assets/products/gants_ete.jpeg", 19.90, 3),
            (2, 1, "Sacoche de cadre étanche", 14, "Sacoche pour smartphone et objets essentiels.",
            "Volume: 1.2L ; Fixation: velcro ; Écran tactile compatible",
            "bdd/assets/products/sacoche_cadre.jpeg", 29.95, 3),
            (2, 1, "Rétroviseur latéral universel", 27, "Rétroviseur adaptable sur guidon gauche ou droit.",
            "Angle réglable ; Fixation: collier universel ; Matériau: ABS",
            "bdd/assets/products/retroviseur.jpeg", 12.99, 8),
            (2, 1, "Porte-bagages arrière aluminium", 11, "Support de charge arrière pour vélos avec freins à disque.",
            "Charge max: 25 kg ; Matériau: Alu anodisé ; Montage rapide",
            "bdd/assets/products/porte_bagages.jpeg", 44.90, 10);
        """
    ecommerce_db_dict[
        "insert into CommandLine: first CommandLine"
    ] = """INSERT INTO CommandLine (id_prod, id_shoppingcart, price_ET, quantity, rate_vat)
            VALUES (1,1,899.99, 2,0.2)
        """
    ecommerce_db_dict[
        "insert into CommandLine: second CommandLine"
    ] = """INSERT INTO CommandLine (id_prod, id_shoppingcart, price_ET, quantity, rate_vat)
            VALUES
            (2, 2, 749.99, 3, 0.2),
            (13, 2, 59.90, 2, 0.2),
            (15, 2, 39.00, 3, 0.2);
        """
    ecommerce_db_dict[
        "insert into CommandLine: third CommandLine"
    ] = """INSERT INTO CommandLine (id_prod, id_shoppingcart, price_ET, quantity, rate_vat)
            VALUES
            (3, 3, 1299.00, 2, 0.2),
            (5, 3, 499.50, 4, 0.2),
            (18, 3, 19.90, 3, 0.2);
        """
    ecommerce_db_dict[
        "insert into CommandLine: fourth CommandLine"
    ] = """INSERT INTO CommandLine (id_prod, id_shoppingcart, price_ET, quantity, rate_vat)
            VALUES
            (6, 4, 1149.00, 2, 0.2),
            (11, 4, 569.00, 1, 0.2),
            (14, 4, 24.90, 5, 0.2);
        """
    ecommerce_db_dict[
        "insert into CommandLine: fifth CommandLine"
    ] = """INSERT INTO CommandLine (id_prod, id_shoppingcart, price_ET, quantity, rate_vat)
            VALUES
            (8, 5, 1699.00, 1, 0.2),
            (9, 5, 399.00, 2, 0.2),
            (19, 5, 29.95, 3, 0.2);
        """
    ecommerce_db_dict[
        "insert into CommandLine: sixth CommandLine"
    ] = """INSERT INTO CommandLine (id_prod, id_shoppingcart, price_ET, quantity, rate_vat)
            VALUES
            (1, 6, 899.99, 2, 0.2),
            (17, 6, 14.50, 2, 0.2);
        """
    ecommerce_db_dict[
        "insert into CommandLine: seventh CommandLine"
    ] = """INSERT INTO CommandLine (id_prod, id_shoppingcart, price_ET, quantity, rate_vat)
            VALUES
            (4, 7, 1999.99, 1, 0.2),
            (10, 7, 899.99, 1, 0.2),
            (20, 7, 12.99, 3, 0.2),
            (16, 7, 50.00, 4, 0.2);
        """
    ecommerce_db_dict[
        "insert into CommandLine: eighth CommandLine"
    ] = """INSERT INTO CommandLine (id_prod, id_shoppingcart, price_ET, quantity, rate_vat)
            VALUES
            (12, 8, 49.99, 2, 0.2),
            (18, 8, 19.90, 2, 0.2),
            (6, 8, 1149.00, 1, 0.2);
        """
    ecommerce_db_dict[
        "insert into CommandLine: ninth CommandLine"
    ] = """INSERT INTO CommandLine (id_prod, id_shoppingcart, price_ET, quantity, rate_vat)
            VALUES
            (7, 9, 159.90, 1, 0.2),
            (14, 9, 24.90, 2, 0.2);
        """
    ecommerce_db_dict[
        "insert into CommandLine: tenth CommandLine"
    ] = """INSERT INTO CommandLine (id_prod, id_shoppingcart, price_ET, quantity, rate_vat)
            VALUES
            (5, 10, 499.50, 2, 0.2),
            (19, 10, 29.95, 1, 0.2),
            (13, 10, 59.90, 1, 0.2),
            (15, 10, 39.00, 2, 0.2);
        """


def generate_password() -> str:
    # Declaring our password
    passwords = [
        "password123",
        "bonjour2024",
        "streamlit",
        "adminadmin",
        "azerty123",
        "testuser",
        "motdepasse",
        "welcome2025",
        "login2025",
        "abc123",
    ]

    for pwd in passwords:
        hashed = bcrypt.hashpw(pwd.encode(), bcrypt.gensalt())
        print(f"{pwd:<18} --- {hashed.decode("utf-8")}")


def create_database(ecommerce_db_dict: dict, database_name: str):
    """Create your database
    Args:
        ecommerce_db_dict (dict): contain all queries to create your database
        database_name (str): database name
    """
    try:
        folder = "bdd/"
        connection = sqlite3.connect(f"{folder}{database_name}.db")
        cursor = connection.cursor()
        for key, sql_command in ecommerce_db_dict.items():
            print(key)
            cursor.execute(sql_command)
        connection.commit()
    except:
        print(f"{database_name} already exist !")


def create_json_file(ecommerce_db_dict: dict, database_name: str):
    # Write data to a JSON file
    folder = "bdd/"
    with open(f"{folder}{database_name}.json", "w") as db_json_file:
        json.dump(ecommerce_db_dict, db_json_file, indent=4, ensure_ascii=False)


def create_database_with_json_file(database_name: str) -> dict:
    """Read your database"""
    try:
        folder = "bdd/"
        with open(f"{folder}{database_name}.json") as db_json_file:
            ecommerce_db_dict = json.load(db_json_file)

        connection = sqlite3.connect(f"{folder}{database_name}.db")
        cursor = connection.cursor()
        for key, sql_command in ecommerce_db_dict.items():
            print(key)
            cursor.execute(sql_command)
        connection.commit()
    except:
        print(f"{database_name} already exist !")


def main():
    db_name = "ecommerce_database"
    ecommerce_db_dict = {}
    create_table_db(ecommerce_db_dict)
    create_insert_into_tables(ecommerce_db_dict)
    create_database(ecommerce_db_dict, db_name)
    create_json_file(ecommerce_db_dict, db_name)
    # create_database_with_json_file(db_name)


if __name__ == "__main__":
    main()

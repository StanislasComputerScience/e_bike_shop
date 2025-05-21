import sqlite3


def create_json_db():
    """Function permit to create json db"""


def create_table_db(ecommerce_db_dict: dict):
    """Function to create table of the db"""
    ecommerce_db_dict[
        "create table Role"
    ] = """CREATE TABLE IF NOT EXISTS Role (
            id_role INTEGER PRIMARY KEY AUTOINCREMENT, 
            name TEXT NOT NULL);"""
    ecommerce_db_dict[
        "create table Connection"
    ] = """CREATE TABLE IF NOT EXISTS Connection (
            id_connection INTEGER PRIMARY KEY AUTOINCREMENT, 
            status TEXT NOT NULL);"""
    ecommerce_db_dict[
        "create table User"
    ] = """CREATE TABLE IF NOT EXISTS User (
            id_user INTEGER PRIMARY KEY AUTOINCREMENT, 
            id_connection INTEGER NOT NULL,
            id_role INTEGER NOT NULL,
            name TEXT NOT NULL,
            firstname TEXT NOT NULL,
            birth_date TEXT,
            email TEXT NOT NULL,
            phone TEXT,
            FOREIGN KEY(id_connection) REFERENCES Connection(id_connection),
            FOREIGN KEY(id_role) REFERENCES Role(id_role));"""
    ecommerce_db_dict[
        "create table Address"
    ] = """CREATE TABLE IF NOT EXISTS Address (
            id_address INTEGER PRIMARY KEY AUTOINCREMENT, 
            id_user INTEGER NOT NULL,
            number INTEGER NOT NULL,
            street TEXT NOT NULL,
            postal_code TEXT NOT NULL,
            city TEXT NOT NULL,
            FOREIGN KEY(id_user) REFERENCES User(id_user));"""
    ecommerce_db_dict[
        "create table Category"
    ] = """CREATE TABLE IF NOT EXISTS Category (
            id_category INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, 
            name TEXT NOT NULL
        )"""
    ecommerce_db_dict[
        "create table VAT"
    ] = """CREATE TABLE IF NOT EXISTS VAT (
            id_vat INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, 
            rate REAL UNSIGNED NOT NULL,
            name TEXT NOT NULL
        )"""
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
        )"""
    ecommerce_db_dict[
        "create table ShoppingCart"
    ] = """CREATE TABLE IF NOT EXISTS ShoppingCart (
            id_shoppingcart INTEGER PRIMARY KEY AUTOINCREMENT, 
            id_user INTEGER NOT NULL,
            date TEXT NOT NULL,
            FOREIGN KEY(id_user) REFERENCES User(id_user));"""
    ecommerce_db_dict[
        "create table Invoice"
    ] = """CREATE TABLE IF NOT EXISTS Invoice (
            id_invoice INTEGER PRIMARY KEY AUTOINCREMENT, 
            id_shoppingcart INTEGER NOT NULL,
            date TEXT NOT NULL,
            FOREIGN KEY(id_shoppingcart) REFERENCES ShoppingCart(id_shoppingcart));"""
    ecommerce_db_dict[
        "create table CommandeLine"
    ] = """CREATE TABLE IF NOT EXISTS CommandLine (
            id_prod INTEGER NOT NULL,
            id_shoppingcart INTEGER NOT NULL,
            price_ET REAL UNSIGNED NOT NULL,
            rate_vat REAL UNSIGNED NOT NULL,
            PRIMARY KEY(id_prod,id_shoppingcart)
            FOREIGN KEY(id_prod) REFERENCES Product(id_prod),
            FOREIGN KEY(id_shoppingcart) REFERENCES ShoppingCart(id_shoppingcart)
       )"""


def create_insert_into_tables(ecommerce_db_dict: dict):
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

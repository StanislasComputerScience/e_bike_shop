from pymongo import MongoClient


def create_collection_product():
    # 1. Connexion
    client = MongoClient("mongodb://localhost:27017/")
    db = client["ecommerce_database"]

    # 2. Définition du schéma
    schema = {
        "bsonType": "object",
        "required": [
            "name",
            "category",
            "number_of_units",
            "description",
            "tech_specification",
            "image_path",
            "price_ET",
            "popularity",
            "name_vat",
            "rate_vat",
        ],
        "properties": {
            "name": {"bsonType": "string"},
            "category": {
                "enum": ["bike", "accessory"],
                "description": "Must be either a bike or an accessory",
            },
            "number_of_units": {"bsonType": "int"},
            "description": {"bsonType": "string"},
            "tech_specification": {"bsonType": "string"},
            "image_path": {"bsonType": "string"},
            "price_ET": {"bsonType": "double", "minimum": 0},
            "popularity": {"bsonType": "int", "minimum": 0},
            "name_vat": {
                "enum": ["french (standard)"],
                "description": "Must be french (standard)",
                },
            "rate_vat": {"bsonType": "double"},
        },
    }

    validator = {"$jsonSchema": schema}

    # Check if table product exist
    try:
        # 3. Création de la collection avec validation
        collection = db.create_collection("Product", validator=validator)
    except:
        db.Product.drop()
        # 3. Création de la collection avec validation
        collection = db.create_collection("Product", validator=validator)

    print("Collection 'Product' créée avec validation JSON Schema.")

    # 4. Insérer un document (INSERT ONE)
    products = list()
    products.append(
        {
            "name": "VTT 1250XC",
            "category": "bike",
            "number_of_units": 10,
            "description": "Ce VTT est conçu pour se lancer dans la pratique du VTT Cross Country (XC). Votre premier VTT XC axé performance à prix contenu. Cadre aluminium et transmission 11 vitesses.",
            "tech_specification": "Cadre: Aluminium, tubes à épaisseurs variables ; Transmission: Plateau de 32 ; Roues: 29'' ; Amortisseur: simple ; Freins : hydraulique",
            "image_path": "bdd/assets/products/vtt_1250xc.jpg",
            "price_ET": 899.99,
            "popularity": 23,
            "name_vat": "french (standard)",
            "rate_vat": 0.2,
        }
    )
    products.append(
        {
            "name": "VTT Trail 500",
            "category": "bike",
            "number_of_units": 15,
            "description": "VTT robuste pour les sentiers forestiers et les randonnées en montagne.",
            "tech_specification": "Cadre: Aluminium 6061 ; Transmission: Shimano 9 vitesses ; Roues: 27.5'' ; Freins: Disques hydrauliques",
            "image_path": "bdd/assets/products/vtt_trail_500.jpeg",
            "price_ET": 749.99,
            "popularity": 36,
            "name_vat": "french (standard)",
            "rate_vat": 0.2,
        }
    )
    products.append(
        {
            "name": "Vélo de route AeroX",
            "category": "bike",
            "number_of_units": 8,
            "description": "Vélo de route profilé pour les cyclistes avides de performance sur bitume.",
            "tech_specification": "Cadre: Carbone ; Transmission: Shimano 105 ; Roues: 700C ; Freins: Patins",
            "image_path": "bdd/assets/products/aerox.jpeg",
            "price_ET": 1299.00,
            "popularity": 14,
            "name_vat": "french (standard)",
            "rate_vat": 0.2,
        }
    )
    products.append(
        {
            "name": "VTT XC Pro 900",
            "category": "bike",
            "number_of_units": 5,
            "description": "Modèle haute performance pour le cross-country intensif.",
            "tech_specification": "Cadre: Carbone ; Transmission: SRAM Eagle 12v ; Amortisseur: RockShox ; Freins: Disques hydrauliques",
            "image_path": "bdd/assets/products/xc_pro_900.jpg",
            "price_ET": 1999.99,
            "popularity": 9,
            "name_vat": "french (standard)",
            "rate_vat": 0.2,
        }
    )
    products.append(
        {
            "name": "VTC Urbain 300",
            "category": "bike",
            "number_of_units": 20,
            "description": "Vélo tout chemin idéal pour les trajets quotidiens en ville ou en campagne.",
            "tech_specification": "Cadre: Acier ; Vitesses: 7 intégrées ; Porte-bagages ; Garde-boue",
            "image_path": "bdd/assets/products/vtc_urbain_300.jpeg",
            "price_ET": 499.50,
            "popularity": 4,
            "name_vat": "french (standard)",
            "rate_vat": 0.2,
        }
    )
    products.append(
        {
            "name": "Gravel TerraMix",
            "category": "bike",
            "number_of_units": 7,
            "description": "Vélo gravel polyvalent pour la route et les chemins non goudronnés.",
            "tech_specification": "Cadre: Aluminium ; Transmission: 2x10 Shimano GRX ; Pneus: 40 mm ; Freins: Disques",
            "image_path": "bdd/assets/products/terramix.jpeg",
            "price_ET": 1149.00,
            "popularity": 28,
            "name_vat": "french (standard)",
            "rate_vat": 0.2,
        }
    )
    products.append(
        {
            "name": "Vélo enfant KidRider 16''",
            "category": "bike",
            "number_of_units": 12,
            "description": "Vélo 16 pouces pour enfants de 4 à 6 ans avec stabilisateurs amovibles.",
            "tech_specification": "Cadre: Acier ; Transmission: Monovitesse ; Freins: V-brake",
            "image_path": "bdd/assets/products/kidrider_16.jpeg",
            "price_ET": 159.90,
            "popularity": 7,
            "name_vat": "french (standard)",
            "rate_vat": 0.2,
        }
    )
    products.append(
        {
            "name": "Vélo électrique E-City 400",
            "category": "bike",
            "number_of_units": 6,
            "description": "Vélo à assistance électrique pour les déplacements urbains confortables.",
            "tech_specification": "Cadre: Aluminium ; Moteur: 250W ; Batterie: 36V 10Ah ; Autonomie: 70 km",
            "image_path": "bdd/assets/products/e_city_400.jpeg",
            "price_ET": 1699.00,
            "popularity": 0,
            "name_vat": "french (standard)",
            "rate_vat": 0.2,
        }
    )
    products.append(
        {
            "name": "Fixie Urban Classic",
            "category": "bike",
            "number_of_units": 10,
            "description": "Vélo fixie élégant et minimaliste pour la ville.",
            "tech_specification": "Cadre: Acier chromé ; Transmission: Single Speed ; Freins: Caliper",
            "image_path": "bdd/assets/products/fixie_urban_classic.jpeg",
            "price_ET": 399.00,
            "popularity": 45,
            "name_vat": "french (standard)",
            "rate_vat": 0.2,
        }
    )
    products.append(
        {
            "name": "Fatbike SnowBeast",
            "category": "bike",
            "number_of_units": 3,
            "description": "Vélo tout-terrain à gros pneus pour rouler sur neige ou sable.",
            "tech_specification": "Cadre: Aluminium ; Pneus: 4.5'' ; Transmission: Shimano 1x9 ; Freins: Disques",
            "image_path": "bdd/assets/products/snowbeast.jpeg",
            "price_ET": 899.99,
            "popularity": 34,
            "name_vat": "french (standard)",
            "rate_vat": 0.2,
        }
    )
    products.append(
        {
            "name": "Vélo pliant Compact 20",
            "category": "bike",
            "number_of_units": 9,
            "description": "Vélo pliable pour les trajets multimodaux et les petits espaces.",
            "tech_specification": "Cadre: Aluminium pliant ; Roues: 20'' ; Vitesses: 6 ; Porte-bagages intégré",
            "image_path": "bdd/assets/products/compact_20.jpeg",
            "price_ET": 569.00,
            "popularity": 23,
            "name_vat": "french (standard)",
            "rate_vat": 0.2,
        }
    )
    products.append(
        {
            "name": "Casque UrbanRide",
            "category": "accessory",
            "number_of_units": 25,
            "description": "Casque léger et ventilé pour les trajets urbains.",
            "tech_specification": "Taille: M/L ; Certification: EN1078 ; Poids: 280g ; 14 aérations",
            "image_path": "bdd/assets/products/casque_urbanride.jpeg",
            "price_ET": 49.99,
            "popularity": 12,
            "name_vat": "french (standard)",
            "rate_vat": 0.2,
        }
    )
    products.append(
        {
            "name": "Antivol U LockMax",
            "category": "accessory",
            "number_of_units": 30,
            "description": "Antivol en U haute sécurité avec double verrouillage.",
            "tech_specification": "Matériau: Acier trempé ; Dimensions: 18x24cm ; Serrure anti-perçage",
            "image_path": "bdd/assets/products/ulockmax.jpeg",
            "price_ET": 59.90,
            "popularity": 56,
            "name_vat": "french (standard)",
            "rate_vat": 0.2,
        }
    )
    products.append(
        {
            "name": "Lumières LED avant/arrière",
            "category": "accessory",
            "number_of_units": 40,
            "description": "Kit de lumières rechargeables pour une meilleure visibilité de nuit.",
            "tech_specification": "Batterie: USB ; Autonomie: 10h ; Modes: 4 ; Étanchéité: IPX4",
            "image_path": "bdd/assets/products/lumieres_led.jpeg",
            "price_ET": 24.90,
            "popularity": 3,
            "name_vat": "french (standard)",
            "rate_vat": 0.2,
        }
    )
    products.append(
        {
            "name": "Pompe à pied ProAir",
            "category": "accessory",
            "number_of_units": 18,
            "description": "Pompe avec manomètre pour un gonflage précis de tous types de pneus.",
            "tech_specification": "Pression max: 11 bars ; Corps: aluminium ; Embout: Presta/Schrader",
            "image_path": "bdd/assets/products/pompe_proair.jpeg",
            "price_ET": 39.00,
            "popularity": 6,
            "name_vat": "french (standard)",
            "rate_vat": 0.2,
        }
    )
    products.append(
        {
            "name": "Bidon isotherme 600ml",
            "category": "accessory",
            "number_of_units": 50,
            "description": "Bidon cycliste double paroi pour conserver vos boissons au frais.",
            "tech_specification": "Matériau: Sans BPA ; Capacité: 600ml ; Poids: 180g",
            "image_path": "bdd/assets/products/bidon_600.jpeg",
            "price_ET": 14.50,
            "popularity": 2,
            "name_vat": "french (standard)",
            "rate_vat": 0.2,
        }
    )
    products.append(
        {
            "name": "Selle Gel Confort+",
            "category": "accessory",
            "number_of_units": 22,
            "description": "Selle large avec gel pour une assise confortable sur longue distance.",
            "tech_specification": "Rails: Acier ; Housse: Synthétique ; Longueur: 270mm",
            "image_path": "bdd/assets/products/selle_confort.jpeg",
            "price_ET": 34.99,
            "popularity": 4,
            "name_vat": "french (standard)",
            "rate_vat": 0.2,
        }
    )
    products.append(
        {
            "name": "Gants été respirants",
            "category": "accessory",
            "number_of_units": 35,
            "description": "Gants légers avec paumes renforcées pour cyclisme estival.",
            "tech_specification": "Taille: S à XL ; Matière: Lycra ; Inserts en gel",
            "image_path": "bdd/assets/products/gants_ete.jpeg",
            "price_ET": 19.90,
            "popularity": 3,
            "name_vat": "french (standard)",
            "rate_vat": 0.2,
        }
    )
    products.append(
        {
            "name": "Sacoche de cadre étanche",
            "category": "accessory",
            "number_of_units": 14,
            "description": "Sacoche pour smartphone et objets essentiels.",
            "tech_specification": "Volume: 1.2L ; Fixation: velcro ; Écran tactile compatible",
            "image_path": "bdd/assets/products/sacoche_cadre.jpeg",
            "price_ET": 29.95,
            "popularity": 3,
            "name_vat": "french (standard)",
            "rate_vat": 0.2,
        }
    )
    products.append(
        {
            "name": "Rétroviseur latéral universel",
            "category": "accessory",
            "number_of_units": 27,
            "description": "Rétroviseur adaptable sur guidon gauche ou droit.",
            "tech_specification": "Angle réglable ; Fixation: collier universel ; Matériau: ABS",
            "image_path": "bdd/assets/products/retroviseur.jpeg",
            "price_ET": 12.99,
            "popularity": 8,
            "name_vat": "french (standard)",
            "rate_vat": 0.2,
        }
    )
    products.append(
        {
            "name": "Porte-bagages arrière aluminium",
            "category": "accessory",
            "number_of_units": 11,
            "description": "Support de charge arrière pour vélos avec freins à disque.",
            "tech_specification": "Charge max: 25 kg ; Matériau: Alu anodisé ; Montage rapide",
            "image_path": "bdd/assets/products/porte_bagages.jpeg",
            "price_ET": 44.90,
            "popularity": 10,
            "name_vat": "french (standard)",
            "rate_vat": 0.2,
        }
    )

    result_many = collection.insert_many(products)
    print("ID inséré pour VTT 1250XC :", result_many)


def main():
    create_collection_product()


if __name__ == "__main__":
    main()

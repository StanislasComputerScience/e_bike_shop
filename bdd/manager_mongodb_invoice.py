from pymongo import MongoClient
from bson.objectid import ObjectId
import datetime as dt
import random
import pprint
import manager_mongodb_user as user
import const_values as cv


def create_collection_invoice():
    """Crée la collection Invoice avec schéma de validation et insère une facture générée dynamiquement."""
    client = MongoClient(cv.MONGODB_LOCAL_PATH)
    db = client[cv.MONGODB_NAME]

    # 1. Schéma JSON
    schema = {
        "bsonType": "object",
        "required": ["date", "commandlines"],
        "properties": {
            "date": {"bsonType": "date"},
            "commandlines": {
                "bsonType": "array",
                "minItems": 1,
                "items": {
                    "bsonType": "object",
                    "required": ["id_product", "price_ET", "quantity", "rate_VAT"],
                    "properties": {
                        "id_product": {"bsonType": "objectId"},
                        "price_ET": {"bsonType": "double", "minimum": 0.0},
                        "quantity": {"bsonType": "int", "minimum": 0},
                        "rate_VAT": {"bsonType": "double", "minimum": 0.0},
                    },
                },
            },
        },
    }

    # 2. Création de la collection
    try:
        db.create_collection(
            "Invoice", validator={"$jsonSchema": schema}, validationLevel="strict"
        )
        print("✅ Collection 'Invoice' créée avec validation.")
    except Exception as e:
        print("⚠️ Collection existante ou erreur :", e)
        db.Invoice.drop()
        print("♻️ Collection 'Invoice' supprimée et recréée.")
        db.create_collection(
            "Invoice", validator={"$jsonSchema": schema}, validationLevel="strict"
        )

    # 3. Récupération des produits
    products = user.find_all_products()
    if len(products) < 5:
        raise ValueError("❌ Pas assez de produits pour créer une facture.")

    # 4. Génération des lignes de commande
    selected_products = random.sample(products, k=5)
    commandlines = []

    for product in selected_products:
        try:
            commandlines.append(
                {
                    "id_product": ObjectId(product["_id"]),
                    "price_ET": float(product["price_ET"]),
                    "quantity": int(random.randint(1, 5)),
                    "rate_VAT": float(product["rate_vat"]),
                }
            )
        except KeyError as ke:
            print(f"❌ Clé manquante dans le produit : {ke}")
            pprint.pprint(product)
            continue
        except Exception as ex:
            print(f"❌ Erreur dans le traitement du produit : {ex}")
            pprint.pprint(product)
            continue

    # 5. Création de la facture
    invoice_data = {
        "date": dt.datetime.now(),
        "commandlines": commandlines,
    }

    print("🧾 Facture générée :")
    pprint.pprint(invoice_data)

    # 6. Insertion dans MongoDB
    try:
        result = db["Invoice"].insert_one(invoice_data)
        print("✅ Facture insérée avec ID :", result.inserted_id)
    except Exception as insert_error:
        print("❌ Erreur à l'insertion :", insert_error)


if __name__ == "__main__":
    create_collection_invoice()

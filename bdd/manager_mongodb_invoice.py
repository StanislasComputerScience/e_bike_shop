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
        "required": ["date", "id_user", "shoppingcart"],
        "properties": {
            "date": {
                "bsonType": "date",
            },
            "id_user": {
                "bsonType": "objectId",
            },
            "shoppingcart": {
                "bsonType": "array",
                "minItems": 1,
                "items": {
                    "bsonType": "object",
                    "required": ["id_product", "price_ET", "quantity", "rate_vat"],
                    "properties": {
                        "id_product": {"bsonType": "objectId"},
                        "price_ET": {"bsonType": "double", "minimum": 0.0},
                        "quantity": {"bsonType": "int", "minimum": 0},
                        "rate_vat": {"bsonType": "double", "minimum": 0.0},
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

    for _ in range(2):
        # 3. Récupération des produits
        products = user.create_shoppingcart(5)
        user_id = user.find_user_id("Dupont", "Paul")
        # 4. Création de la facture
        invoice_data = {
            "date": dt.datetime.now(),
            "id_user": user_id,
            "shoppingcart": products,
        }

        print("🧾 Facture générée :")
        pprint.pprint(invoice_data)

        # 5. Insertion dans MongoDB
        try:
            result = db["Invoice"].insert_one(invoice_data)
            print("✅ Facture insérée avec ID :", result.inserted_id)
        except Exception as insert_error:
            print("❌ Erreur à l'insertion :", insert_error)


if __name__ == "__main__":
    create_collection_invoice()

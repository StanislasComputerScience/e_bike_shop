import os
import streamlit as st

st.subheader("Mosaïque de produits :")

path = "./bdd/assets/products/"

list_products = []

# Charger les produits
for i, f in enumerate(os.listdir(path)):
    chemin = os.path.join(path, f)
    if os.path.isfile(chemin):
        list_products.append(
            {
                "nom": f"Produit_{i}",
                "description": f"Produit n°{i+1} : vélo performant pour usage quotidien.",
                "chemin_image": chemin,
            }
        )

# Afficher en tableau de 3 colonnes par ligne
n_colonnes = 3
for i in range(0, len(list_products), n_colonnes):
    cols = st.columns(n_colonnes)
    for j in range(n_colonnes):
        if i + j < len(list_products):
            product = list_products[i + j]
            with cols[j]:
                st.image(product["chemin_image"], use_container_width=True)
                st.write(product["description"])

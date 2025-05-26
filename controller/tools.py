from .controller import product_catalog
import streamlit as st

# def load_products_and_c():
#     # Chargement des produits
#     l_products = product_catalog()
#     name_products = [p["name"] for p in l_products]

#     # Initialisation de l'index
#     if "c" not in st.session_state:
#         st.session_state.c = 0

#     # Fonction appelée quand on change de produit via la radio
#     def update_choice():
#         st.session_state.c = name_products.index(st.session_state.choix_radio)

#     # Affichage du bouton radio (il est toujours affiché, avec clé)


#     return l_products, name_products

def load_products_and_c():
    l_products = product_catalog()
    name_products = [p["name"] for p in l_products]

    if "c" not in st.session_state:
        st.session_state.c = 0

    return l_products, name_products


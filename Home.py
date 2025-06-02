import os
import streamlit as st
import const_values as cv

if cv.BDD_TECHNO == "mongodb":
    import controller_mongod.controller_mongod as control
else:
    import controller.controller as control
from random import choice

# CSS pour centrer le texte
st.markdown(
    """
<style>
.large-text {
    font-size: 24px;
    font-weight: bold;
    text-align: center;
    line-height: 1.2;
}
</style>
""",
    unsafe_allow_html=True,
)

# Crée 2 colonnes : image et message bienvenue
colonne_image, colonne_titre = st.columns([3, 2])

with colonne_image:
    match choice([1, 2]):
        case 1:
            st.image("./assets/eShop-bike.png")
        case 2:
            st.image("./assets/eShop-bike2.png")

with colonne_titre:
    st.markdown(
        '<div class="large-text">Bienvenue sur eBike-Shop !</div>',
        unsafe_allow_html=True,
    )

most_popular_products = control.most_popular_products()
most_products_buy = control.most_products_buy()

st.subheader("Produits les plus populaires :")
# Créer 2 colonnes
colonne_gauche, colonne_droite = st.columns(2)

with colonne_gauche:
    st.image(
        most_popular_products[0]["image_path"],
        caption=most_popular_products[0]["name"],
        use_container_width=True,
    )

with colonne_droite:
    st.image(
        most_popular_products[1]["image_path"],
        caption=most_popular_products[1]["name"],
        use_container_width=True,
    )

st.subheader("Produits les plus vendus :")
colonne_gauche, colonne_droite = st.columns(2)

with colonne_gauche:
    st.image(
        most_products_buy[0]["image_path"],
        caption=most_products_buy[0]["name"],
        use_container_width=True,
    )

with colonne_droite:
    st.image(
        most_products_buy[1]["image_path"],
        caption=most_products_buy[1]["name"],
        use_container_width=True,
    )

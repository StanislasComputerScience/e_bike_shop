import os
import streamlit as st
import controller.controller as control

ecommerce_db_name = "ecommerce_database"

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
colonne_image, colonne_titre = st.columns([1, 3])

with colonne_image:

    st.image("./bdd/assets/velo4.jpeg")

with colonne_titre:
    st.markdown(
        '<div class="large-text">Bienvenue sur eBike-Shop !</div>',
        unsafe_allow_html=True,
    )

most_popular_products = control.most_popular_products(ecommerce_db_name)
most_products_buy = control.most_products_buy(ecommerce_db_name)

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

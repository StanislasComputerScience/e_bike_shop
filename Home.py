import os
import streamlit as st


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

st.subheader("Produits les plus populaires :")
# Créer 2 colonnes
colonne_gauche, colonne_droite = st.columns(2)

with colonne_gauche:
    st.image("./assets/Velo1.jpeg", caption="Vélo 1", use_container_width=True)

with colonne_droite:
    st.image("./assets/Velo2.jpeg", caption="Vélo 2", use_container_width=True)


st.subheader("produits les plus vendus :")
colonne_gauche, colonne_droite = st.columns(2)

with colonne_gauche:
    st.image("./assets/Velo1.jpeg", caption="Vélo 1", use_container_width=True)

with colonne_droite:
    st.image("./assets/velo3.jpeg", caption="Vélo 1", use_container_width=True)

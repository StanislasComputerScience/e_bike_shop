import os
import streamlit as st

# Initialisation
if "c" not in st.session_state:
    st.session_state.c = 0




# CSS pour centrer le texte
st.markdown("""
<style>
.large-text {
    font-size: 24px;
    font-weight: bold;
    text-align: center;
    line-height: 1.2;
}
</style>
""", unsafe_allow_html=True)

# Crée 3 colonnes : bouton "Précédent", titre centré, "Suivant" décalé à droite
col1, col2, col3 = st.columns([1, 3, 1])

with col1:

        st.image("./assets/velo4.jpeg")

with col2:
    st.markdown('<div class="large-text">Bienvenue sur eBike-Shop !</div>', unsafe_allow_html=True)

st.subheader("Produits les plus populaires :")
# Créer 2 colonnes
col1, col2 = st.columns(2)

with col1:
    st.image("./assets/Velo1.jpeg", caption="Vélo 1", use_container_width=True)

with col2:
    st.image("./assets/Velo2.jpeg", caption="Vélo 2", use_container_width=True)

# def main():
#     # Pages principales définies manuellement
#     liste_pages = [
#         "0. Page d'accueil",
#         "1. Catalogue de produits",
#         "2. Panier",
#     ]



#     # st.subheader("produits les plus populaires :")
#     # st.image("./assets/Velo1.jpeg")
#     # st.image("./assets/Velo2.jpeg")





st.subheader("produits les plus vendus :")

st.image("./assets/velo3.jpeg")





    # st.write("Calcul des Salaires Mensuels dans une Entreprise avec plusieurs filiales.")
    # st.image("image.webp", width=300)
    # st.markdown("**Contexte du projet**")
    # st.write("Bla bla...")


# if __name__ == "__main__":
#     main()
